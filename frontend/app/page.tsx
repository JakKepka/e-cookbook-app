'use client';

import { useState } from 'react';
import RecipeSearch from '@/components/RecipeSearch';
import ExpertSystem from '@/components/ExpertSystem';
import Layout from '@/components/Layout';
import { Recipe, UserPreferences } from '@/types';

export default function Home() {
  const [activeTab, setActiveTab] = useState('search');

  const handleSearch = async (preferences: UserPreferences): Promise<Recipe[]> => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/recipes/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences),
      });
      if (!response.ok) throw new Error('Search failed');
      return response.json();
    } catch (error) {
      console.error('Search error:', error);
      return [];
    }
  };

  return (
    <Layout>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="sm:flex sm:items-center">
          <div className="sm:flex-auto">
            <h1 className="text-3xl font-semibold text-gray-900">E-Cookbook</h1>
            <p className="mt-2 text-sm text-gray-700">
              Twój inteligentny asystent kulinarny
            </p>
          </div>
        </div>

        <div className="mt-8">
          <div className="sm:hidden">
            <select
              className="block w-full rounded-md border-gray-300"
              value={activeTab}
              onChange={(e) => setActiveTab(e.target.value)}
            >
              <option value="search">Wyszukiwarka Przepisów</option>
              <option value="expert">System Ekspercki</option>
            </select>
          </div>

          <div className="hidden sm:block">
            <nav className="flex space-x-4" aria-label="Tabs">
              {['search', 'expert'].map((tab) => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`${
                    activeTab === tab
                      ? 'bg-gray-100 text-gray-700'
                      : 'text-gray-500 hover:text-gray-700'
                  } px-3 py-2 font-medium text-sm rounded-md`}
                >
                  {tab === 'search' ? 'Wyszukiwarka Przepisów' : 'System Ekspercki'}
                </button>
              ))}
            </nav>
          </div>

          <div className="mt-8">
            {activeTab === 'search' ? (
              <RecipeSearch onSearch={handleSearch} />
            ) : (
              <ExpertSystem />
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
} 