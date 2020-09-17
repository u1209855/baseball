INSERT into wh.awardssharemanagers
("manager_ID", "awardID", "yearID", "lgID", "pointsWon", "pointsMax", "votesFirst"
)
SELECT  "manager_ID", "awardID", pa."yearID", pa."lgID", "pointsWon", "pointsMax", "votesFirst"
	FROM public.awardssharemanagers pa
	left join wh.managers wm ON pa."playerID" = wm."playerID"
	                         AND pa."yearID" = wm."yearID";

	drop table public.awardssharemanagers;