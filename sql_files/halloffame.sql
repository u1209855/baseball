insert into wh.halloffame
("playerID_auto", "yearID", "votedBy", ballots, needed, votes, inducted, category, needed_note)
SELECT "playerID_auto", "yearID", "votedBy", ballots, needed, votes, inducted, category, needed_note
	FROM public.halloffame ph
	LEFT JOIN wh.master wm ON ph."playerID" = wm."playerID";

	drop table public.halloffame