/**
 * Web Audio API synthesized chimes and Web Speech API Synthesis
 * Includes unified global mute/unmute management and browser media sync.
 */

let audioCtx: AudioContext | null = null;
let masterGain: GainNode | null = null;

let isGlobalMuted: boolean = (() => {
  try {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('linguajunior_audio_muted') === 'true';
    }
  } catch {
    // ignore
  }
  return false;
})();

function getAudioContext(): AudioContext | null {
  try {
    if (typeof window === 'undefined') return null;
    const AudioContextClass =
      window.AudioContext ||
      (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (!AudioContextClass) return null;
    if (!audioCtx || audioCtx.state === 'closed') {
      audioCtx = new AudioContextClass();
      masterGain = null;
    }
    if (!masterGain && audioCtx) {
      masterGain = audioCtx.createGain();
      masterGain.gain.setValueAtTime(isGlobalMuted ? 0 : 1, audioCtx.currentTime);
      masterGain.connect(audioCtx.destination);
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  } catch {
    return null;
  }
}

/**
 * Check if the application/browser audio is currently muted
 */
export function isAudioMuted(): boolean {
  return isGlobalMuted;
}

/**
 * Set the global audio mute state and sync with Web Audio API, Web Speech, and Media elements
 */
export function setGlobalAudioMuted(muted: boolean) {
  isGlobalMuted = muted;

  if (typeof window !== 'undefined') {
    try {
      localStorage.setItem('linguajunior_audio_muted', String(muted));
    } catch {
      // ignore
    }

    // Sync Web Audio master gain
    if (audioCtx && masterGain) {
      try {
        masterGain.gain.setValueAtTime(muted ? 0 : 1, audioCtx.currentTime);
      } catch {
        // ignore
      }
    }

    // Immediately stop ongoing TTS if muted
    if (muted) {
      stopSpeaking();
    }

    // Sync all HTML5 audio/video elements in document
    const mediaElements = document.querySelectorAll<HTMLMediaElement>('audio, video');
    mediaElements.forEach((el) => {
      try {
        el.muted = muted;
      } catch {
        // ignore
      }
    });

    // Notify all UI components of the audio state update
    window.dispatchEvent(new CustomEvent('audiomutestatechange', { detail: { muted } }));
  }
}

/**
 * Toggle global audio mute state
 */
export function toggleGlobalAudioMute(): boolean {
  const nextMuted = !isGlobalMuted;
  setGlobalAudioMuted(nextMuted);
  return nextMuted;
}

/**
 * Celebratory success chime arpeggio (C5 - E5 - G5 - C6)
 */
export function playSuccessChime() {
  if (isGlobalMuted) return;
  const ctx = getAudioContext();
  if (!ctx || !masterGain) return;

  const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
  const startTime = ctx.currentTime;

  notes.forEach((freq, idx) => {
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(freq, startTime + idx * 0.1);

    gain.gain.setValueAtTime(0, startTime + idx * 0.1);
    gain.gain.linearRampToValueAtTime(0.25, startTime + idx * 0.1 + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.001, startTime + idx * 0.1 + 0.35);

    osc.connect(gain);
    gain.connect(masterGain!);

    osc.start(startTime + idx * 0.1);
    osc.stop(startTime + idx * 0.1 + 0.4);
  });
}

/**
 * Gentle encouraging sound for try again
 */
export function playTryAgainChime() {
  if (isGlobalMuted) return;
  const ctx = getAudioContext();
  if (!ctx || !masterGain) return;

  const startTime = ctx.currentTime;
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();

  osc.type = 'sine';
  osc.frequency.setValueAtTime(329.63, startTime); // E4
  osc.frequency.exponentialRampToValueAtTime(261.63, startTime + 0.25); // C4

  gain.gain.setValueAtTime(0.2, startTime);
  gain.gain.exponentialRampToValueAtTime(0.001, startTime + 0.3);

  osc.connect(gain);
  gain.connect(masterGain!);

  osc.start(startTime);
  osc.stop(startTime + 0.35);
}

/**
 * Subtle tactile tap click
 */
export function playTapClick() {
  if (isGlobalMuted) return;
  const ctx = getAudioContext();
  if (!ctx || !masterGain) return;

  const startTime = ctx.currentTime;
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();

  osc.type = 'sine';
  osc.frequency.setValueAtTime(600, startTime);
  osc.frequency.exponentialRampToValueAtTime(300, startTime + 0.04);

  gain.gain.setValueAtTime(0.08, startTime);
  gain.gain.exponentialRampToValueAtTime(0.001, startTime + 0.05);

  osc.connect(gain);
  gain.connect(masterGain!);

  osc.start(startTime);
  osc.stop(startTime + 0.05);
}

/**
 * Native Text-To-Speech Pronunciation with Web Speech Synthesis
 */
export function speakPhrase(
  text: string,
  speechLocale: string,
  rate = 1.0,
  onStart?: () => void,
  onEnd?: () => void,
  onError?: () => void
): boolean {
  if (isGlobalMuted) {
    if (onEnd) onEnd();
    return false;
  }

  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    return false;
  }

  try {
    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = speechLocale;
    utterance.rate = Math.max(0.6, Math.min(1.4, rate));
    utterance.pitch = 1.05; // Slightly clear and friendly tone

    // Try to pick the most natural voice for this locale
    const voices = window.speechSynthesis.getVoices();
    const langPrefix = speechLocale.slice(0, 2);
    const matchedVoice = voices.find(
      (v) => v.lang.toLowerCase() === speechLocale.toLowerCase()
    ) || voices.find(
      (v) => v.lang.toLowerCase().startsWith(langPrefix)
    );

    if (matchedVoice) {
      utterance.voice = matchedVoice;
    }

    if (onStart) utterance.onstart = onStart;
    if (onEnd) utterance.onend = onEnd;
    if (onError) utterance.onerror = onError;

    window.speechSynthesis.speak(utterance);
    return true;
  } catch (err) {
    console.warn('Speech synthesis error:', err);
    if (onError) onError();
    return false;
  }
}

export function stopSpeaking() {
  if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    try {
      window.speechSynthesis.cancel();
    } catch {
      // ignore
    }
  }
}
