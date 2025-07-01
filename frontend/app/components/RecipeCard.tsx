'use client';

import Image from 'next/image';
import Link from 'next/link';

interface RecipeCardProps {
  id: string;
  title: string;
  description: string;
  imageUrl: string;
  prepTime: string;
  difficulty: 'easy' | 'medium' | 'hard';
  category: string;
}

export default function RecipeCard({
  id,
  title,
  description,
  imageUrl,
  prepTime,
  difficulty,
  category,
}: RecipeCardProps) {
  const difficultyColor = {
    easy: 'bg-green-100 text-green-800',
    medium: 'bg-cookbook-beige text-cookbook-navy',
    hard: 'bg-cookbook-red/20 text-cookbook-red',
  }[difficulty];

  return (
    <div className="bg-cookbook-light rounded-lg shadow-md overflow-hidden transition-all duration-300 hover:scale-[1.02] group">
      <div className="relative h-48">
        <Image
          src={imageUrl}
          alt={title}
          fill
          className="object-cover"
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        />
        <div className="absolute top-4 right-4">
          <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${difficultyColor}`}>
            {difficulty === 'easy' ? 'Łatwy' : difficulty === 'medium' ? 'Średni' : 'Trudny'}
          </span>
        </div>
      </div>

      <div className="p-6 bg-cookbook-beige group-hover:bg-cookbook-orange transition-colors">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm text-cookbook-navy font-medium group-hover:text-white transition-colors">
            {category}
          </span>
          <span className="text-sm text-cookbook-navy/70 group-hover:text-white/90 transition-colors">
            {prepTime}
          </span>
        </div>

        <Link href={`/recipes/${id}`}>
          <h3 className="text-xl font-serif font-semibold mb-2 text-cookbook-navy group-hover:text-white transition-colors">
            {title}
          </h3>
        </Link>

        <p className="text-sm text-cookbook-navy/80 group-hover:text-white/90 transition-colors line-clamp-2">
          {description}
        </p>

        <div className="mt-4 flex justify-between items-center">
          <Link
            href={`/recipes/${id}`}
            className="text-cookbook-red group-hover:text-white transition-colors text-sm font-medium"
          >
            Zobacz przepis →
          </Link>
          <button
            className="p-2 text-cookbook-navy group-hover:text-white transition-colors"
            aria-label="Dodaj do ulubionych"
          >
            <svg
              className="h-5 w-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
} 