INSERT into wh.fieldingof
("playerID_auto", "yearID", stint, glf, gcf, grf)
SELECT "playerID_auto", "yearID", stint, glf, gcf, grf
	FROM public.fieldingof pf
	LEFT JOIN wh.master wm ON wm."playerID" = pf."playerID";

	drop table public.fieldingof;