/**
 * Speech Recognition and Pronunciation Scoring Engine
 */

export interface SpeechRecognitionResultState {
  transcript: string;
  score: number; // 0 to 100
  isMatch: boolean; // >= 70%
  feedback: string;
}

// Levenshtein distance
function levenshteinDistance(s1: string, s2: string): number {
  const m = s1.length;
  const n = s2.length;
  const dp: number[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
      }
    }
  }

  return dp[m][n];
}

// Clean and normalize strings for robust multi-language comparison
export function normalizePhrase(text: string): string {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // remove diacritics
    .replace(/[¡!¿?,.:;"'()—\-_]/g, '') // remove punctuation
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Compare spoken transcript with target phrase
 * Returns score between 0 and 100
 */
export function calculatePronunciationScore(transcript: string, targetPhrase: string): {
  score: number;
  isMatch: boolean;
  feedback: string;
} {
  const cleanTranscript = normalizePhrase(transcript);
  const cleanTarget = normalizePhrase(targetPhrase);

  if (!cleanTranscript) {
    return {
      score: 0,
      isMatch: false,
      feedback: "Couldn't hear clearly. Please tap the mic and try again!",
    };
  }

  // Exact match
  if (cleanTranscript === cleanTarget) {
    return {
      score: 100,
      isMatch: true,
      feedback: 'Flawless native pronunciation! Perfect!',
    };
  }

  // Character similarity
  const maxLen = Math.max(cleanTranscript.length, cleanTarget.length);
  const dist = levenshteinDistance(cleanTranscript, cleanTarget);
  const charScore = maxLen === 0 ? 1 : Math.max(0, (maxLen - dist) / maxLen);

  // Word token overlap
  const targetWords = cleanTarget.split(' ').filter(Boolean);
  const spokenWords = cleanTranscript.split(' ').filter(Boolean);

  let matchedWordsCount = 0;
  for (const tw of targetWords) {
    const hasWord = spokenWords.some((sw) => {
      if (sw === tw) return true;
      if (Math.abs(sw.length - tw.length) <= 2 && levenshteinDistance(sw, tw) <= 2) return true;
      return false;
    });
    if (hasWord) matchedWordsCount++;
  }

  const wordScore = targetWords.length > 0 ? matchedWordsCount / targetWords.length : 0;

  // Combined score weighted towards word accuracy and phonetics
  const finalPercentage = Math.min(100, Math.round((wordScore * 0.6 + charScore * 0.4) * 100));

  const isMatch = finalPercentage >= 70;

  let feedback = 'Almost there! Listen closely to the native audio and give it another go.';
  if (finalPercentage >= 90) {
    feedback = 'Outstanding pronunciation! You nailed every syllable!';
  } else if (finalPercentage >= 75) {
    feedback = 'Great job! Very clear and natural cadence!';
  } else if (finalPercentage >= 50) {
    feedback = 'Good attempt! Try slowing down slightly on tricky sounds.';
  }

  return {
    score: finalPercentage,
    isMatch,
    feedback,
  };
}

// Browser Web Speech Recognition Wrapper
export interface SpeechRecognitionInterface {
  continuous: boolean;
  interimResults: boolean;
  lang: string;
  start: () => void;
  stop: () => void;
  abort: () => void;
  onstart: (() => void) | null;
  onresult: ((event: unknown) => void) | null;
  onerror: ((event: unknown) => void) | null;
  onend: (() => void) | null;
}

export function isSpeechRecognitionSupported(): boolean {
  if (typeof window === 'undefined') return false;
  return Boolean(
    (window as unknown as { SpeechRecognition?: unknown }).SpeechRecognition ||
    (window as unknown as { webkitSpeechRecognition?: unknown }).webkitSpeechRecognition
  );
}

export function createSpeechRecognizer(
  speechLocale: string,
  onResult: (transcript: string) => void,
  onError: (err: string) => void,
  onStart: () => void,
  onEnd: () => void
): { start: () => void; stop: () => void; abort: () => void } | null {
  if (!isSpeechRecognitionSupported()) return null;

  try {
    const windowObj = window as unknown as {
      SpeechRecognition?: new () => SpeechRecognitionInterface;
      webkitSpeechRecognition?: new () => SpeechRecognitionInterface;
    };

    const SpeechRecConstructor = windowObj.SpeechRecognition || windowObj.webkitSpeechRecognition;
    if (!SpeechRecConstructor) return null;

    const recognizer = new SpeechRecConstructor();
    recognizer.continuous = false;
    recognizer.interimResults = false;
    recognizer.lang = speechLocale;

    recognizer.onstart = onStart;

    recognizer.onresult = (event: unknown) => {
      try {
        const evt = event as {
          results: { [index: number]: { [index: number]: { transcript: string } } };
        };
        const transcript = evt?.results?.[0]?.[0]?.transcript || '';
        onResult(transcript);
      } catch (e) {
        console.error('Speech parsing error', e);
        onError('Could not parse voice response');
      }
    };

    recognizer.onerror = (event: unknown) => {
      const errEvent = event as { error?: string };
      console.warn('SpeechRecognition error:', errEvent?.error);
      onError(errEvent?.error || 'Speech recognition encountered an issue.');
    };

    recognizer.onend = onEnd;

    return {
      start: () => {
        try {
          recognizer.start();
        } catch {
          // in case it's already running
        }
      },
      stop: () => {
        try {
          recognizer.stop();
        } catch {
          // ignore
        }
      },
      abort: () => {
        try {
          recognizer.abort();
        } catch {
          // ignore
        }
      },
    };
  } catch (err) {
    console.warn('Failed to initialize speech recognition:', err);
    return null;
  }
}
