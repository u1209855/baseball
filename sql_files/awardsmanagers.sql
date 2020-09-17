INSERT into wh.awardsmanagers
("manager_ID", "awardID", "yearID", "lgID", tie, notes)
select "manager_ID", "awardID", pa."yearID", pa."lgID", tie, notes
	FROM public.awardsmanagers pa
	LEFT JOIN wh.managers_lu wm ON pa."playerID" = wm."playerID";

drop table public.awardsmanagers;

