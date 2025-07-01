'use client';

import { useState } from 'react';
import { Recipe, UserPreferences } from '@/types';

export default function RecipesPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [filters, setFilters] = useState({
    cuisine: '',
    diet: '',
    difficulty: '',
  });
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:8000/api/v1/recipes/search?q=${encodeURIComponent(searchTerm)}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(filters),
      });
      const data = await response.json();
      setRecipes(data);
    } catch (error) {
      console.error('Search error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="max-w-2xl mx-auto lg:max-w-none">
        <h1 className="text-3xl font-extrabold text-gray-900 sm:text-4xl">Wyszukiwarka Przepisów</h1>
        <p className="mt-4 text-gray-500">Znajdź inspirację na swój następny posiłek</p>

        <div className="mt-12 grid grid-cols-1 gap-x-8 gap-y-10 lg:grid-cols-4">
          {/* Filters */}
          <div className="hidden lg:block">
            <div className="space-y-6">
              <div>
                <h3 className="text-lg font-medium text-gray-900">Kuchnia</h3>
                <select
                  className="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                  value={filters.cuisine}
                  onChange={(e) => setFilters({ ...filters, cuisine: e.target.value })}
                >
                  <option value="">Wszystkie</option>
                  <option value="polska">Polska</option>
                  <option value="wloska">Włoska</option>
                  <option value="azjatycka">Azjatycka</option>
                </select>
              </div>

              <div>
                <h3 className="text-lg font-medium text-gray-900">Dieta</h3>
                <select
                  className="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                  value={filters.diet}
                  onChange={(e) => setFilters({ ...filters, diet: e.target.value })}
                >
                  <option value="">Wszystkie</option>
                  <option value="wegetarianska">Wegetariańska</option>
                  <option value="weganska">Wegańska</option>
                  <option value="bezglutenowa">Bezglutenowa</option>
                </select>
              </div>

              <div>
                <h3 className="text-lg font-medium text-gray-900">Poziom trudności</h3>
                <select
                  className="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                  value={filters.difficulty}
                  onChange={(e) => setFilters({ ...filters, difficulty: e.target.value })}
                >
                  <option value="">Wszystkie</option>
                  <option value="latwy">Łatwy</option>
                  <option value="sredni">Średni</option>
                  <option value="trudny">Trudny</option>
                </select>
              </div>
            </div>
          </div>

          {/* Search results */}
          <div className="lg:col-span-3">
            <div className="mb-8">
              <div className="flex gap-4">
                <input
                  type="text"
                  placeholder="Szukaj przepisów..."
                  className="block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
                />
                <button
                  onClick={handleSearch}
                  disabled={loading}
                  className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500"
                >
                  {loading ? 'Szukam...' : 'Szukaj'}
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {recipes.map((recipe) => (
                <div
                  key={recipe.id}
                  className="bg-white overflow-hidden shadow rounded-lg hover:shadow-md transition-shadow duration-300"
                >
                  <div className="p-6">
                    <h3 className="text-lg font-medium text-gray-900">{recipe.name}</h3>
                    <p className="mt-2 text-sm text-gray-500">{recipe.description}</p>
                    <div className="mt-4 flex items-center justify-between text-sm text-gray-500">
                      <span>Czas: {recipe.cooking_time} min</span>
                      <span>{recipe.difficulty}</span>
                    </div>
                  </div>
                </div>
              ))}

              {recipes.length === 0 && !loading && (
                <div className="col-span-full text-center text-gray-500 py-12">
                  Nie znaleziono przepisów. Spróbuj zmienić kryteria wyszukiwania.
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
} 