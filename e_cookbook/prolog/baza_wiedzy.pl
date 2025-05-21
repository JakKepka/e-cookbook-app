% Definicja przepisu:
% przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki)

:- discontiguous alternatywny_skladnik/2.
:- discontiguous przepis/9.

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

% Dodatkowe przepisy z różnych kuchni świata
przepis('Pad Thai', glowne, bezglutenowa, tajska, 30, sredni, umami, 450,
        [makaron_ryzowy, tofu, orzeszki_ziemne, kiełki, sos_rybny, jajko, limonka]).

przepis('Pierogi ruskie', glowne, wegetarianska, polska, 90, trudny, neutralny, 400,
        [maka_pszenna, ziemniaki, ser_twarogowy, cebula, jajko, maslo]).

przepis('Ramen', zupa, normalna, japonska, 60, trudny, umami, 550,
        [makaron_ramen, bulion_drobiowy, jajko, wieprzowina, szczypiorek, glony_nori, imbir]).

przepis('Falafel', glowne, weganska, bliskowschodnia, 45, sredni, neutralny, 350,
        [ciecierzyca, pietruszka, kolendra, czosnek, cebula, kminek, kolendra_mielona]).

przepis('Quiche Lorraine', glowne, normalna, francuska, 75, sredni, umami, 500,
        [maka_pszenna, maslo, jajka, boczek, ser_gruyere, smietana, cebula]).

przepis('Tiramisu', deser, normalna, wloska, 40, sredni, slodki, 400,
        [mascarpone, jajka, biszkopty, kawa, kakao, cukier]).

% Nowe kategorie diet
dieta(bezglutenowa).
dieta(weganska).
dieta(wegetarianska).
dieta(normalna).
dieta(bez_laktozy).
dieta(paleo).
dieta(keto).
dieta(low_carb).

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
             DostepneSkladniki, WymaganaDieta, WymaganyPoziom) :-
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

% Reguły sprawdzania składników
ma_wszystkie_skladniki([], _).
ma_wszystkie_skladniki([H|T], DostepneSkladniki) :-
    member(H, DostepneSkladniki),
    ma_wszystkie_skladniki(T, DostepneSkladniki).

% Główna reguła wyszukiwania przepisów
znajdz_przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki, DostepneSkladniki) :-
    przepis(Nazwa, Typ, Dieta, Kuchnia, Czas, Trudnosc, Smak, Kalorie, Skladniki),
    ma_wszystkie_skladniki(Skladniki, DostepneSkladniki).

% Rozszerzone reguły dla alternatywnych składników z właściwościami
alternatywny_skladnik(skladnik(maka_pszenna, glutenowa), skladnik(maka_ryzowa, bezglutenowa)).
alternatywny_skladnik(skladnik(maka_pszenna, glutenowa), skladnik(maka_kokosowa, bezglutenowa)).
alternatywny_skladnik(skladnik(cukier, wysoki_ig), skladnik(erytrytol, niski_ig)).
alternatywny_skladnik(skladnik(maslo, nabiał), skladnik(olej_kokosowy, roślinny)).
alternatywny_skladnik(skladnik(jajko, zwierzęcy), skladnik(siemie_lniane_namoczone, roślinny)).
alternatywny_skladnik(skladnik(smietana, nabiał), skladnik(mleko_kokosowe, roślinny)).
alternatywny_skladnik(skladnik(ser, nabiał), skladnik(drozdze_odzywcze, roślinny)).

% Reguły dla sprzętu kuchennego
wymaga_sprzetu(przepis(_, _, _, _, _, _, _, _, _), podstawowy).
wymaga_sprzetu('Ramen', garnek_duzy).
wymaga_sprzetu('Tiramisu', mikser).
wymaga_sprzetu('Pierogi ruskie', walek).
wymaga_sprzetu('Quiche Lorraine', forma_do_tarty).

