INSERT into wh.batting
("playerID_auto", "yearID", stint, "teamID_auto", "lgID", "G", "AB", "R", "H", "B2", "B3", "HR", "RB", "SB", "CS", "BB", "SO", "IBB", "HBP", "SH", "SF", "GIDP"
)
SELECT "playerID_auto", pa."yearID", stint, "teamID_auto", "lgID", pa."G", pa."AB", pa."R", pa."H", pa."B2", pa."B3", pa."HR", pa."RB", pa."SB",
pa."CS", pa."BB", pa."SO", "IBB", pa."HBP", pa."SH", pa."SF", pa."GIDP"
	FROM public.batting pa
	left join wh.master wm ON pa."playerID" = wm."playerID"
	left join wh.teams wt ON pa."teamID" = wt."teamID"
	                      AND pa."yearID" = wt."yearID";

	drop table public.batting;