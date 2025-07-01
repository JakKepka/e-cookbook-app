'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const Navbar = () => {
  const pathname = usePathname();
  const isActive = (path: string) => pathname === path;

  return (
    <nav className="bg-custom-dark">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        {/* Logo section */}
        <div className="flex justify-center mb-6">
          <Link href="/" className="flex-shrink-0 flex items-center">
            <span className="text-3xl font-serif font-bold text-custom-light hover:text-custom-yellow transition-colors duration-300">
              E-Cookbook
            </span>
          </Link>
        </div>

        {/* Desktop navigation */}
        <div className="hidden sm:block">
          <div className="grid grid-cols-3 gap-4">
            <Link
              href="/recipes"
              className={`${
                isActive('/recipes')
                  ? 'bg-custom-orange text-custom-dark'
                  : 'bg-custom-yellow text-custom-dark hover:bg-custom-red hover:text-custom-light'
              } rounded-lg p-4 text-center font-medium transition-all duration-300 transform hover:scale-105 shadow-md`}
            >
              <div className="text-lg">Wyszukiwarka Przepisów</div>
            </Link>

            <Link
              href="/expert"
              className={`${
                isActive('/expert')
                  ? 'bg-custom-orange text-custom-dark'
                  : 'bg-custom-yellow text-custom-dark hover:bg-custom-red hover:text-custom-light'
              } rounded-lg p-4 text-center font-medium transition-all duration-300 transform hover:scale-105 shadow-md`}
            >
              <div className="text-lg">System Ekspercki</div>
            </Link>

            <Link
              href="/favorites"
              className={`${
                isActive('/favorites')
                  ? 'bg-custom-orange text-custom-dark'
                  : 'bg-custom-yellow text-custom-dark hover:bg-custom-red hover:text-custom-light'
              } rounded-lg p-4 text-center font-medium transition-all duration-300 transform hover:scale-105 shadow-md`}
            >
              <div className="text-lg">Ulubione Przepisy</div>
            </Link>
          </div>
        </div>

        {/* Mobile navigation */}
        <div className="sm:hidden space-y-2">
          <Link
            href="/recipes"
            className={`${
              isActive('/recipes')
                ? 'bg-custom-orange text-custom-dark'
                : 'bg-custom-yellow text-custom-dark hover:bg-custom-red hover:text-custom-light'
            } block rounded-lg p-3 text-center font-medium transition-colors duration-300`}
          >
            Wyszukiwarka Przepisów
          </Link>

          <Link
            href="/expert"
            className={`${
              isActive('/expert')
                ? 'bg-custom-orange text-custom-dark'
                : 'bg-custom-yellow text-custom-dark hover:bg-custom-red hover:text-custom-light'
            } block rounded-lg p-3 text-center font-medium transition-colors duration-300`}
          >
            System Ekspercki
          </Link>

          <Link
            href="/favorites"
            className={`${
              isActive('/favorites')
                ? 'bg-custom-orange text-custom-dark'
                : 'bg-custom-yellow text-custom-dark hover:bg-custom-red hover:text-custom-light'
            } block rounded-lg p-3 text-center font-medium transition-colors duration-300`}
          >
            Ulubione Przepisy
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 