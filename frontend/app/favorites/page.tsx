'use client';

import { useState, useEffect } from 'react';
import { Recipe } from '@/types';

export default function FavoritesPage() {
  const [favorites, setFavorites] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // W przyszłości można dodać pobieranie z backendu
    const savedFavorites = localStorage.getItem('favorites');
    if (savedFavorites) {
      setFavorites(JSON.parse(savedFavorites));
    }
    setLoading(false);
  }, []);

  const removeFavorite = (recipeId: string) => {
    const newFavorites = favorites.filter((recipe) => recipe.id !== recipeId);
    setFavorites(newFavorites);
    localStorage.setItem('favorites', JSON.stringify(newFavorites));
  };

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-3xl mx-auto py-12">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600 mx-auto"></div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-3xl font-extrabold text-gray-900 sm:text-4xl">Ulubione Przepisy</h1>
        <p className="mt-4 text-gray-500">
          Twoja kolekcja zapisanych przepisów.
        </p>

        {favorites.length === 0 ? (
          <div className="mt-12 text-center py-12 bg-white rounded-lg shadow">
            <svg
              className="mx-auto h-12 w-12 text-gray-400"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
              />
            </svg>
            <h3 className="mt-2 text-sm font-medium text-gray-900">Brak ulubionych przepisów</h3>
            <p className="mt-1 text-sm text-gray-500">
              Zacznij dodawać przepisy do ulubionych podczas przeglądania.
            </p>
          </div>
        ) : (
          <div className="mt-12 space-y-6">
            {favorites.map((recipe) => (
              <div
                key={recipe.id}
                className="bg-white shadow rounded-lg overflow-hidden hover:shadow-md transition-shadow duration-200"
              >
                <div className="p-6">
                  <div className="flex items-start justify-between">
                    <div>
                      <h3 className="text-lg font-medium text-gray-900">{recipe.name}</h3>
                      <p className="mt-2 text-sm text-gray-500">{recipe.description}</p>
                    </div>
                    <button
                      onClick={() => removeFavorite(recipe.id)}
                      className="text-gray-400 hover:text-gray-500"
                    >
                      <span className="sr-only">Usuń z ulubionych</span>
                      <svg className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path
                          fillRule="evenodd"
                          d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                          clipRule="evenodd"
                        />
                      </svg>
                    </button>
                  </div>
                  <div className="mt-4 flex items-center text-sm text-gray-500">
                    <span>Czas przygotowania: {recipe.cooking_time} min</span>
                    <span className="mx-2">•</span>
                    <span>Poziom trudności: {recipe.difficulty}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
} 