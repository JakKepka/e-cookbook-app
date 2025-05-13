import type { Metadata } from 'next';
import './globals.css';
import Navbar from '@/components/Navbar';

export const metadata: Metadata = {
  title: 'E-Cookbook - Twój Inteligentny Asystent Kulinarny',
  description: 'Odkryj nowe przepisy i otrzymuj spersonalizowane rekomendacje kulinarne',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pl" className="h-full">
      <body className="h-full bg-custom-light">
        <Navbar />
        <main className="min-h-[calc(100vh-4rem)] py-8">
          {children}
        </main>
        <footer className="bg-custom-dark text-custom-light">
          <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
            <p className="text-center text-sm">
              © {new Date().getFullYear()} E-Cookbook. Wszystkie prawa zastrzeżone.
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
} 