% Reguły sezonowości składników
sezonowy(pomidory, lato).
sezonowy(truskawki, lato).
sezonowy(dynia, jesien).
sezonowy(szparagi, wiosna).
sezonowy(grzyby_lesne, jesien).

% Reguły dla minimalnego zestawu składników
skladnik_podstawowy(sol).
skladnik_podstawowy(pieprz).
skladnik_podstawowy(oliwa).
skladnik_podstawowy(czosnek).
skladnik_podstawowy(cebula).

% Reguły optymalizacji czasu
szybki_przepis(Nazwa) :-
    przepis(Nazwa, _, _, _, Czas, _, _, _, _),
    Czas =< 30.

sredni_czas_przepis(Nazwa) :-
    przepis(Nazwa, _, _, _, Czas, _, _, _, _),
    Czas > 30,
    Czas =< 60.

dlugi_przepis(Nazwa) :-
    przepis(Nazwa, _, _, _, Czas, _, _, _, _),
    Czas > 60.

% Reguły dla redukcji marnowania żywności
moze_wykorzystac_resztki(Skladnik, Przepis) :-
    przepis(Przepis, _, _, _, _, _, _, _, Skladniki),
    member(Skladnik, Skladniki).

% Reguły dla wartości odżywczych
wysoka_zawartosc_bialka(Nazwa) :-
    przepis(Nazwa, _, _, _, _, _, _, _, Skladniki),
    (member(kurczak, Skladniki);
     member(tofu, Skladniki);
     member(ciecierzyca, Skladniki);
     member(jajka, Skladniki)).

niska_zawartosc_weglowodanow(Nazwa) :-
    przepis(Nazwa, _, _, _, _, _, _, _, Skladniki),
    \+ (member(maka_pszenna, Skladniki);
        member(ryz, Skladniki);
        member(ziemniaki, Skladniki);
        member(makaron, Skladniki)).

% Reguła dla przepisów przyjaznych początkującym
przyjazny_poczatkujacym(Nazwa) :-
    przepis(Nazwa, _, _, _, Czas, Trudnosc, _, _, Skladniki),
    Czas =< 30,
    Trudnosc = latwy,
    length(Skladniki, Dlugosc),
    Dlugosc =< 6.

% Reguła dla przepisów ekonomicznych
ekonomiczny_przepis(Nazwa) :-
    przepis(Nazwa, _, _, _, _, _, _, _, Skladniki),
    \+ (member(owoce_morza, Skladniki);
        member(wolowina, Skladniki);
        member(ser_gruyere, Skladniki)),
    length(Skladniki, Dlugosc),
    Dlugosc =< 8.

% Główna reguła wyszukiwania z uwzględnieniem wszystkich kryteriów
znajdz_optymalny_przepis(Nazwa, Dieta, MaxCzas, Trudnosc, DostepneSkładniki, DostepnySprzet) :-
    przepis(Nazwa, _, Dieta, _, Czas, Trudnosc, _, _, Skladniki),
    Czas =< MaxCzas,
    ma_wszystkie_skladniki(Skladniki, DostepneSkładniki),
    wymaga_sprzetu(Nazwa, DostepnySprzet).

% Śniadania
przepis('Owsianka z owocami', sniadanie, wegetarianska, miedzynarodowa, 15, latwy, slodki, 300,
        [platki_owsiane, mleko, banan, jagody, miod, cynamon]).

przepis('Jajecznica na masle', sniadanie, wegetarianska, polska, 10, latwy, neutralny, 250,
        [jajka, maslo, szczypiorek, sol, pieprz]).

przepis('Szakszuka', sniadanie, wegetarianska, bliskowschodnia, 25, sredni, pikantny, 350,
        [jajka, pomidory, papryka, cebula, czosnek, kummin, papryka_wedzona]).

przepis('Smoothie bowl', sniadanie, weganska, miedzynarodowa, 10, latwy, slodki, 280,
        [banan, jagody, szpinak, mleko_migdalowe, nasiona_chia]).

