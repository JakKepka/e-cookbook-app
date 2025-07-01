'use client';

import { useState } from 'react';
import { Recipe } from '@/types';

interface ExpertRecommendation {
  recipes: Recipe[];
  explanation: string;
}

export default function ExpertPage() {
  const [step, setStep] = useState(1);
  const [preferences, setPreferences] = useState({
    dietary_restrictions: [] as string[],
    cuisine_type: '',
    cooking_time: '',
    skill_level: '',
    available_ingredients: [] as string[],
    servings: '',
    occasion: '',
  });
  const [recommendations, setRecommendations] = useState<ExpertRecommendation | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/expert/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences),
      });
      const data = await response.json();
      setRecommendations(data);
    } catch (error) {
      console.error('Error getting recommendations:', error);
    } finally {
      setLoading(false);
    }
  };

  const renderStep = () => {
    switch (step) {
      case 1:
        return (
          <div className="space-y-6">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Ograniczenia dietetyczne</h3>
              <div className="mt-4 space-y-4">
                {['Wegetariańskie', 'Wegańskie', 'Bezglutenowe', 'Bez laktozy'].map((restriction) => (
                  <label key={restriction} className="inline-flex items-center">
                    <input
                      type="checkbox"
                      className="rounded border-gray-300 text-emerald-600 focus:ring-emerald-500"
                      checked={preferences.dietary_restrictions.includes(restriction)}
                      onChange={(e) => {
                        const newRestrictions = e.target.checked
                          ? [...preferences.dietary_restrictions, restriction]
                          : preferences.dietary_restrictions.filter((r) => r !== restriction);
                        setPreferences({ ...preferences, dietary_restrictions: newRestrictions });
                      }}
                    />
                    <span className="ml-2">{restriction}</span>
                  </label>
                ))}
              </div>
            </div>

            <div>
              <h3 className="text-lg font-medium text-gray-900">Preferowana kuchnia</h3>
              <select
                className="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                value={preferences.cuisine_type}
                onChange={(e) => setPreferences({ ...preferences, cuisine_type: e.target.value })}
              >
                <option value="">Wybierz typ kuchni</option>
                <option value="polska">Polska</option>
                <option value="wloska">Włoska</option>
                <option value="azjatycka">Azjatycka</option>
                <option value="meksykanska">Meksykańska</option>
              </select>
            </div>
          </div>
        );

      case 2:
        return (
          <div className="space-y-6">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Dostępny czas</h3>
              <select
                className="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                value={preferences.cooking_time}
                onChange={(e) => setPreferences({ ...preferences, cooking_time: e.target.value })}
              >
                <option value="">Wybierz czas przygotowania</option>
                <option value="15">Do 15 minut</option>
                <option value="30">Do 30 minut</option>
                <option value="60">Do 1 godziny</option>
                <option value="120">Powyżej 1 godziny</option>
              </select>
            </div>

            <div>
              <h3 className="text-lg font-medium text-gray-900">Poziom umiejętności</h3>
              <select
                className="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                value={preferences.skill_level}
                onChange={(e) => setPreferences({ ...preferences, skill_level: e.target.value })}
              >
                <option value="">Wybierz poziom</option>
                <option value="poczatkujacy">Początkujący</option>
                <option value="sredniozaawansowany">Średniozaawansowany</option>
                <option value="zaawansowany">Zaawansowany</option>
              </select>
            </div>
          </div>
        );

      case 3:
        return (
          <div className="space-y-6">
            <div>
              <h3 className="text-lg font-medium text-gray-900">Dostępne składniki</h3>
              <div className="mt-2">
                <textarea
                  rows={4}
                  className="block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                  placeholder="Wpisz składniki oddzielone przecinkami..."
                  value={preferences.available_ingredients.join(', ')}
                  onChange={(e) => setPreferences({
                    ...preferences,
                    available_ingredients: e.target.value.split(',').map(i => i.trim()).filter(Boolean)
                  })}
                />
              </div>
            </div>

            <div>
              <h3 className="text-lg font-medium text-gray-900">Liczba porcji</h3>
              <select
                className="mt-2 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500"
                value={preferences.servings}
                onChange={(e) => setPreferences({ ...preferences, servings: e.target.value })}
              >
                <option value="">Wybierz liczbę porcji</option>
                <option value="1">1 osoba</option>
                <option value="2">2 osoby</option>
                <option value="4">4 osoby</option>
                <option value="6">6 osób</option>
              </select>
            </div>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-3xl font-extrabold text-gray-900 sm:text-4xl">System Ekspercki</h1>
        <p className="mt-4 text-gray-500">
          Pozwól naszemu systemowi eksperckiemu pomóc Ci w znalezieniu idealnego przepisu.
        </p>

        {!recommendations ? (
          <div className="mt-12">
            <div className="space-y-12">
              <nav aria-label="Progress">
                <ol role="list" className="flex items-center">
                  {[1, 2, 3].map((s) => (
                    <li key={s} className={`${s === 1 ? '' : 'ml-8'} relative`}>
                      <button
                        onClick={() => setStep(s)}
                        className={`${
                          s === step
                            ? 'border-emerald-600 bg-emerald-600 text-white'
                            : s < step
                            ? 'border-emerald-600 bg-white text-emerald-600'
                            : 'border-gray-300 bg-white text-gray-500'
                        } h-8 w-8 rounded-full border-2 flex items-center justify-center`}
                      >
                        {s}
                      </button>
                    </li>
                  ))}
                </ol>
              </nav>

              <div className="bg-white shadow rounded-lg p-6">
                {renderStep()}

                <div className="mt-8 flex justify-between">
                  {step > 1 && (
                    <button
                      type="button"
                      onClick={() => setStep(step - 1)}
                      className="inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                    >
                      Wstecz
                    </button>
                  )}
                  {step < 3 ? (
                    <button
                      type="button"
                      onClick={() => setStep(step + 1)}
                      className="ml-auto inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-emerald-600 hover:bg-emerald-700"
                    >
                      Dalej
                    </button>
                  ) : (
                    <button
                      type="button"
                      onClick={handleSubmit}
                      disabled={loading}
                      className="ml-auto inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-emerald-600 hover:bg-emerald-700"
                    >
                      {loading ? 'Szukam...' : 'Znajdź przepisy'}
                    </button>
                  )}
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div className="mt-12">
            <div className="bg-white shadow rounded-lg overflow-hidden">
              <div className="p-6">
                <h2 className="text-xl font-medium text-gray-900">Rekomendowane przepisy</h2>
                <p className="mt-2 text-gray-500">{recommendations.explanation}</p>

                <div className="mt-6 grid gap-6 sm:grid-cols-2">
                  {recommendations.recipes.map((recipe) => (
                    <div
                      key={recipe.id}
                      className="bg-gray-50 rounded-lg p-6 hover:bg-gray-100 transition-colors duration-200"
                    >
                      <h3 className="text-lg font-medium text-gray-900">{recipe.name}</h3>
                      <p className="mt-2 text-sm text-gray-500">{recipe.description}</p>
                      <div className="mt-4 flex items-center justify-between text-sm text-gray-500">
                        <span>Czas: {recipe.cooking_time} min</span>
                        <span>{recipe.difficulty}</span>
                      </div>
                    </div>
                  ))}
                </div>

                <button
                  type="button"
                  onClick={() => {
                    setRecommendations(null);
                    setStep(1);
                  }}
                  className="mt-8 inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                >
                  Rozpocznij ponownie
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
} 