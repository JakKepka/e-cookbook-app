import './globals.css';
import { Inter, Playfair_Display } from 'next/font/google';
import Header from './components/Header';
import Footer from './components/Footer';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

const playfair = Playfair_Display({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-playfair',
});

export const metadata = {
  title: 'E-Cookbook - Twoja książka kucharska online',
  description: 'Odkryj, zapisuj i dziel się przepisami kulinarnymi. Znajdź inspirację na kolejny posiłek!',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pl" className={`${inter.variable} ${playfair.variable}`}>
      <body className="min-h-screen flex flex-col bg-cookbook-light/5">
        <Header />
        <main className="flex-grow">{children}</main>
        <Footer />
      </body>
    </html>
  );
} 