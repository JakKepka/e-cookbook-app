'use client';

import Link from 'next/link';
import { useState } from 'react';

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className="bg-cookbook-navy text-cookbook-light">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          {/* Logo and main nav */}
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <Link href="/" className="font-serif text-2xl font-bold">
                E-Cookbook
              </Link>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <Link
                href="/recipes"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium hover:text-cookbook-orange"
              >
                Przepisy
              </Link>
              <Link
                href="/categories"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium hover:text-cookbook-orange"
              >
                Kategorie
              </Link>
              <Link
                href="/about"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium hover:text-cookbook-orange"
              >
                O nas
              </Link>
            </div>
          </div>

          {/* Auth buttons */}
          <div className="hidden sm:ml-6 sm:flex sm:items-center sm:space-x-4">
            <Link
              href="/login"
              className="px-4 py-2 text-sm font-medium bg-cookbook-orange text-white rounded-md hover:bg-cookbook-red transition-colors"
            >
              Zaloguj się
            </Link>
            <Link
              href="/register"
              className="px-4 py-2 text-sm font-medium bg-cookbook-beige text-cookbook-navy rounded-md hover:bg-cookbook-light transition-colors"
            >
              Zarejestruj się
            </Link>
          </div>

          {/* Mobile menu button */}
          <div className="flex items-center sm:hidden">
            <button
              type="button"
              className="inline-flex items-center justify-center p-2 rounded-md text-cookbook-light hover:text-cookbook-orange"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
            >
              <span className="sr-only">Otwórz menu</span>
              {!isMenuOpen ? (
                <svg className="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              ) : (
                <svg className="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              )}
            </button>
          </div>
        </div>

        {/* Mobile menu */}
        <div className={`${isMenuOpen ? 'block' : 'hidden'} sm:hidden`}>
          <div className="pt-2 pb-3 space-y-1">
            <Link
              href="/recipes"
              className="block px-3 py-2 text-base font-medium hover:text-cookbook-orange"
            >
              Przepisy
            </Link>
            <Link
              href="/categories"
              className="block px-3 py-2 text-base font-medium hover:text-cookbook-orange"
            >
              Kategorie
            </Link>
            <Link
              href="/about"
              className="block px-3 py-2 text-base font-medium hover:text-cookbook-orange"
            >
              O nas
            </Link>
          </div>
          <div className="pt-4 pb-3 border-t border-cookbook-light/20">
            <div className="space-y-2">
              <Link
                href="/login"
                className="block px-3 py-2 text-base font-medium hover:text-cookbook-orange"
              >
                Zaloguj się
              </Link>
              <Link
                href="/register"
                className="block px-3 py-2 text-base font-medium hover:text-cookbook-orange"
              >
                Zarejestruj się
              </Link>
            </div>
          </div>
        </div>
      </nav>
    </header>
  );
} 