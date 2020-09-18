INSERT INTO wh.managers
("manager_ID", "yearID", "teamID_auto", "lgID", inseason, "G", "W", "L", rank, "plyMgr")

SELECT "manager_ID", pm."yearID", "teamID_auto", "lgID", inseason, pm."G", pm."W", pm."L", rank, "plyMgr"
	FROM public.managers pm
	LEFT JOIN wh.teams wt ON pm."teamID" = wt."teamID"
	                      AND pm."yearID" = wt."yearID"
	left join wh.managers_lu wl ON pm."playerID" = wl."playerID";

	drop table public.managers;