:- module(recipe_optimizer,
    [
        optimize_recipe/4,
        find_essential_ingredients/2,
        minimize_shopping/3,
        optimize_cooking_time/3,
        adapt_recipe_for_diet/4,
        reduce_food_waste/3
    ]).

:- use_module(fuzzy_logic).
:- use_module(baza_wiedzy).

% Recipe Optimizer - handles recipe optimization and ingredient substitution

% Fuzzy similarity values for ingredient properties
podobienstwo_skladnikow(X, X, 1.0).  % Ten sam składnik
podobienstwo_skladnikow(mleko_krowkie, mleko_sojowe, 0.8).
podobienstwo_skladnikow(mleko_krowkie, mleko_migdalowe, 0.8).
podobienstwo_skladnikow(mleko_krowkie, mleko_kokosowe, 0.7).
podobienstwo_skladnikow(jajko, banan, 0.6).
podobienstwo_skladnikow(maka_pszenna, maka_kukurydziana, 0.9).
podobienstwo_skladnikow(maka_pszenna, maka_ryzowa, 0.85).
podobienstwo_skladnikow(makaron, makaron_bezglutenowy, 0.95).
podobienstwo_skladnikow(makaron_lasagne, makaron_lasagne_bezglutenowy, 0.95).
podobienstwo_skladnikow(tortilla, tortilla_kukurydziana, 0.9).
podobienstwo_skladnikow(sos_sojowy, tamari, 0.95).

% Symetryczna relacja podobieństwa
podobne_skladniki(X, Y, Podobienstwo) :-
    (podobienstwo_skladnikow(X, Y, Podobienstwo);
     podobienstwo_skladnikow(Y, X, Podobienstwo)).

% Znajdź zamiennik dla składnika
znajdz_zamiennik(Skladnik, DostepneSkladniki, Zamiennik, Podobienstwo) :-
    member(Zamiennik, DostepneSkladniki),
    podobne_skladniki(Skladnik, Zamiennik, Podobienstwo),
    Podobienstwo > 0.5.

% Optymalizuj listę składników
optymalizuj_skladniki([], _, [], []).
optymalizuj_skladniki([H|T], DostepneSkladniki, [H|OptSkladniki], Zamienniki) :-
    member(H, DostepneSkladniki),
    optymalizuj_skladniki(T, DostepneSkladniki, OptSkladniki, Zamienniki).
optymalizuj_skladniki([H|T], DostepneSkladniki, [Zamiennik|OptSkladniki], [(H,Zamiennik,Podobienstwo)|Zamienniki]) :-
    \+ member(H, DostepneSkladniki),
    znajdz_zamiennik(H, DostepneSkladniki, Zamiennik, Podobienstwo),
    optymalizuj_skladniki(T, DostepneSkladniki, OptSkladniki, Zamienniki).

% Preferencje smakowe
pasuje_do_preferencji(slodki, Sweetness, _) :- Sweetness > 7.
pasuje_do_preferencji(ostry, _, Spiciness) :- Spiciness > 7.
pasuje_do_preferencji(_, _, _).

% Główna reguła znajdowania i optymalizacji przepisów
znajdz_i_optymalizuj_przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, 
                            OptymalneSkladniki, Zamienniki, DostepneSkladniki, Sweetness, Spiciness) :-
    przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki),
    pasuje_do_preferencji(Smak, Sweetness, Spiciness),
    optymalizuj_skladniki(Skladniki, DostepneSkladniki, OptymalneSkladniki, Zamienniki),
    Zamienniki \= [].  % Musi istnieć przynajmniej jeden możliwy zamiennik

% Struktura dla zoptymalizowanego przepisu
% optimize_recipe(+Recipe, +Preferences, +Available, -OptimizedRecipe)
optimize_recipe(Recipe, Preferences, Available, OptimizedRecipe) :-
    % Znajdź podstawowe składniki
    find_essential_ingredients(Recipe, Essential),
    % Zoptymalizuj zakupy
    minimize_shopping(Recipe, Available, ShoppingList),
    % Dostosuj do diety
    member(diet(Diet), Preferences),
    adapt_recipe_for_diet(Recipe, Diet, Essential, AdaptedRecipe),
    % Zoptymalizuj czas
    member(max_time(MaxTime), Preferences),
    optimize_cooking_time(AdaptedRecipe, MaxTime, TimedRecipe),
    % Zredukuj marnowanie żywności
    reduce_food_waste(TimedRecipe, Available, OptimizedRecipe).

% Znajdowanie podstawowych składników
find_essential_ingredients(Recipe, Essential) :-
    przepis(Recipe, _, _, _, _, _, _, _, Ingredients),
    findall(Ing, (
        member(Ing, Ingredients),
        \+ can_be_substituted(Ing)
    ), Essential).

% Sprawdzanie czy składnik może być zastąpiony
can_be_substituted(Ingredient) :-
    substitute_ingredients(Ingredient, 0.7, [_|_]).

% Minimalizacja zakupów
minimize_shopping(Recipe, Available, ShoppingList) :-
    przepis(Recipe, _, _, _, _, _, _, _, Ingredients),
    findall(Ing, (
        member(Ing, Ingredients),
        \+ member(Ing, Available),
        \+ (
            substitute_ingredients(Ing, 0.7, Substitutes),
            member(Sub, Substitutes),
            member(Sub, Available)
        )
    ), ShoppingList).

