import { useState } from 'react';
import { UserPreferences, Recipe } from '../types';

interface RecipeSearchProps {
  onSearch: (preferences: UserPreferences) => Promise<Recipe[]>;
}

const RecipeSearch: React.FC<RecipeSearchProps> = ({ onSearch }) => {
  const [preferences, setPreferences] = useState<UserPreferences>({
    dietary_restrictions: [],
    cuisine_type: '',
    cooking_time: undefined,
    skill_level: undefined
  });

  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const results = await onSearch(preferences);
      setRecipes(results);
    } catch (err) {
      setError('Failed to fetch recipes. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-5">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="space-y-2">
          <label htmlFor="cuisine" className="block text-sm font-medium text-gray-700">
            Cuisine Type:
          </label>
          <input
            type="text"
            id="cuisine"
            className="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            value={preferences.cuisine_type}
            onChange={(e) => setPreferences({...preferences, cuisine_type: e.target.value})}
          />
        </div>

        <div className="space-y-2">
          <label htmlFor="cooking-time" className="block text-sm font-medium text-gray-700">
            Cooking Time (minutes):
          </label>
          <input
            type="number"
            id="cooking-time"
            className="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            value={preferences.cooking_time || ''}
            onChange={(e) => setPreferences({...preferences, cooking_time: parseInt(e.target.value) || undefined})}
          />
        </div>

        <div className="space-y-2">
          <label className="block text-sm font-medium text-gray-700">
            Dietary Restrictions:
          </label>
          <select
            multiple
            className="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            value={preferences.dietary_restrictions}
            onChange={(e) => {
              const values = Array.from(e.target.selectedOptions, option => option.value);
              setPreferences({...preferences, dietary_restrictions: values});
            }}
          >
            <option value="vegetarian">Vegetarian</option>
            <option value="vegan">Vegan</option>
            <option value="gluten-free">Gluten Free</option>
            <option value="dairy-free">Dairy Free</option>
          </select>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50"
        >
          {loading ? 'Searching...' : 'Search Recipes'}
        </button>
      </form>

      {error && <div className="mt-4 text-red-600">{error}</div>}

      <div className="mt-8 space-y-4">
        {recipes.map((recipe) => (
          <div key={recipe.id} className="bg-white shadow rounded-lg p-6 border border-gray-200">
            <h3 className="text-lg font-medium text-gray-900">{recipe.name}</h3>
            <p className="mt-2 text-gray-500">{recipe.description}</p>
            <div className="mt-4 flex gap-4 text-sm text-gray-500">
              <span>Cooking time: {recipe.cooking_time} minutes</span>
              <span>•</span>
              <span>Difficulty: {recipe.difficulty}</span>
              <span>•</span>
              <span>Cuisine: {recipe.cuisine}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecipeSearch;