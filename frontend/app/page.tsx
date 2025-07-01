'use client';

import Card from './components/ui/Card';

export default function Home() {
  const categories = [
    {
      title: 'Dania główne',
      description: 'Odkryj różnorodne przepisy na pyszne dania główne - od tradycyjnych po nowoczesne interpretacje.',
      href: '/categories/main-dishes',
      imageUrl: 'https://placehold.co/400x200/F2F3AE/020122/png?text=Dania+Główne',
    },
    {
      title: 'Zupy',
      description: 'Rozgrzewające zupy na każdą porę roku - klasyczne receptury i nowe kompozycje smakowe.',
      href: '/categories/soups',
      imageUrl: 'https://placehold.co/400x200/EDD382/020122/png?text=Zupy',
    },
    {
      title: 'Sałatki',
      description: 'Lekkie i pełne witamin sałatki - idealne jako dodatek lub samodzielne danie.',
      href: '/categories/salads',
      imageUrl: 'https://placehold.co/400x200/FC9E4F/020122/png?text=Sałatki',
    },
  ];

  const quickAccess = [
    {
      title: 'Przepisy sezonowe',
      description: 'Sprawdź co warto gotować w tym sezonie. Wykorzystaj najlepsze składniki dostępne teraz.',
      href: '/seasonal',
      icon: (
        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
        </svg>
      ),
    },
    {
      title: 'Popularne przepisy',
      description: 'Zobacz co najczęściej gotują inni. Znajdź inspirację wśród sprawdzonych przepisów.',
      href: '/popular',
      icon: (
        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
        </svg>
      ),
    },
    {
      title: 'Dodaj przepis',
      description: 'Podziel się swoim ulubionym przepisem. Dołącz do naszej kulinarnej społeczności.',
      href: '/add-recipe',
      icon: (
        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 4v16m8-8H4" />
        </svg>
      ),
    },
  ];

  return (
    <main className="min-h-screen bg-cookbook-light/5">
      {/* Hero section */}
      <section className="bg-cookbook-navy text-white py-12 mb-12">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-3xl sm:text-4xl font-serif font-bold mb-4">
            Odkryj radość gotowania
          </h1>
          <p className="text-cookbook-light/90 text-sm sm:text-base max-w-2xl mx-auto">
            Znajdź inspirację wśród tysięcy przepisów, dziel się swoimi kulinarnymi odkryciami
            i dołącz do społeczności pasjonatów gotowania.
          </p>
        </div>
      </section>

      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Quick access section */}
        <section className="mb-12">
          <h2 className="text-xl font-serif font-semibold text-cookbook-navy mb-6">
            Szybki dostęp
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {quickAccess.map((item, index) => (
              <Card
                key={index}
                {...item}
                variant={index % 2 === 0 ? 'primary' : 'secondary'}
              />
            ))}
          </div>
        </section>

        {/* Categories section */}
        <section className="mb-12">
          <h2 className="text-xl font-serif font-semibold text-cookbook-navy mb-6">
            Kategorie przepisów
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {categories.map((category, index) => (
              <Card
                key={index}
                {...category}
                variant={index % 2 === 0 ? 'primary' : 'secondary'}
              />
            ))}
          </div>
        </section>
      </div>
    </main>
  );
} 