insert into wh.pitching_post
("playerID_auto", "yearID", round, "teamID_auto", "lgID", "W", "L", "G", "GS", "CG", "SHO", "SV", "IPouts", "H", "ER", "HR", "BB", "SO", "BAopp", "ERA", "IBB", "WP", "HBP", "BK", "BFP", "GF", "R", "SH", "SF", "GIDP")
SELECT "playerID_auto", pp."yearID", round, "teamID_auto", pp."lgID", pp."W", pp."L", pp."G", pp."GS", pp."CG", pp."SHO", pp."SV",
pp."IPouts", pp."H", pp."ER", pp."HR", pp."BB", pp."SO", pp."BAopp", pp."ERA", pp."IBB", pp."WP", pp."HBP", pp."BK", pp."BFP",
pp."GF", pp."R", pp."SH", pp."SF", pp."GIDP"
	FROM public.pitching_post pp
	LEFT JOIN wh.master wm ON pp."playerID" = wm."playerID"
	LEFT JOIN wh.teams wt ON pp."teamID" = wt."teamID"
	                      AND pp."yearID" = wt."yearID";


	drop table public.pitching_post;