przepis('Tost z awokado', sniadanie, weganska, miedzynarodowa, 10, latwy, neutralny, 320,
        [chleb, awokado, pomidor, rukola, oliwa, sol, pieprz]).

% Zupy
przepis('Krem z dyni', zupa, wegetarianska, polska, 45, sredni, neutralny, 280,
        [dynia, ziemniaki, cebula, czosnek, smietana, bulion_warzywny, przyprawy]).

przepis('Barszcz czerwony', zupa, wegetarianska, polska, 60, sredni, kwasny, 220,
        [buraki, marchew, pietruszka, seler, czosnek, zakwas_burakowy, przyprawy]).

przepis('Zupa miso', zupa, weganska, japonska, 20, latwy, umami, 150,
        [pasta_miso, tofu, glony_wakame, szczypiorek, grzyby_shitake]).

przepis('Tom Yum', zupa, normalna, tajska, 40, sredni, pikantny, 300,
        [krewetki, grzyby, trawa_cytrynowa, galangal, chili, limonka, bulion]).

przepis('Minestrone', zupa, wegetarianska, wloska, 50, sredni, neutralny, 280,
        [fasola, makaron, pomidory, marchew, seler, cukinia, bazylia]).

% Dania główne - Kuchnia polska
przepis('Schabowy', glowne, normalna, polska, 40, sredni, neutralny, 550,
        [schab, jajka, bulka_tarta, maka_pszenna, sol, pieprz, olej]).

przepis('Golonka', glowne, normalna, polska, 120, trudny, neutralny, 800,
        [golonka, czosnek, cebula, marchew, piwo, przyprawy, majeranek]).

przepis('Bigos', glowne, normalna, polska, 180, sredni, neutralny, 450,
        [kapusta_kiszona, kielbasa, boczek, grzyby_suszone, sliwki_suszone, przyprawy]).

przepis('Kopytka', glowne, wegetarianska, polska, 45, sredni, neutralny, 380,
        [ziemniaki, maka_pszenna, jajko, sol, maslo]).

% Dania główne - Kuchnia włoska
przepis('Pizza Margherita', glowne, wegetarianska, wloska, 60, sredni, neutralny, 700,
        [maka_pszenna, drozdze, pomidory, mozzarella, bazylia, oliwa]).

przepis('Carbonara', glowne, normalna, wloska, 25, sredni, umami, 650,
        [makaron_spaghetti, jajka, pecorino, guanciale, pieprz]).

przepis('Gnocchi', glowne, wegetarianska, wloska, 50, trudny, neutralny, 450,
        [ziemniaki, maka_pszenna, jajko, sol, maslo_szalwiowe]).

% Dania główne - Kuchnia azjatycka
przepis('Curry z kurczakiem', glowne, normalna, indyjska, 45, sredni, pikantny, 500,
        [kurczak, mleko_kokosowe, pasta_curry, ryz, cebula, czosnek, imbir]).

przepis('Dim sum', przystawka, normalna, chinska, 60, trudny, neutralny, 350,
        [maka_pszenna, krewetki, wieprzowina, kapusta, sos_sojowy, olej_sezamowy]).

przepis('Bibimbap', glowne, normalna, koreanska, 40, sredni, pikantny, 550,
        [ryz, wolowina, marchew, szpinak, kiełki, jajko, gochujang]).

przepis('Sushi rolls', glowne, normalna, japonska, 60, trudny, umami, 400,
        [ryz_do_sushi, nori, losos, awokado, ogorek, wasabi, sos_sojowy]).

% Dania główne - Kuchnia meksykańska
przepis('Enchiladas', glowne, normalna, meksykanska, 50, sredni, pikantny, 600,
        [tortilla, kurczak, fasola, ser, salsa, smietana, papryka]).

przepis('Guacamole', przystawka, weganska, meksykanska, 15, latwy, neutralny, 200,
        [awokado, pomidor, cebula, limonka, kolendra, chili, sol]).

