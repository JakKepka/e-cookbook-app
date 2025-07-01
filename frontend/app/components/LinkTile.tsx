'use client';

import Link from 'next/link';
import Image from 'next/image';

interface LinkTileProps {
  href: string;
  title: string;
  description: string;
  imageUrl?: string;
  icon?: React.ReactNode;
  variant?: 'primary' | 'secondary';
}

export default function LinkTile({
  href,
  title,
  description,
  imageUrl,
  icon,
  variant = 'primary',
}: LinkTileProps) {
  const bgColor = variant === 'primary' ? 'bg-cookbook-beige' : 'bg-cookbook-light';
  const textColor = 'text-cookbook-navy';

  return (
    <Link 
      href={href}
      className="group block rounded-lg shadow-sm overflow-hidden transition-all duration-300 hover:shadow-md"
    >
      {imageUrl && (
        <div className="relative h-32 w-full">
          <Image
            src={imageUrl}
            alt={title}
            fill
            className="object-cover transition-transform duration-300 group-hover:scale-105"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          />
          <div className="absolute inset-0 bg-cookbook-navy/0 group-hover:bg-cookbook-navy/20 transition-colors duration-300" />
        </div>
      )}
      <div className={`p-4 ${bgColor} group-hover:bg-cookbook-orange transition-all duration-300`}>
        {icon && (
          <div className="mb-2 transform transition-transform duration-300 group-hover:scale-110 group-hover:text-white">
            {icon}
          </div>
        )}
        <h3 className={`text-lg font-serif font-semibold mb-1 ${textColor} group-hover:text-white transition-colors`}>
          {title}
        </h3>
        <p className={`text-xs ${textColor}/80 group-hover:text-white/90 transition-colors line-clamp-2`}>
          {description}
        </p>
        <div className="mt-3 flex items-center text-cookbook-orange group-hover:text-white transition-colors">
          <span className="text-xs font-medium">Dowiedz się więcej</span>
          <svg 
            className="w-4 h-4 ml-1 transform transition-transform group-hover:translate-x-1" 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke="currentColor"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
          </svg>
        </div>
      </div>
    </Link>
  );
} 