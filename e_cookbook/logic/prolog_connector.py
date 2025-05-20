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
        Returns a list of matching recipes
        """
        # Convert ingredients string to list
        ingredients_list = [i.strip().lower() for i in ingredients.split(',') if i.strip()]
        
        # Build Prolog query
        query = (f"moze_gotowac(przepis(Nazwa, {difficulty}, {diet_type}, "
                f"Okazja, _, _, _, Skladniki), {ingredients_list})")
        
        try:
            # Execute query and get results
            results = list(self.prolog.query(query))
            return [result["Nazwa"] for result in results]
        except Exception as e:
            print(f"Error executing Prolog query: {e}")
            return [] 