przepis('Chili con carne', glowne, normalna, meksykanska, 60, sredni, pikantny, 550,
        [mieso_mielone, fasola, pomidory, papryka, cebula, czosnek, przyprawy_meksykanskie]).

% Dania główne - Kuchnia śródziemnomorska
przepis('Moussaka', glowne, normalna, grecka, 90, trudny, neutralny, 650,
        [baklazan, mieso_mielone, ziemniaki, beszamel, ser_feta, cynamon]).

przepis('Paella', glowne, normalna, hiszpanska, 60, trudny, neutralny, 600,
        [ryz, krewetki, malze, chorizo, szafran, groszek, papryka]).

przepis('Souvlaki', glowne, normalna, grecka, 40, sredni, neutralny, 450,
        [wieprzowina, oliwa, czosnek, oregano, cytryna, pita]).

% Sałatki
przepis('Sałatka grecka', salatka, wegetarianska, grecka, 15, latwy, neutralny, 300,
        [pomidor, ogorek, cebula, oliwki, ser_feta, oliwa, oregano]).

przepis('Sałatka z komosą ryżową', salatka, weganska, miedzynarodowa, 25, latwy, neutralny, 350,
        [komosa_ryzowa, ciecierzyca, pomidor, ogorek, rukola, oliwa, cytryna]).

przepis('Sałatka nicejska', salatka, normalna, francuska, 20, latwy, neutralny, 400,
        [salata, tunczyk, jajka, fasola, oliwki, anchois, sos_vinaigrette]).

% Desery
przepis('Brownie', deser, normalna, amerykanska, 45, sredni, slodki, 400,
        [czekolada, maslo, jajka, cukier, maka_pszenna, orzechy_wloskie]).

przepis('Crème brûlée', deser, wegetarianska, francuska, 60, trudny, slodki, 350,
        [smietanka, żółtka, cukier, wanilia, cukier_do_karmelizacji]).

przepis('Panna cotta', deser, wegetarianska, wloska, 20, latwy, slodki, 300,
        [smietanka, cukier, zelantyna, wanilia, owoce]).

przepis('Baklava', deser, wegetarianska, turecka, 90, trudny, slodki, 450,
        [ciasto_filo, orzechy, maslo, miod, cynamon, kardamon]).

% Przekąski
przepis('Spring rolls', przekaska, weganska, wietnamska, 40, sredni, neutralny, 250,
        [papier_ryzowy, marchew, ogorek, mango, mięta, orzeszki, sos_orzechowy]).

przepis('Bruschetta', przekaska, weganska, wloska, 20, latwy, neutralny, 200,
        [bagietka, pomidory, czosnek, bazylia, oliwa, sol, pieprz]).

przepis('Nachos', przekaska, wegetarianska, meksykanska, 25, latwy, pikantny, 500,
        [nachos, ser, fasola, pomidory, awokado, jalapeno, smietana]).

% Dania wegetariańskie
przepis('Kotlety z kalafiora', glowne, wegetarianska, miedzynarodowa, 40, sredni, neutralny, 350,
        [kalafior, jajko, bulka_tarta, czosnek, natka_pietruszki, przyprawy]).

przepis('Curry z soczewicą', glowne, weganska, indyjska, 35, sredni, pikantny, 400,
        [soczewica, pomidory, cebula, czosnek, imbir, przyprawy_curry, ryz]).

przepis('Makaron z pesto', glowne, wegetarianska, wloska, 20, latwy, neutralny, 450,
        [makaron, bazylia, orzechy_pinii, parmezan, czosnek, oliwa]).

% Dania bezglutenowe
przepis('Bowl z quinoa', glowne, bezglutenowa, miedzynarodowa, 30, latwy, neutralny, 400,
        [quinoa, ciecierzyca, batat, szpinak, awokado, pestki_dyni]).

przepis('Placki z cukinii', glowne, bezglutenowa, miedzynarodowa, 25, latwy, neutralny, 300,
        [cukinia, jajko, maka_kukurydziana, czosnek, koper, jogurt]).

