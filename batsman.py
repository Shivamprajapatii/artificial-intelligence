% Define the predicates
batsman(sachin).
wicketkeeper(dhoni).
footballer(ronaldo).
% Define the rule
cricketer(X) :- batsman(X).
crickerter(X):-wicketkiper(X).
not_creicketer(A) :- footballer(A).


Output:
% Query
?- cricketer(sachin)
