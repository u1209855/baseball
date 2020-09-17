INSERT into wh.allstarfull
("playerID_auto", "yearID", "gameNum", "gameID", "teamID_auto", "lgID", "GP", "startingPOS")
SELECT "playerID_auto", pa."yearID", "gameNum", "gameID", "teamID_auto", pa."lgID", "GP", "startingPOS"
	FROM public.allstarfull pa
	LEFT JOIN wh.teams wt ON pa."teamID" = wt."teamID"
	                      AND pa."yearID" = wt."yearID"
	LEFT JOIN wh.master wm ON pa."playerID" = wm."playerID";

drop table public.allstarfull;