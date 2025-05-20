from dataclasses import dataclass
from typing import List, Dict, Set, Optional
from .fuzzy_logic import FuzzyReasoning

@dataclass
class OptimizedRecipe:
    nazwa: str
    skladniki_podstawowe: List[str]
    skladniki_opcjonalne: List[str]
    zamienniki: Dict[str, List[str]]
    czas_przygotowania: int
    koszt_bazowy: float
    wymagany_sprzet: List[str]
    kalorie: int
    poziom_trudnosci: str

class RecipeOptimizer:
    def __init__(self, fuzzy_reasoning: FuzzyReasoning):
        self.fuzzy_reasoning = fuzzy_reasoning
        self.essential_ingredients = {
            'ciasto': {'maka', 'sol'},
            'sos': {'sol', 'przyprawy'},
            'zupa': {'woda', 'sol', 'przyprawy'},
            'miesne': {'mieso', 'sol', 'przyprawy'},
            'salatka': {'sol', 'oliwa'},
            'deser': {'cukier'}
        }
        
        self.equipment_substitutes = {
            'piekarnik': ['multicooker', 'garnek_z_pokrywka'],
            'mikrofala': ['garnek', 'piekarnik'],
            'blender': ['mikser', 'rozdrabniacz'],
            'mixer': ['blender', 'trzepaczka'],
            'parowar': ['garnek_z_sitkiem', 'multicooker']
        }

        self.cooking_methods = {
            'piekarnik': {'czas': 1.5, 'energia': 2.0},
            'mikrofala': {'czas': 0.5, 'energia': 1.0},
            'multicooker': {'czas': 1.2, 'energia': 1.5},
            'garnek': {'czas': 1.0, 'energia': 1.0},
            'patelnia': {'czas': 0.8, 'energia': 1.2}
        }

    def optimize_recipe(self, recipe: dict, available_ingredients: List[str], 
                       available_equipment: List[str], max_time: Optional[int] = None,
                       max_calories: Optional[int] = None, allergies: List[str] = None) -> OptimizedRecipe:
        """
        Optymalizuje przepis na podstawie dostępnych składników i sprzętu
        """
        # Identyfikacja składników podstawowych i opcjonalnych
        basic_ingredients = self._identify_essential_ingredients(recipe['skladniki'], recipe['nazwa'])
        optional_ingredients = [ing for ing in recipe['skladniki'] if ing not in basic_ingredients]

        # Znajdź zamienniki dla brakujących składników podstawowych
        substitutes = {}
        for ingredient in basic_ingredients:
            if ingredient not in available_ingredients:
                if allergies and ingredient in allergies:
                    # Znajdź zamienniki uwzględniające alergie
                    substitute = self._find_allergy_safe_substitute(ingredient, available_ingredients, allergies)
                else:
                    # Znajdź standardowe zamienniki
                    substitute = self.fuzzy_reasoning.find_substitute(ingredient, available_ingredients)
                if substitute:
                    substitutes[ingredient] = substitute

        # Optymalizacja czasu przygotowania
        optimized_time = self._optimize_cooking_time(recipe['czas'], available_equipment)
        
        # Oblicz przybliżony koszt bazowy (przykładowe wartości)
        base_cost = len(basic_ingredients) * 5.0 + len(optional_ingredients) * 3.0
        
        # Znajdź wymagany sprzęt i jego zamienniki
        required_equipment = self._identify_required_equipment(recipe['nazwa'], recipe['trudnosc'])
        
        return OptimizedRecipe(
            nazwa=recipe['nazwa'],
            skladniki_podstawowe=list(basic_ingredients),
            skladniki_opcjonalne=optional_ingredients,
            zamienniki=substitutes,
            czas_przygotowania=optimized_time,
            koszt_bazowy=base_cost,
            wymagany_sprzet=required_equipment,
            kalorie=recipe['kalorie'],
            poziom_trudnosci=recipe['trudnosc']
        )

    def _identify_essential_ingredients(self, ingredients: List[str], recipe_type: str) -> Set[str]:
        """
        Identyfikuje kluczowe składniki dla danego typu przepisu
        """
        essential = set()
        
        # Dodaj podstawowe składniki dla danego typu przepisu
        for category, base_ingredients in self.essential_ingredients.items():
            if category.lower() in recipe_type.lower():
                essential.update(base_ingredients)
        
        # Dodaj składniki, które są kluczowe dla charakteru dania
        for ingredient in ingredients:
            if any(key in ingredient.lower() for key in ['mieso', 'ryba', 'maka', 'ryz', 'ziemniaki']):
                essential.add(ingredient)
        
        return essential

    def _find_allergy_safe_substitute(self, ingredient: str, available_ingredients: List[str], 
                                    allergies: List[str]) -> Optional[dict]:
        """
        Znajduje bezpieczne zamienniki dla osób z alergiami
        """
        # Najpierw znajdź wszystkie możliwe zamienniki
        substitute = self.fuzzy_reasoning.find_substitute(ingredient, available_ingredients)
        if not substitute:
            return None

        # Sprawdź czy zamiennik jest bezpieczny
        if isinstance(substitute['składniki'], tuple):
            if any(allergen in allergies for allergen in substitute['składniki']):
                return None
        elif substitute['składniki'] in allergies:
            return None

        return substitute

    def _optimize_cooking_time(self, base_time: int, available_equipment: List[str]) -> int:
        """
        Optymalizuje czas przygotowania na podstawie dostępnego sprzętu
        """
        min_time_factor = float('inf')
        for equipment in available_equipment:
            if equipment in self.cooking_methods:
                min_time_factor = min(min_time_factor, self.cooking_methods[equipment]['czas'])
        
        if min_time_factor == float('inf'):
            return base_time
        
        return int(base_time * min_time_factor)

    def _identify_required_equipment(self, recipe_name: str, difficulty: str) -> List[str]:
        """
        Identyfikuje wymagany sprzęt na podstawie nazwy przepisu i poziomu trudności
        """
        required = []
        
        # Podstawowy sprzęt
        if 'zupa' in recipe_name.lower():
            required.extend(['garnek', 'chochla'])
        elif 'ciasto' in recipe_name.lower() or 'pieczeń' in recipe_name.lower():
            required.append('piekarnik')
        elif 'sałatka' in recipe_name.lower():
            required.extend(['miska', 'deska_do_krojenia'])
            
        # Dodatkowy sprzęt w zależności od poziomu trudności
        if difficulty == 'trudny':
            required.extend(['mikser', 'waga_kuchenna'])
        
        return required 