przepis('Kurczak teriyaki', glowne, bezglutenowa, japonska, 35, sredni, umami, 450,
        [kurczak, sos_tamari, miod, imbir, czosnek, ryz, sezam]).

% Dania keto
przepis('Stek z awokado', glowne, keto, miedzynarodowa, 25, sredni, neutralny, 600,
        [stek_wolowy, awokado, maslo, czosnek, rozmaryn, sol, pieprz]).

przepis('Łosoś ze szpinakiem', glowne, keto, miedzynarodowa, 30, sredni, neutralny, 500,
        [losos, szpinak, smietana, czosnek, maslo, sol, pieprz]).

przepis('Jajka po benedyktyńsku', sniadanie, keto, miedzynarodowa, 25, trudny, neutralny, 450,
        [jajka, szynka_parmeńska, maslo, ocet, natka_pietruszki]).

% Dania wegańskie
przepis('Tofu scramble', sniadanie, weganska, miedzynarodowa, 20, latwy, neutralny, 300,
        [tofu, kurkuma, cebula, papryka, szpinak, przyprawy]).

przepis('Buddha bowl', glowne, weganska, miedzynarodowa, 30, latwy, neutralny, 450,
        [quinoa, ciecierzyca, batat, jarmuż, awokado, tahini]).

przepis('Makaron z sosem pomidorowym', glowne, weganska, wloska, 25, latwy, neutralny, 400,
        [makaron, pomidory, czosnek, cebula, bazylia, oliwa]).

% Dania na specjalne okazje
przepis('Wellington', glowne, normalna, brytyjska, 120, trudny, umami, 800,
        [polędwica_wolowa, ciasto_francuskie, grzyby, szpinak, musztarda, jajko]).

przepis('Kaczka w pomarańczach', glowne, normalna, francuska, 90, trudny, slodko_kwasny, 700,
        [kaczka, pomarancze, miod, tymianek, czosnek, wino_czerwone]).

przepis('Lobster thermidor', glowne, normalna, francuska, 60, trudny, umami, 600,
        [homar, maslo, musztarda, smietana, ser_gruyere, szalotka, koniakl]).

% Dania jednogarnkowe
przepis('Gulasz wołowy', glowne, normalna, wegierska, 120, sredni, umami, 550,
        [wolowina, ziemniaki, marchew, cebula, papryka, kminek, wino_czerwone]).

przepis('Cassoulet', glowne, normalna, francuska, 180, trudny, umami, 750,
        [fasola, kielbasa, boczek, kaczka_konfitowana, pomidory, tymianek]).

przepis('Ratatouille', glowne, weganska, francuska, 60, sredni, neutralny, 300,
        [baklazan, cukinia, papryka, pomidory, cebula, czosnek, zioła_prowansalskie]).

% Dania z ryb i owoców morza
przepis('Ceviche', przystawka, normalna, peruwianska, 30, sredni, kwasny, 250,
        [dorsz, limonka, cebula_czerwona, kolendra, chili, kukurydza]).

przepis('Fish and chips', glowne, normalna, brytyjska, 45, sredni, neutralny, 700,
        [dorsz, ziemniaki, maka_pszenna, piwo, groszek, sos_tatarski]).

przepis('Krewetki w sosie winno-maślanym', glowne, normalna, francuska, 25, sredni, umami, 400,
        [krewetki, maslo, wino_biale, czosnek, natka_pietruszki, cytryna]).

% Dania z grilla
przepis('Szaszłyki', glowne, normalna, miedzynarodowa, 40, latwy, neutralny, 450,
        [mieso_wieprzowe, papryka, cebula, pieczarki, oliwa, przyprawy]).

przepis('Hamburger', glowne, normalna, amerykanska, 30, sredni, umami, 650,
        [wolowina_mielona, bulka, ser_cheddar, salata, pomidor, cebula, sos]).