% Optymalizacja czasu gotowania
optimize_cooking_time(Recipe, MaxTime, OptimizedRecipe) :-
    przepis(Recipe, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki),
    (Czas > MaxTime ->
        % Znajdź szybsze alternatywy dla czasochłonnych kroków
        optimize_ingredients_for_time(Skladniki, OptimizedIngredients),
        OptimizedRecipe = przepis(Recipe, Typ, Dieta, Kuchnia, MaxTime, Trudnosc, Smak, Kalorie, OptimizedIngredients)
    ;
        OptimizedRecipe = przepis(Recipe, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki)
    ).

% Optymalizacja składników pod kątem czasu
optimize_ingredients_for_time(Ingredients, Optimized) :-
    findall(OptIng, (
        member(Ing, Ingredients),
        (requires_long_preparation(Ing) ->
            find_faster_alternative(Ing, OptIng)
        ;
            OptIng = Ing
        )
    ), Optimized).

% Sprawdzanie czy składnik wymaga długiego przygotowania
requires_long_preparation(Ingredient) :-
    member(Ingredient, [
        'fasola_sucha',
        'grzyby_suszone',
        'mieso_surowe',
        'ziemniaki_surowe'
    ]).

% Znajdowanie szybszej alternatywy
find_faster_alternative(Ingredient, Alternative) :-
    fast_alternative(Ingredient, Alternative).

% Definicje szybkich alternatyw
fast_alternative('fasola_sucha', 'fasola_konserwowa').
fast_alternative('grzyby_suszone', 'grzyby_swieże').
fast_alternative('mieso_surowe', 'mieso_wstepnie_obrobione').
fast_alternative('ziemniaki_surowe', 'ziemniaki_blanszowane').

% Dostosowanie przepisu do diety
adapt_recipe_for_diet(Recipe, Diet, Essential, AdaptedRecipe) :-
    przepis(Recipe, Typ, _, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki),
    adapt_ingredients_for_diet(Skladniki, Diet, Essential, AdaptedIngredients),
    AdaptedRecipe = przepis(Recipe, Typ, Diet, Kuchnia, Czas, Trudnosc, Smak, Kalorie, AdaptedIngredients).

% Dostosowanie składników do diety
adapt_ingredients_for_diet(Ingredients, Diet, Essential, Adapted) :-
    findall(AdaptedIng, (
        member(Ing, Ingredients),
        (member(Ing, Essential) ->
            % Jeśli składnik jest podstawowy, sprawdź czy pasuje do diety
            (compatible_with_diet(Ing, Diet) ->
                AdaptedIng = Ing
            ;
                find_diet_alternative(Ing, Diet, AdaptedIng)
            )
        ;
            % Dla nie-podstawowych składników znajdź zamienniki zgodne z dietą
            (compatible_with_diet(Ing, Diet) ->
                AdaptedIng = Ing
            ;
                find_diet_alternative(Ing, Diet, AdaptedIng)
            )
        )
    ), Adapted).

% Sprawdzanie kompatybilności z dietą
compatible_with_diet(Ingredient, Diet) :-
    \+ (
        (Diet = bezglutenowa, ingredient_property(Ingredient, glutenowa, _));
        (Diet = weganska, ingredient_property(Ingredient, zwierzęcy, _));
        (Diet = bez_laktozy, ingredient_property(Ingredient, nabiał, _))
    ).

% Znajdowanie alternatywy zgodnej z dietą
find_diet_alternative(Ingredient, Diet, Alternative) :-
    substitute_ingredients(Ingredient, 0.7, Substitutes),
    member(Alternative, Substitutes),
    compatible_with_diet(Alternative, Diet).

% Redukcja marnowania żywności
reduce_food_waste(Recipe, Available, OptimizedRecipe) :-
    przepis(Recipe, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki),
    % Znajdź składniki, które mogą się zmarnować
    findall(Ing-Quantity, (
        member(Ing, Available),
        will_expire_soon(Ing, Quantity)
    ), ExpiringIngredients),
    % Dostosuj przepis, aby wykorzystać składniki przed przetermionowaniem
    incorporate_expiring_ingredients(Skladniki, ExpiringIngredients, OptimizedIngredients),
    OptimizedRecipe = przepis(Recipe, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, OptimizedIngredients).

% Sprawdzanie czy składnik wkrótce się przeterminuje (przykładowa implementacja)
will_expire_soon(Ingredient, Quantity) :-
    % W rzeczywistej implementacji należałoby połączyć to z bazą danych
    % zawierającą daty ważności produktów
    member(Ingredient-Quantity, [
        mleko-1,
        jogurt-2,
        ser-1,
        warzywa-3
    ]).

% Włączanie składników z krótką datą ważności do przepisu
incorporate_expiring_ingredients(Ingredients, Expiring, Optimized) :-
    findall(OptIng, (
        member(Ing, Ingredients),
        (member(Exp-_, Expiring), can_substitute(Exp, Ing) ->
            OptIng = Exp
        ;
            OptIng = Ing
        )
    ), Optimized).

% Sprawdzanie czy jeden składnik może zastąpić drugi
can_substitute(Substitute, Original) :-
    ingredient_similarity(Substitute, Original, Similarity),
    Similarity >= 0.7. 