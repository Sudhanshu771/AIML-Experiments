rle([],[]).
rle([X],[X]).
rle([X,X|Xs],Zs) :- rle([X|Xs],Zs).
rle([X,Y|Ys],[X|Zs]) :- X \= Y, rle([Y|Ys],Zs).
