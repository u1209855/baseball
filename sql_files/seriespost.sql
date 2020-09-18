insert into wh.series_post
("yearID", round, "teamID_auto_Winner", "lgIDWinner", "teamID_auto_Loser", "lgIDLoser", wins, losses, ties)
SELECT ps."yearID", round,  wt."franchID_auto", "lgIDWinner", wt2."franchID_auto", "lgIDLoser", wins, losses, ties
	FROM public.series_post ps
	left join wh.teams wt ON ps."teamIDWinner" = wt."teamID"
	                      AND ps."yearID" = wt."yearID"
	left join wh.teams wt2 ON ps."teamIDLoser" = wt2."teamID"
	                       AND ps."yearID" = wt."yearID"
    group by ps."yearID", round, wt."franchID_auto", "teamIDWinner", "lgIDWinner", wt2."franchID_auto", "lgIDLoser", wins, losses, ties;

	drop table public.series_post