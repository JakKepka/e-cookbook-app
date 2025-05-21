:- module(fuzzy_logic,
    [
        ingredient_similarity/3,
        substitute_ingredients/3,
        ingredient_property/3,
        combine_ingredients/3
    ]).

% Właściwości składników (składnik, właściwość, wartość 0-1)
ingredient_property(mleko, kremowe, 0.8).
ingredient_property(mleko, słodkie, 0.3).
ingredient_property(mleko, neutralne, 0.7).
ingredient_property(mleko_kokosowe, kremowe, 0.9).
ingredient_property(mleko_kokosowe, słodkie, 0.4).
ingredient_property(mleko_kokosowe, egzotyczne, 0.8).
ingredient_property(smietana, kremowe, 1.0).
ingredient_property(smietana, tłuste, 0.9).
ingredient_property(jogurt, kremowe, 0.7).
ingredient_property(jogurt, kwasne, 0.6).
ingredient_property(tofu, neutralne, 0.9).
ingredient_property(tofu, białkowe, 0.8).
ingredient_property(ser, słone, 0.7).
ingredient_property(ser, tłuste, 0.8).
ingredient_property(ser, białkowe, 0.9).

% Definicje właściwości dla różnych typów mąki
ingredient_property(maka_pszenna, glutenowa, 1.0).
ingredient_property(maka_pszenna, neutralna, 0.8).
ingredient_property(maka_kukurydziana, bezglutenowa, 1.0).
ingredient_property(maka_kukurydziana, słodkawa, 0.3).
ingredient_property(maka_ryzowa, bezglutenowa, 1.0).
ingredient_property(maka_ryzowa, neutralna, 0.9).
ingredient_property(maka_migdalowa, bezglutenowa, 1.0).
ingredient_property(maka_migdalowa, słodka, 0.4).
ingredient_property(maka_migdalowa, tłusta, 0.6).

% Właściwości dla słodzików i zamienników cukru
ingredient_property(cukier, słodkie, 1.0).
ingredient_property(cukier, wysoki_ig, 1.0).
ingredient_property(miod, słodkie, 0.9).
ingredient_property(miod, naturalne, 1.0).
ingredient_property(syrop_klonowy, słodkie, 0.8).
ingredient_property(syrop_klonowy, naturalne, 0.9).
ingredient_property(erytrytol, słodkie, 0.7).
ingredient_property(erytrytol, niski_ig, 1.0).

% Obliczanie podobieństwa między składnikami
ingredient_similarity(Ing1, Ing2, Similarity) :-
    findall(Property, (ingredient_property(Ing1, Property, _); ingredient_property(Ing2, Property, _)), Properties),
    sort(Properties, UniqueProperties),
    calculate_properties_similarity(Ing1, Ing2, UniqueProperties, Similarities),
    sum_list(Similarities, Sum),
    length(Similarities, Length),
    (Length > 0 -> Similarity is Sum / Length; Similarity is 0).

% Obliczanie podobieństwa dla listy właściwości
calculate_properties_similarity(_, _, [], []).
calculate_properties_similarity(Ing1, Ing2, [Prop|Props], [Sim|Sims]) :-
    get_property_value(Ing1, Prop, Val1),
    get_property_value(Ing2, Prop, Val2),
    Sim is 1 - abs(Val1 - Val2),
    calculate_properties_similarity(Ing1, Ing2, Props, Sims).

% Pobieranie wartości właściwości (z domyślną wartością 0)
get_property_value(Ing, Prop, Value) :-
    (ingredient_property(Ing, Prop, V) -> Value = V; Value = 0).

% Znajdowanie zamienników dla składnika
substitute_ingredients(Ingredient, MinSimilarity, Substitutes) :-
    findall(
        Similarity-Substitute,
        (
            ingredient_property(Substitute, _, _),
            Substitute \= Ingredient,
            ingredient_similarity(Ingredient, Substitute, Similarity),
            Similarity >= MinSimilarity
        ),
        Pairs
    ),
    keysort(Pairs, Sorted),
    reverse(Sorted, ReverseSorted),
    pairs_values(ReverseSorted, Substitutes).

% Łączenie składników z uwzględnieniem ich właściwości
combine_ingredients(Ing1, Ing2, Properties) :-
    findall(
        Prop-Val,
        (
            (ingredient_property(Ing1, Prop, Val1); ingredient_property(Ing2, Prop, Val1)),
            (ingredient_property(Ing1, Prop, Val2); ingredient_property(Ing2, Prop, Val2)),
            Val is (Val1 + Val2) / 2
        ),
        Properties
    ).

% Pomocnicze predykaty
sum_list([], 0).
sum_list([H|T], Sum) :-
    sum_list(T, Rest),
    Sum is H + Rest.

pairs_values([], []).
pairs_values([_-V|T], [V|VT]) :-
    pairs_values(T, VT). 