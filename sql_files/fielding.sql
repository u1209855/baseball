insert into wh.fielding
("playerID_auto", "yearID", stint, "teamID_auto", "lgID", "POS", "G", "GS", "InnOuts", "PO", "A", "E", "DP", "PB", "WP", "SB", "CS", "ZR")

SELECT "playerID_auto", pf."yearID", stint, "teamID_auto", pf."lgID", "POS", pf."G", pf."GS", "InnOuts", "PO", "A", pf."E", pf."DP", pf."PB",
pf."WP", pf."SB", pf."CS", "ZR"
	FROM public.fielding pf
	left join wh.master wm ON pf."playerID" = wm."playerID"
	left join wh.teams wt ON pf."teamID" = wt."teamID"
	                      AND pf."yearID" = wt."yearID";

	drop table public.fielding;