from experta import *
from typing import List, Dict, Any

class RecipeFact(Fact):
    """Recipe fact with all necessary attributes."""
    pass

class UserPreferenceFact(Fact):
    """User preferences and restrictions."""
    pass

class IngredientFact(Fact):
    """Available ingredients."""
    pass

class RecipeExpertSystem(KnowledgeEngine):
    @DefFacts()
    def initial_facts(self):
        """Define initial facts at startup."""
        yield Fact(system_status="ready")

    @Rule(
        Fact(system_status="ready"),
        UserPreferenceFact(
            dietary_restrictions=MATCH.restrictions,
            cuisine_type=MATCH.cuisine,
            cooking_time=MATCH.time
        )
    )
    def match_basic_preferences(self, restrictions, cuisine, time):
        """Match recipes based on basic user preferences."""
        self.declare(Fact(matching_preferences=True))
        self.declare(Fact(current_restrictions=restrictions))
        self.declare(Fact(desired_cuisine=cuisine))
        self.declare(Fact(max_cooking_time=time))

    @Rule(
        Fact(matching_preferences=True),
        Fact(current_restrictions=MATCH.restrictions),
        RecipeFact(
            name=MATCH.name,
            ingredients=MATCH.ingredients,
            dietary_info=MATCH.dietary_info
        )
    )
    def check_dietary_restrictions(self, restrictions, name, ingredients, dietary_info):
        """Check if recipe matches dietary restrictions."""
        if all(restriction in dietary_info for restriction in restrictions):
            self.declare(Fact(suitable_recipe=name))

    @Rule(
        Fact(suitable_recipe=MATCH.recipe_name),
        Fact(desired_cuisine=MATCH.cuisine),
        RecipeFact(name=MATCH.recipe_name, cuisine=MATCH.cuisine)
    )
    def match_cuisine_preference(self, recipe_name):
        """Match recipes based on cuisine preference."""
        self.declare(Fact(cuisine_matched_recipe=recipe_name))

    @Rule(
        Fact(cuisine_matched_recipe=MATCH.recipe_name),
        Fact(max_cooking_time=MATCH.max_time),
        RecipeFact(name=MATCH.recipe_name, cooking_time=MATCH.time)
    )
    def check_cooking_time(self, recipe_name, max_time, time):
        """Check if recipe matches cooking time preference."""
        if time <= max_time:
            self.declare(Fact(final_matched_recipe=recipe_name))

def create_expert_system() -> RecipeExpertSystem:
    """Create and initialize the expert system."""
    expert_system = RecipeExpertSystem()
    expert_system.reset()
    return expert_system

def add_recipe_facts(expert_system: RecipeExpertSystem, recipes: List[Dict[str, Any]]):
    """Add recipe facts to the expert system."""
    for recipe in recipes:
        expert_system.declare(RecipeFact(**recipe))

def get_recommendations(
    expert_system: RecipeExpertSystem,
    preferences: Dict[str, Any]
) -> List[str]:
    """Get recipe recommendations based on user preferences."""
    expert_system.declare(UserPreferenceFact(**preferences))
    expert_system.run()
    
    # Collect all matched recipes
    matched_recipes = []
    for fact in expert_system.facts:
        if isinstance(fact, Fact) and 'final_matched_recipe' in fact:
            matched_recipes.append(fact['final_matched_recipe'])
    
    return matched_recipes 