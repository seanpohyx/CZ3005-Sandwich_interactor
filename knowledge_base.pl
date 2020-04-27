
/*meal checkers; to verify if the following meals are selected*/
is_healthy_meal(healthy).
is_value_meal(value).
is_vegan_meal(vegan).
is_veggie_meal(veggie).

/*consists of all the available meals*/
meals([healthy, normal, value, vegan, veggie]).
/*consists of all the available breads*/
breads([italian, hearty_italian, mulitgrain, honey_oat, parmesan, flatbread, parmesan_oregano]).
/*consists of all the available veggies*/
veggies([lettuce, tomatoes, cucumbers, green_peppers, onions, olives, pickles, jalapenos]).
/*consists of all the available fatty sauces*/
fatty_sauces([spicy_mayo, mayo, bbq, ranch, chipotle_southwest, mustard]).
/*consists of all the available non-fatty sauces*/
non_fatty_sauces([honey_mustard, sweet_onion, chilli, ketchup, salt, pepper]).

/*consists of all the meat top-ups*/
meat_topups([tuna, bacon]).
/*consists of all the vegan top-ups*/
vegan_topups([avocado]).
/*consists of all the veggie top-ups*/
veggie_topups([american_cheese, shredded_cheddar, egg_mayo]).

/*consists of all the sides*/
sides([chips, cookies, hashbrowns]).

/*consists of all the drinks*/
drinks([water, coke, ice_lemon_tea, hot_cappuccino, hot_coffee_without_milk, hot_tea_without_milk, orange_juice]).

/*consists of all the mains*/
mains([chicken_bacon_ranch, chicken_teritaki, cold_cut_trio, egg_mayo, italian_bmt, meatball_marinara_melt, roast_beef, roasted_chicken_breast, steak_cheese, subway_club, subway_melt, turkey]).

/*consists of all the veggies main*/
veggie_mains([veggie_delite, veggie_patty]).

/*ask for all the meals*/
ask_meal(X):-meals(X).

/*ask for all the breads*/
ask_bread(X):-breads(X).

/*ask for all the mains, if vegan or veggie is chosen, only veggie mains will be shown. Else, it will show everything including veggie mains*/
ask_mains(X):-chosen_meal(Y)->((\+is_vegan_meal(Y), \+is_veggie_meal(Y))->(veggie_mains(M1), mains(M2), append(M1, M2, X)); veggie_mains(X)).

/*ask for all the veggies*/
ask_veggie(X):-veggies(X).

/*ask for all the top-ups*/
/*if value meal is chosen, no topup will be available*/
/*if vegan meal is chosen, only vegan topup will be available*/
/*if veggie meal is chosen, only veggie topup will be available. That is inclusive of veggie and vegan topups*/
/*else all topups will be available. vegan, veggie and meat topups*/
ask_topup(X):-chosen_meal(Y)->
(\+is_value_meal(Y)->
(is_vegan_meal(Y)->vegan_topups(X);
 is_veggie_meal(Y)->(vegan_topups(V1), veggie_topups(V2), append(V1, V2, X));
 ((vegan_topups(V1), veggie_topups(V2), append(V1, V2, M1)), meat_topups(M2), append(M1, M2, X)))).

/*if healthy meal is chosen, only non fatty sauces will be available, else everthing including fatty sauces will be available*/
ask_sauces(X):-chosen_meal(Y)->(is_healthy_meal(Y)->non_fatty_sauces(X); (non_fatty_sauces(S1), fatty_sauces(S2), append(S1, S2, X))).

/*ask for all sides*/
ask_sides(X):-sides(X).

/*ask for all drinks*/
ask_drinks(X):-drinks(X).

/*show all selected choices*/
show_meals(X) :- findall(Y, chosen_meal(Y), X).
show_breads(X) :- findall(Y, chosen_bread(Y), X).
show_mains(X) :- findall(Y, chosen_main(Y), X).
show_veggies(X) :- findall(Y, chosen_veggie(Y), X).
show_sauces(X) :- findall(Y, chosen_sauce(Y), X).
show_topups(X) :- findall(Y, chosen_topup(Y), X).
show_sides(X) :- findall(Y, chosen_side(Y), X).
show_drinks(X) :- findall(Y, chosen_drink(Y), X).
