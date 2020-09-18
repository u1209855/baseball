INSERT into wh.awardsshareplayers
("awardID", "yearID", "lgID", "playerID_auto", "pointsWon", "pointsMax", "votesFirst")
SELECT "awardID", pa."yearID", pa."lgID", "playerID_auto", "pointsWon", "pointsMax", "votesFirst"
	FROM public.awardsshareplayers pa
	LEFT JOIN wh.master wm ON pa."playerID" = wm."playerID";

	drop table public.awardsshareplayers;