przepis('Grillowany łosoś', glowne, normalna, miedzynarodowa, 20, latwy, neutralny, 400,
        [losos, cytryna, koper, czosnek, oliwa, sol, pieprz]).

% Dania śniadaniowe
przepis('Pancakes', sniadanie, normalna, amerykanska, 25, latwy, slodki, 400,
        [maka_pszenna, jajka, mleko, maslo, syrop_klonowy, proszek_do_pieczenia]).

przepis('Granola', sniadanie, weganska, miedzynarodowa, 40, latwy, slodki, 300,
        [platki_owsiane, orzechy, miod, rodzynki, olej_kokosowy, cynamon]).

przepis('Frittata', sniadanie, wegetarianska, wloska, 30, sredni, neutralny, 350,
        [jajka, szpinak, pomidory, ser_feta, cebula, ziola]).

% Dania dietetyczne
przepis('Sałatka z quinoa i awokado', glowne, weganska, miedzynarodowa, 20, latwy, neutralny, 350,
        [quinoa, awokado, pomidor, ogorek, ciecierzyca, limonka, oliwa]).

przepis('Pieczona pierś z kurczaka', glowne, normalna, miedzynarodowa, 30, latwy, neutralny, 300,
        [pierś_z_kurczaka, ziola_prowansalskie, cytryna, czosnek, oliwa]).

przepis('Zupa krem z brokulow', zupa, wegetarianska, miedzynarodowa, 25, latwy, neutralny, 200,
        [brokuly, ziemniaki, cebula, smietanka, bulion_warzywny]).

% Dania na zimno
przepis('Tatar', przystawka, normalna, polska, 20, trudny, umami, 300,
        [polędwica_wolowa, cebula, ogorek_kiszony, grzyby_marynowane, żółtko, przyprawy]).

przepis('Carpaccio', przystawka, normalna, wloska, 15, sredni, umami, 250,
        [polędwica_wolowa, rukola, parmezan, kapary, oliwa, cytryna]).

przepis('Vitello tonnato', przystawka, normalna, wloska, 40, trudny, umami, 350,
        [cielecina, tunczyk, anchois, kapary, majonez, cytryna]).

% Dania street food
przepis('Kebab', glowne, normalna, turecka, 20, latwy, neutralny, 600,
        [mieso_baranie, pita, salata, pomidor, cebula, sos_czosnkowy, przyprawy]).

przepis('Pho ga', zupa, normalna, wietnamska, 45, sredni, umami, 400,
        [kurczak, makaron_ryzowy, kiełki, kolendra, imbir, anyż, przyprawy]).

przepis('Pad see ew', glowne, normalna, tajska, 25, sredni, umami, 550,
        [makaron_ryzowy_szeroki, kurczak, brokuly_chinskie, sos_sojowy, jajko]).

% Dania sezonowe - Lato
przepis('Gazpacho andaluzyjskie', zupa, weganska, hiszpanska, 20, latwy, kwasny, 200,
        [pomidory, ogorek, papryka, czosnek, oliwa, ocet_sherry]).

przepis('Sałatka caprese', przystawka, wegetarianska, wloska, 10, latwy, neutralny, 250,
        [pomidory, mozzarella, bazylia, oliwa, sol, pieprz]).

przepis('Zupa truskawkowa', zupa, wegetarianska, polska, 30, latwy, slodki, 200,
        [truskawki, smietana, wino_białe, cukier, mięta]).

% Dania sezonowe - Zima
przepis('Boeuf bourguignon', glowne, normalna, francuska, 180, trudny, umami, 650,
        [wolowina, marchew, cebula, boczek, wino_czerwone, grzyby]).

przepis('Zupa grzybowa', zupa, wegetarianska, polska, 45, sredni, umami, 300,
        [grzyby_lesne, ziemniaki, smietana, marchew, pietruszka, makaron]).

przepis('Piernik', deser, wegetarianska, polska, 60, sredni, slodki, 400,
        [maka_pszenna, miod, przyprawy_korzenne, jajka, mleko, maslo]). 