class FuzzyIngredient:
    def __init__(self, name, creaminess=0, sourness=0, sweetness=0, thickness=0, neutrality=0):
        self.name = name
        self.properties = {
            'kremowość': creaminess,
            'kwasowość': sourness,
            'słodkość': sweetness,
            'gęstość': thickness,
            'neutralność': neutrality
        }

class FuzzyReasoning:
    def __init__(self):
        # Definicja bazowych składników z ich właściwościami rozmytymi
        self.ingredients = {
            'śmietana': FuzzyIngredient('śmietana', creaminess=0.9, thickness=0.8, neutrality=0.7),
            'jogurt': FuzzyIngredient('jogurt', creaminess=0.6, sourness=0.7, thickness=0.6),
            'mleko': FuzzyIngredient('mleko', creaminess=0.3, neutrality=0.9, thickness=0.3),
            'mleko_kokosowe': FuzzyIngredient('mleko_kokosowe', creaminess=0.7, sweetness=0.4, thickness=0.6),
            'mleko_migdałowe': FuzzyIngredient('mleko_migdałowe', creaminess=0.5, sweetness=0.3, thickness=0.4),
            'mleko_sojowe': FuzzyIngredient('mleko_sojowe', creaminess=0.4, neutrality=0.8, thickness=0.4),
            'masło': FuzzyIngredient('masło', creaminess=0.9, thickness=0.9, neutrality=0.6),
            'olej': FuzzyIngredient('olej', creaminess=0.3, neutrality=0.9, thickness=0.4),
            'oliwa': FuzzyIngredient('oliwa', creaminess=0.4, neutrality=0.7, thickness=0.4),
            'tahini': FuzzyIngredient('tahini', creaminess=0.8, thickness=0.9, neutrality=0.5),
        }

        # Progi akceptowalności dla zamienników
        self.acceptance_threshold = 0.7

    def find_substitute(self, target_ingredient, available_ingredients):
        """
        Znajduje najlepszy zamiennik lub kombinację zamienników dla danego składnika
        """
        if target_ingredient not in self.ingredients:
            return None

        target = self.ingredients[target_ingredient]
        best_substitute = None
        best_score = 0
        best_mix = None

        # Sprawdź pojedyncze składniki
        for ing_name in available_ingredients:
            if ing_name in self.ingredients:
                ing = self.ingredients[ing_name]
                score = self._calculate_similarity(target, ing)
                if score > best_score and score >= self.acceptance_threshold:
                    best_score = score
                    best_substitute = ing_name
                    best_mix = None

        # Sprawdź kombinacje dwóch składników
        for i, ing1_name in enumerate(available_ingredients):
            for ing2_name in available_ingredients[i+1:]:
                if ing1_name in self.ingredients and ing2_name in self.ingredients:
                    ing1 = self.ingredients[ing1_name]
                    ing2 = self.ingredients[ing2_name]
                    
                    # Sprawdź różne proporcje
                    for ratio in [0.7, 0.6, 0.5]:
                        mixed_properties = self._mix_ingredients(ing1, ing2, ratio)
                        score = self._calculate_similarity(target, mixed_properties)
                        if score > best_score and score >= self.acceptance_threshold:
                            best_score = score
                            best_substitute = (ing1_name, ing2_name)
                            best_mix = ratio

        if best_mix is not None:
            return {
                'składniki': best_substitute,
                'proporcje': f"{int(best_mix*100)}% {best_substitute[0]} + {int((1-best_mix)*100)}% {best_substitute[1]}",
                'podobieństwo': round(best_score, 2)
            }
        elif best_substitute:
            return {
                'składniki': best_substitute,
                'proporcje': "100%",
                'podobieństwo': round(best_score, 2)
            }
        return None

    def _calculate_similarity(self, target, substitute):
        """
        Oblicza podobieństwo między składnikami na podstawie ich właściwości
        """
        total_weight = 0
        weighted_sum = 0
        
        for prop, value in target.properties.items():
            if value > 0:  # Tylko istotne właściwości
                weight = value
                target_val = value
                sub_val = substitute.properties[prop] if isinstance(substitute, FuzzyIngredient) else substitute[prop]
                similarity = 1 - abs(target_val - sub_val)
                weighted_sum += similarity * weight
                total_weight += weight

        return weighted_sum / total_weight if total_weight > 0 else 0

    def _mix_ingredients(self, ing1, ing2, ratio):
        """
        Miesza dwa składniki w zadanych proporcjach
        """
        mixed = {}
        for prop in ing1.properties:
            mixed[prop] = ing1.properties[prop] * ratio + ing2.properties[prop] * (1 - ratio)
        return mixed 