insert into wh.batting_post
("yearID", round, "playerID_auto", "teamID_auto", "lgID", "G", "AB", "R", "H", "B2", "B3", "HR", "RB", "SB", "CS", "BB", "SO", "IBB", "HBP", "SH", "SF", "GIDP"
)
SELECT bp."yearID", round, "playerID_auto", "teamID_auto", "lgID", bp."G", bp."AB",
bp."R", bp."H", bp."B2", bp."B3", bp."HR", bp."RB", bp."SB", bp."CS", bp."BB", bp."SO", bp."IBB", bp."HBP",
bp."SH", bp."SF", bp."GIDP"
	FROM public.batting_post bp
	left join wh.master wm ON bp."playerID" = wm."playerID"
	left join wh.teams wt ON bp."teamID" = wt."teamID"
	                      AND bp."yearID" = wt."yearID";

	drop table public.batting_post;