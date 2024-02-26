% Facts 
male(sunai).
male(ashish).
male(ravi).
male(subarao).
male(amit).
male(shivom).
male(ishaan).
male(shlok).
male(samved).

female(sunanda).
female(vishaka).
female(kanchan).
female(asha).
female(nilima).
female(mrinal).

parent(ashish, sunai).
parent(ashish, sunanda).
parent(kanchan, sunai).
parent(kanchan, sunanda).

parent(amit, subarao).
parent(amit, asha).
parent(vishaka, subarao).
parent(vishaka, asha).

parent(shivom, ashish).
parent(shivom, vishaka).
parent(mrinal, ashish).
parent(mrinal, vishaka).
parent(ishaan, amit).
parent(ishaan, nilima).
parent(shlok, kanchan).
parent(shlok, ravi).
parent(samved, kanchan).
parent(samved, ravi).

married(vishaka, ashish).
married(ashish, vishaka).
married(ravi, kanchan).
married(kanchan, ravi).
married(amit, nilima).
married(nilima, amit).
married(asha, subarao).
married(subarao, asha).
married(sunai, sunanda).
married(sunanda, sunai).

% Rules
father(X, Y) :- parent(X, Y), male(Y).
mother(X, Y) :- parent(X, Y), female(Y).
grandfather(X, Z) :- parent(X, Y), father(Y, Z).
grandmother(X, Z) :- parent(X, Y), mother(Y, Z).

sibling(X, Y) :- father(X, Z), father(Y, Z), mother(X, W), mother(Y, W), X \= Y.
sister(X, Y) :- sibling(X, Y), female(Y).
brother(X, Y) :- sibling(X, Y), male(Y).

aunt(X, Y) :- father(X, Z), sister(Z,Y)  ; mother(X, Z), sister(Z,Y).
uncle(X, Y) :- father(X, Z), brother(Z,Y)  ; mother(X, Z), brother(Z,Y).

cousin(X, Y) :- parent(Y, Z), aunt(X, Z) ; parent(Y, Z), uncle(X, Z) ; cousin(X, Z), cousin(Z, Y).

parent_in_law(X, Y) :- parent(Z, Y), married(X, Z).
father_in_law(X, Y) :- parent_in_law(X, Y), male(Y).
mother_in_law(X, Y) :- parent_in_law(X, Y), female(Y).

