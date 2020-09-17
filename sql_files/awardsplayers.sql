INSERT into wh.awardsplayers
("playerID_auto", "awardID", "yearID", "lgID", tie, notes)
SELECT "playerID_auto", "awardID", pa."yearID", pa."lgID", tie, notes
	FROM public.awardsplayers pa
	LEFT JOIN wh.master wm ON pa."playerID" = wm."playerID";

drop table public.awardsplayers;