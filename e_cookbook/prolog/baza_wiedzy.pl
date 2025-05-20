% Definicja przepisu:
% przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki)

% Przykładowe przepisy
przepis('Placki bananowe', sniadanie, bezglutenowa, europejska, 20, latwy, slodki, 300,
        [banan, jajko, platki_owsiane_bezglutenowe, cynamon, miod]).

przepis('Spaghetti Bolognese', obiad, normalna, wloska, 45, sredni, umami, 600,
        [makaron, mieso_mielone, cebula, czosnek, pomidory, marchew, przyprawy]).

przepis('Hummus', przekaska, weganska, bliskowschodnia, 15, latwy, neutralny, 250,
        [ciecierzyca, tahini, cytryna, czosnek, oliwa, kminek]).

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
alternatywny_skladnik(jajko, banan).  % w niektórych przepisach
alternatywny_skladnik(maka_pszenna, maka_kukurydziana).
alternatywny_skladnik(maka_pszenna, maka_ryzowa).

% Sprawdzanie czy składnik może być zastąpiony
mozna_zastapic(Skladnik, Zamiennik) :-
    alternatywny_skladnik(Skladnik, Zamiennik);
    alternatywny_skladnik(Zamiennik, Skladnik). 