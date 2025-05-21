from pyswip import Prolog

class PrologConnector:
    def __init__(self):
        self.prolog = Prolog()
        self.load_knowledge_base()

    def load_knowledge_base(self):
        """Load the Prolog knowledge base files"""
        try:
            self.prolog.consult("e_cookbook/prolog/baza_wiedzy.pl")
            self.prolog.consult("e_cookbook/prolog/recipe_optimizer.pl")
        except Exception as e:
            print(f"Error loading knowledge base: {e}")

    def find_recipes(self, ingredients, diet_type, sweetness, spiciness, occasion, difficulty):
        """
        Query Prolog for recipes matching the given criteria
        Returns a list of matching recipes with details
        """
        # Convert ingredients string to list and normalize
        ingredients_list = [i.strip().lower().replace(' ', '_') for i in ingredients.split(',') if i.strip()]
        
        # Convert parameters to Prolog format
        diet = diet_type.lower().replace('wszystkie', 'normalna')
        difficulty = difficulty.lower()
        occasion = occasion.lower()
        
        # Build Prolog query for optimized recipes
        query = (f"znajdz_i_optymalizuj_przepis(Nazwa, {occasion}, {diet}, Kuchnia, Czas, "
                f"{difficulty}, Smak, Kalorie, Skladniki, ZamiennikiLista, {ingredients_list}, "
                f"{sweetness}, {spiciness})")
        
        try:
            results = []
            for result in self.prolog.query(query):
                recipe = {
                    'nazwa': result['Nazwa'],
                    'kuchnia': result['Kuchnia'],
                    'czas': result['Czas'],
                    'kalorie': result['Kalorie'],
                    'smak': result['Smak'],
                    'skladniki': result['Skladniki'],
                    'zamienniki': self._parse_zamienniki(result['ZamiennikiLista'])
                }
                results.append(recipe)
            return results
        except Exception as e:
            print(f"Error executing Prolog query: {e}")
            return []

    def _parse_zamienniki(self, zamienniki_lista):
        """Convert Prolog substitutes list to Python dictionary"""
        zamienniki = {}
        if zamienniki_lista:
            for zamiennik in zamienniki_lista:
                oryginalny = str(zamiennik[0])
                zamiennik_skladnik = str(zamiennik[1])
                podobienstwo = float(zamiennik[2])
                zamienniki[oryginalny] = {
                    'proporcje': zamiennik_skladnik,
                    'podobieństwo': podobienstwo
                }
        return zamienniki 