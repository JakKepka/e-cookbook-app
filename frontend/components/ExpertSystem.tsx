import React, { useState } from 'react';
import axios from 'axios';

interface Preference {
  dietaryRestrictions: string[];
  cuisineType: string;
  cookingTime: string;
  skillLevel: string;
}

const ExpertSystem: React.FC = () => {
  const [preferences, setPreferences] = useState<Preference>({
    dietaryRestrictions: [],
    cuisineType: '',
    cookingTime: '',
    skillLevel: '',
  });

  const [recommendations, setRecommendations] = useState<any[]>([]);

  const dietaryOptions = [
    'Wegetariańskie',
    'Wegańskie',
    'Bezglutenowe',
    'Bez laktozy',
  ];

  const cuisineTypes = [
    'Polska',
    'Włoska',
    'Azjatycka',
    'Meksykańska',
    'Śródziemnomorska',
  ];

  const handleDietaryChange = (restriction: string) => {
    setPreferences(prev => ({
      ...prev,
      dietaryRestrictions: prev.dietaryRestrictions.includes(restriction)
        ? prev.dietaryRestrictions.filter(r => r !== restriction)
        : [...prev.dietaryRestrictions, restriction],
    }));
  };

  const getRecommendations = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/v1/expert/recommend', preferences);
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error getting recommendations:', error);
    }
  };

  return (
    <div className="space-y-8">
      <div>
        <h3 className="text-lg font-medium leading-6 text-gray-900">
          Preferencje Żywieniowe
        </h3>
        <div className="mt-4 space-y-4">
          <div>
            <label className="text-sm font-medium text-gray-700">
              Ograniczenia dietetyczne
            </label>
            <div className="mt-2 grid grid-cols-2 gap-2">
              {dietaryOptions.map((option) => (
                <label
                  key={option}
                  className="inline-flex items-center"
                >
                  <input
                    type="checkbox"
                    className="rounded border-gray-300 text-indigo-600"
                    checked={preferences.dietaryRestrictions.includes(option)}
                    onChange={() => handleDietaryChange(option)}
                  />
                  <span className="ml-2">{option}</span>
                </label>
              ))}
            </div>
          </div>

          <div>
            <label className="text-sm font-medium text-gray-700">
              Typ kuchni
            </label>
            <select
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
              value={preferences.cuisineType}
              onChange={(e) => setPreferences(prev => ({ ...prev, cuisineType: e.target.value }))}
            >
              <option value="">Wybierz typ kuchni</option>
              {cuisineTypes.map((type) => (
                <option key={type} value={type}>
                  {type}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      <button
        onClick={getRecommendations}
        className="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
      >
        Znajdź Przepisy
      </button>

      {recommendations.length > 0 && (
        <div className="mt-8">
          <h3 className="text-lg font-medium leading-6 text-gray-900">
            Rekomendowane Przepisy
          </h3>
          <div className="mt-4 grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
            {recommendations.map((recipe, index) => (
              <div
                key={index}
                className="bg-white overflow-hidden shadow rounded-lg"
              >
                <div className="px-4 py-5 sm:p-6">
                  <h4 className="text-lg font-medium text-gray-900">
                    {recipe.name}
                  </h4>
                  <p className="mt-1 text-sm text-gray-500">
                    {recipe.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ExpertSystem; 