insert into wh.pitching
("playerID_auto", "yearID", stint, "teamID_auto", "lgID", "W", "L", "G", "GS", "CG", "SHO", "SV", "IPouts", "H", "ER", "HR", "BB", "SO", "BAopp", "ERA", "IBB", "WP", "HBP", "BK", "BFP", "GF", "R", "SH", "SF", "GIDP")
SELECT "playerID_auto", pp."yearID", stint, "teamID_auto", pp."lgID", pp."W", pp."L", pp."G", pp."GS", pp."CG", pp."SHO", pp."SV", pp."IPouts", pp."H", pp."ER",
pp."HR", pp."BB", pp."SO", pp."BAopp", pp."ERA", pp."IBB", pp."WP", pp."HBP", pp."BK", pp."BFP", pp."GF", pp."R", pp."SH",
pp."SF", pp."GIDP"
	FROM public.pitching pp
	left join wh.master wm ON pp."playerID" = wm."playerID"
	left join wh.teams wt ON pp."teamID" = wt."teamID"
	                      AND pp."yearID" = wt."yearID";

	drop table public.pitching;