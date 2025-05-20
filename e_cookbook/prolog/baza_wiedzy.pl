% Definicja przepisu:
% przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki)

% Przykładowe przepisy
przepis('Placki bananowe', sniadanie, bezglutenowa, europejska, 20, latwy, slodki, 300,
        [banan, jajko, platki_owsiane_bezglutenowe, cynamon, miod]).

przepis('Spaghetti Bolognese', glowne, normalna, wloska, 30, latwy, neutralny, 600,
        [makaron, mieso_mielone, cebula, czosnek, pomidory, marchew, przyprawy]).

przepis('Hummus', przystawka, weganska, bliskowschodnia, 15, latwy, neutralny, 250,
        [ciecierzyca, tahini, cytryna, czosnek, oliwa, kminek]).

% Przepisy z tabeli decyzyjnej
przepis('Gazpacho', zupa, weganska, hiszpanska, 15, latwy, ostry, 200,
        [pomidory, ogorek, papryka, czosnek, oliwa, ocet, chleb]).

przepis('Curry warzywne', glowne, weganska, indyjska, 40, sredni, ostry, 400,
        [ciecierzyca, ziemniaki, marchew, cebula, czosnek, mleko_kokosowe, przyprawy_curry]).

przepis('Sernik', deser, bezglutenowa, polska, 90, trudny, slodki, 350,
        [ser_twarogowy, jajka, maka_kukurydziana, maslo, cukier, wanilia]).

przepis('Salatka Cezar', przystawka, normalna, amerykanska, 20, latwy, neutralny, 300,
        [salata, kurczak, parmezan, grzanki, sos_cezar, anchois]).

przepis('Risotto', glowne, bezglutenowa, wloska, 35, sredni, neutralny, 450,
        [ryz_arborio, wino_biale, cebula, parmezan, maslo, bulion]).

przepis('Tacos', glowne, normalna, meksykanska, 25, sredni, ostry, 500,
        [tortilla, mieso_mielone, pomidory, cebula, papryka, ser, salsa]).

przepis('Zupa Pho', zupa, normalna, wietnamska, 50, sredni, umami, 300,
        [makaron_ryzowy, wolowina, cebula, imbir, przyprawy_azjatyckie, kolendra]).

przepis('Lasagne', glowne, normalna, wloska, 60, trudny, umami, 700,
        [makaron_lasagne, mieso_mielone, pomidory, ser, beszamel, przyprawy]).

% Reguły decyzyjne
wybierz_przepis(Nazwa) :-
    przepis(Nazwa, glowne, _, wloska, Czas, latwy, _, _, _),
    Czas =< 30.

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, weganska, _, Czas, _, _, _, _),
    Czas =< 20.

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, deser, bezglutenowa, _, _, _, _, _, _).

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, zupa, weganska, _, _, _, _, _, _).

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, przystawka, _, amerykanska, _, _, _, _, _).

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, _, indyjska, Czas, sredni, _, _, _),
    Czas =< 45.

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, _, _, Czas, trudny, _, _, _),
    Czas >= 60.

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, bezglutenowa, wloska, _, _, _, _, _).

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, glowne, _, _, _, _, neutralny, _, _).

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, _, meksykanska, Czas, _, _, _, _),
    Czas =< 30.

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, _, wietnamska, Czas, _, _, _, _),
    Czas >= 45.

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, weganska, bliskowschodnia, _, _, _, _, _).

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, deser, _, amerykanska, _, _, _, _, _).

wybierz_przepis(Nazwa) :-
    przepis(Nazwa, _, _, japonska, trudny, _, _, _, _).

% Reguły dopasowywania przepisów

% Sprawdza czy użytkownik ma wszystkie potrzebne składniki
ma_skladniki(Skladniki, DostepneSkladniki) :-
    subset(Skladniki, DostepneSkladniki).

% Sprawdza zgodność diety
zgodna_dieta(bezglutenowa, bezglutenowa).
zgodna_dieta(weganska, weganska).
zgodna_dieta(wegetarianska, wegetarianska).
zgodna_dieta(_, normalna).
zgodna_dieta(normalna, _).

% Sprawdza poziom trudności
odpowiednia_trudnosc(latwy, _).
odpowiednia_trudnosc(sredni, sredni).
odpowiednia_trudnosc(sredni, trudny).
odpowiednia_trudnosc(trudny, trudny).

% Główna reguła wyszukiwania przepisów
moze_gotowac(przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki),
             DostepneSkladniki, WymaganadiDeta, WymaganyPoziom) :-
    przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki),
    ma_skladniki(Skladniki, DostepneSkladniki),
    zgodna_dieta(Dieta, WymaganaDieta),
    odpowiednia_trudnosc(Trudnosc, WymaganyPoziom).

% Reguła dla alternatywnych składników
alternatywny_skladnik(mleko_krowkie, mleko_sojowe).
alternatywny_skladnik(mleko_krowkie, mleko_migdalowe).
alternatywny_skladnik(mleko_krowkie, mleko_kokosowe).
alternatywny_skladnik(jajko, banan).  % w niektórych przepisach
alternatywny_skladnik(maka_pszenna, maka_kukurydziana).
alternatywny_skladnik(maka_pszenna, maka_ryzowa).
alternatywny_skladnik(makaron, makaron_bezglutenowy).
alternatywny_skladnik(makaron_lasagne, makaron_lasagne_bezglutenowy).
alternatywny_skladnik(tortilla, tortilla_kukurydziana).
alternatywny_skladnik(sos_sojowy, tamari).  % bezglutenowy odpowiednik

% Sprawdzanie czy składnik może być zastąpiony
mozna_zastapic(Skladnik, Zamiennik) :-
    alternatywny_skladnik(Skladnik, Zamiennik);
    alternatywny_skladnik(Zamiennik, Skladnik). 