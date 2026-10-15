import React, { useEffect } from 'react';
import { X, Youtube, ShieldCheck } from 'lucide-react';
import { playTapClick } from '../utils/audio';

interface VideoModalProps {
  isOpen: boolean;
  onClose: () => void;
  videoId: string;
  title: string;
}

export const VideoModal: React.FC<VideoModalProps> = ({
  isOpen,
  onClose,
  videoId,
  title,
}) => {
  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="video-modal-title"
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 backdrop-blur-md bg-slate-950/60 animate-fade-in"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-3xl bg-slate-900 rounded-2xl sm:rounded-3xl overflow-hidden shadow-2xl border border-slate-800 text-left"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header Bar */}
        <div className="flex items-center justify-between px-4 sm:px-5 py-3 sm:py-4 border-b border-slate-800 bg-slate-900/90">
          <div className="flex items-center gap-2 min-w-0 pr-2">
            <div className="w-8 h-8 rounded-lg bg-red-600/20 text-red-500 flex items-center justify-center shrink-0">
              <Youtube className="w-4 h-4" />
            </div>
            <div className="min-w-0">
              <h3 id="video-modal-title" className="text-xs sm:text-sm font-bold text-slate-100 truncate">
                {title}
              </h3>
              <div className="flex items-center gap-1.5 text-[10px] sm:text-[11px] text-slate-400">
                <ShieldCheck className="w-3 h-3 text-emerald-400 shrink-0" />
                <span className="truncate">Safe Classroom Stream</span>
              </div>
            </div>
          </div>

          <button
            onClick={() => {
              playTapClick();
              onClose();
            }}
            className="p-2 rounded-full hover:bg-slate-800 text-slate-400 hover:text-slate-200 transition-colors min-w-[44px] min-h-[44px] flex items-center justify-center shrink-0 cursor-pointer"
            aria-label="Close video lesson"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* 16:9 Video Frame */}
        <div className="relative w-full aspect-video bg-black">
          <iframe
            src={`https://www.youtube-nocookie.com/embed/${videoId}?playsinline=1&modestbranding=1&rel=0&autoplay=1`}
            title={title}
            className="w-full h-full border-0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>

        {/* Footer Note */}
        <div className="px-4 sm:px-5 py-3 bg-slate-950 text-xs text-slate-400 flex flex-col xs:flex-row items-start xs:items-center justify-between gap-2 pb-safe">
          <span className="text-[11px] sm:text-xs">Tip: Listen to native rhythms and mouth shapes.</span>
          <button
            onClick={onClose}
            className="text-xs font-semibold text-amber-400 hover:underline min-h-[44px] flex items-center cursor-pointer"
          >
            Return to Mission
          </button>
        </div>
      </div>
    </div>
  );
};
