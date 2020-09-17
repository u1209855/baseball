INSERT INTO wh.managers
("playerID", "yearID", "teamID_auto", "lgID", inseason, "G", "W", "L", rank, "plyMgr")

SELECT "playerID", pm."yearID", "teamID_auto", "lgID", inseason, pm."G", pm."W", pm."L", rank, "plyMgr"
	FROM public.managers pm
	LEFT JOIN wh.teams wt ON pm."teamID" = wt."teamID"
	                      AND pm."yearID" = wt."yearID";

	drop table public.managers;