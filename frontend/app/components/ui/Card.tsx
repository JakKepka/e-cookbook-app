'use client';

import Link from 'next/link';
import Image from 'next/image';
import { ReactNode } from 'react';

interface CardProps {
  href: string;
  title: string;
  description: string;
  imageUrl?: string;
  icon?: ReactNode;
  variant?: 'primary' | 'secondary';
  className?: string;
}

export default function Card({
  href,
  title,
  description,
  imageUrl,
  icon,
  variant = 'primary',
  className = '',
}: CardProps) {
  return (
    <Link 
      href={href}
      className={`
        block rounded-lg shadow-sm overflow-hidden 
        transition-all duration-200 ease-in-out
        hover:shadow-md hover:-translate-y-0.5
        ${className}
      `}
    >
      {imageUrl && (
        <div className="relative h-32 w-full">
          <Image
            src={imageUrl}
            alt={title}
            fill
            className="object-cover"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          />
          <div className="absolute inset-0 bg-cookbook-navy/0 group-hover:bg-cookbook-navy/10 transition-colors duration-200" />
        </div>
      )}
      <div className={`
        p-4 ${variant === 'primary' ? 'bg-cookbook-beige' : 'bg-cookbook-light'}
        group-hover:bg-cookbook-orange transition-colors duration-200
      `}>
        {icon && (
          <div className="mb-3 text-cookbook-navy group-hover:text-white transition-colors duration-200">
            {icon}
          </div>
        )}
        <h3 className="text-base font-serif font-semibold mb-1.5 text-cookbook-navy group-hover:text-white transition-colors duration-200">
          {title}
        </h3>
        <p className="text-sm text-cookbook-navy/80 group-hover:text-white/90 transition-colors duration-200 line-clamp-2">
          {description}
        </p>
        <div className="mt-3 flex items-center text-cookbook-orange group-hover:text-white transition-colors duration-200">
          <span className="text-xs font-medium">Zobacz więcej</span>
          <svg 
            className="w-4 h-4 ml-1 transform transition-transform group-hover:translate-x-0.5" 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke="currentColor"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
          </svg>
        </div>
      </div>
    </Link>
  );
} 