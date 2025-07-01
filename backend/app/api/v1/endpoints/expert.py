from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.core.expert_rules import create_expert_system, add_recipe_facts, get_recommendations

router = APIRouter()

class UserPreferences(BaseModel):
    dietary_restrictions: List[str] = []
    cuisine_type: Optional[str] = None
    cooking_time: Optional[int] = None
    skill_level: Optional[str] = None

class Recipe(BaseModel):
    id: str
    name: str
    description: str
    ingredients: List[str]
    instructions: List[str]
    cooking_time: int
    difficulty: str
    cuisine: str
    dietary_info: List[str]

@router.post("/recommend", response_model=List[Recipe])
async def get_recipe_recommendations(preferences: UserPreferences):
    try:
        # Create and initialize expert system
        expert_system = create_expert_system()
        
        # TODO: Load recipes from database
        sample_recipes = [
            {
                "id": "1",
                "name": "Spaghetti Bolognese",
                "description": "Classic Italian pasta dish",
                "ingredients": ["pasta", "beef", "tomato sauce"],
                "instructions": ["Cook pasta", "Make sauce", "Combine"],
                "cooking_time": 30,
                "difficulty": "easy",
                "cuisine": "Włoska",
                "dietary_info": []
            },
            {
                "id": "2",
                "name": "Vegan Buddha Bowl",
                "description": "Healthy vegan bowl",
                "ingredients": ["quinoa", "chickpeas", "vegetables"],
                "instructions": ["Cook quinoa", "Roast veggies", "Assemble"],
                "cooking_time": 25,
                "difficulty": "easy",
                "cuisine": "Wegetariańska",
                "dietary_info": ["Wegetariańskie", "Wegańskie"]
            }
        ]
        
        # Add recipe facts to expert system
        add_recipe_facts(expert_system, sample_recipes)
        
        # Get recommendations
        recommended_recipe_names = get_recommendations(expert_system, preferences.dict())
        
        # Filter and return recommended recipes
        recommended_recipes = [
            recipe for recipe in sample_recipes
            if recipe["name"] in recommended_recipe_names
        ]
        
        return recommended_recipes
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error getting recommendations: {str(e)}"
        ) 