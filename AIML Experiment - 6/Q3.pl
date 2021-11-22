slice([H|_],[0,0],[H]).
slice([H|T],[0,To],[H|X]) :-
        N is To - 1,
        slice(T,[0,N],X).
slice([_|T],[From,To], L) :-
        N is From - 1,
        M is To - 1,
        slice(T,[N,M],L).
