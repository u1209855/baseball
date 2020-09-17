INSERT into wh.teams_half
("yearID", "lgID", "teamID_auto", half, "divID", "divWin", "Rank", "G", "W", "L")
SELECT th."yearID", th."lgID", "teamID_auto", half, th."divID", "divWin", th."Rank", th."G", th."W", th."L"
	FROM public.teams_half th
	left join wh.teams wt ON th."teamID" = wt."teamID"
	                     AND th."yearID" = wt."yearID";

drop table public.teams_half;