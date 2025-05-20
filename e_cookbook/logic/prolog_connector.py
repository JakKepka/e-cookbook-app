from pyswip import Prolog

class PrologConnector:
    def __init__(self):
        self.prolog = Prolog()
        self.load_knowledge_base()

    def load_knowledge_base(self):
        """Load the Prolog knowledge base"""
        try:
            self.prolog.consult("e_cookbook/prolog/baza_wiedzy.pl")
        except Exception as e:
            print(f"Error loading knowledge base: {e}")

    def find_recipes(self, ingredients, diet_type, sweetness, spiciness, occasion, difficulty):
        """
        Query Prolog for recipes matching the given criteria
        Returns a list of matching recipes with details
        """
        # Convert ingredients string to list
        ingredients_list = [i.strip().lower() for i in ingredients.split(',') if i.strip()]
        
        # Convert parameters to Prolog format
        diet = diet_type.lower().replace('wszystkie', 'normalna')
        difficulty = difficulty.lower()
        occasion = occasion.lower()
        
        # Build Prolog query for recipes matching criteria
        query = (f"przepis(Nazwa, {occasion}, {diet}, Kuchnia, Czas, {difficulty}, Smak, Kalorie, Skladniki), "
                f"ma_skladniki(Skladniki, {ingredients_list})")
        
        try:
            # Execute query and get results
            results = []
            for result in self.prolog.query(query):
                recipe = {
                    'nazwa': result['Nazwa'],
                    'kuchnia': result['Kuchnia'],
                    'czas': result['Czas'],
                    'kalorie': result['Kalorie'],
                    'smak': result['Smak']
                }
                results.append(recipe)
            
            # Apply additional filtering based on taste preferences
            if sweetness > 7:
                results = [r for r in results if r['smak'] == 'slodki']
            elif spiciness > 7:
                results = [r for r in results if r['smak'] == 'ostry']
            
            return results
        except Exception as e:
            print(f"Error executing Prolog query: {e}")
            return []

    def get_alternative_ingredients(self, ingredient):
        """Find alternative ingredients for a given ingredient"""
        query = f"mozna_zastapic({ingredient}, Zamiennik)"
        try:
            return [result["Zamiennik"] for result in self.prolog.query(query)]
        except Exception as e:
            print(f"Error finding alternative ingredients: {e}")
            return [] 