from pyswip import Prolog
from .fuzzy_logic import FuzzyReasoning

class PrologConnector:
    def __init__(self):
        self.prolog = Prolog()
        self.fuzzy_reasoning = FuzzyReasoning()
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
        # Convert ingredients string to list and normalize
        ingredients_list = [i.strip().lower().replace(' ', '_') for i in ingredients.split(',') if i.strip()]
        print(f"\nDebug - Znormalizowane składniki: {ingredients_list}")
        
        # Convert parameters to Prolog format
        diet = diet_type.lower().replace('wszystkie', 'normalna')
        difficulty = difficulty.lower()
        occasion = occasion.lower()
        
        print(f"Debug - Parametry wyszukiwania:")
        print(f"- Dieta: {diet}")
        print(f"- Trudność: {difficulty}")
        print(f"- Typ: {occasion}")
        
        # Build Prolog query for recipes matching criteria
        query = (f"przepis(Nazwa, {occasion}, {diet}, Kuchnia, Czas, {difficulty}, "
                f"Smak, Kalorie, Skladniki), ma_wszystkie_skladniki(Skladniki, {ingredients_list})")
        
        print(f"\nDebug - Zapytanie Prolog: {query}")
        
        try:
            # Execute query and get results
            results = []
            for result in self.prolog.query(query):
                recipe = {
                    'nazwa': result['Nazwa'],
                    'kuchnia': result['Kuchnia'],
                    'czas': result['Czas'],
                    'kalorie': result['Kalorie'],
                    'smak': result['Smak'],
                    'skladniki': result['Skladniki']
                }
                results.append(recipe)
                print(f"\nDebug - Znaleziono przepis: {recipe['nazwa']}")
                print(f"Debug - Wymagane składniki: {recipe['skladniki']}")

            # Jeśli nie znaleziono przepisów, spróbuj znaleźć podobne z użyciem wnioskowania rozmytego
            if not results:
                print("\nDebug - Próba znalezienia przepisów z zamiennikami...")
                fuzzy_results = self._find_recipes_with_substitutes(ingredients_list, occasion, diet, difficulty)
                results.extend(fuzzy_results)
            
            # Apply additional filtering based on taste preferences
            if sweetness > 7:
                results = [r for r in results if r['smak'] == 'slodki']
            elif spiciness > 7:
                results = [r for r in results if r['smak'] == 'ostry']
            
            return results
        except Exception as e:
            print(f"\nDebug - Błąd podczas wykonywania zapytania: {e}")
            return []

    def _find_recipes_with_substitutes(self, available_ingredients, occasion, diet, difficulty):
        """
        Znajduje przepisy, które mogą być wykonane z użyciem zamienników
        """
        results = []
        query = f"przepis(Nazwa, {occasion}, {diet}, Kuchnia, Czas, {difficulty}, Smak, Kalorie, Skladniki)"
        
        try:
            for result in self.prolog.query(query):
                required_ingredients = result['Skladniki']
                substitutes = {}
                can_make = True

                # Sprawdź każdy wymagany składnik
                for ingredient in required_ingredients:
                    if ingredient not in available_ingredients:
                        # Spróbuj znaleźć zamiennik
                        substitute = self.fuzzy_reasoning.find_substitute(ingredient, available_ingredients)
                        if substitute:
                            substitutes[ingredient] = substitute
                        else:
                            can_make = False
                            break

                if can_make:
                    recipe = {
                        'nazwa': result['Nazwa'],
                        'kuchnia': result['Kuchnia'],
                        'czas': result['Czas'],
                        'kalorie': result['Kalorie'],
                        'smak': result['Smak'],
                        'skladniki': result['Skladniki'],
                        'zamienniki': substitutes
                    }
                    results.append(recipe)
                    print(f"\nDebug - Znaleziono przepis z zamiennikami: {recipe['nazwa']}")
                    for ing, sub in substitutes.items():
                        print(f"Debug - Zamiennik dla {ing}: {sub['proporcje']} (podobieństwo: {sub['podobieństwo']})")

            return results
        except Exception as e:
            print(f"\nDebug - Błąd podczas szukania przepisów z zamiennikami: {e}")
            return []

    def get_alternative_ingredients(self, ingredient):
        """Find alternative ingredients for a given ingredient"""
        # Normalize ingredient name
        ingredient = ingredient.lower().replace(' ', '_')
        
        # Najpierw sprawdź zamienniki z bazy Prologowej
        prolog_alternatives = []
        query = f"mozna_zastapic({ingredient}, Zamiennik)"
        try:
            prolog_alternatives = [result["Zamiennik"] for result in self.prolog.query(query)]
        except Exception as e:
            print(f"Error finding Prolog alternative ingredients: {e}")

        # Następnie sprawdź zamienniki z systemu rozmytego
        fuzzy_substitute = self.fuzzy_reasoning.find_substitute(ingredient, 
            [ing for ing in self.fuzzy_reasoning.ingredients.keys() if ing != ingredient])
        
        # Połącz wyniki
        alternatives = []
        if prolog_alternatives:
            alternatives.extend(prolog_alternatives)
        if fuzzy_substitute:
            if isinstance(fuzzy_substitute['składniki'], tuple):
                alternatives.append(f"{fuzzy_substitute['proporcje']}")
            else:
                alternatives.append(fuzzy_substitute['składniki'])
        
        return alternatives 