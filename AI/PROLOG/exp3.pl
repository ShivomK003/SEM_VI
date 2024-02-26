% Suspects
suspect(miss_scarlet).
suspect(colonel_mustard).
suspect(mrs_peacock).
suspect(mr_green).
suspect(mrs_white).

% Victim
victim(prof_plum).

% Murder weapon
murder_weapon(knife).

% Motives
motive(miss_scarlet, jealousy).
motive(colonel_mustard, revenge).
motive(mrs_peacock, blackmail).
motive(mr_green, greed).

% Clues
clue(miss_scarlet, was_near_scene).
clue(colonel_mustard, has_fingerprints_on_weapon).
clue(mr_green, has_alibi).
clue(mrs_peacock, has_alibi).
clue(mrs_white, found_with_bloodstains).

% Rules
has_alibi(X) :-
    suspect(X),
    clue(X, has_alibi).

guilty(X) :-
    suspect(X),
    motive(X, _),
    clue(X, has_fingerprints_on_weapon),
    not(clue(X, has_alibi)).

% Solution
murderer(Killer, Weapon, Motive, Clue) :-
    guilty(Killer),
    murder_weapon(Weapon),
    motive(Killer, Motive),
    clue(Killer, Clue).
