export interface UserPreferences {
  dietary_restrictions: string[];
  cuisine_type: string;
  cooking_time?: number;
  skill_level?: string;
}

export interface Recipe {
  id: string;
  name: string;
  description: string;
  cooking_time: number;
  difficulty: string;
  cuisine: string;
  ingredients: string[];
  instructions: string[];
} 