INSERT INTO
wh.salaries ("yearID", "teamID_auto", "lgID", "playerID_auto", salary)
SELECT ps."yearID", "teamID_auto", ps."lgID", "playerID_auto", salary
	FROM public.salaries ps
	LEFT JOIN wh.master wm ON ps."playerID" = wm."playerID"
	LEFT JOIN wh.teams wt ON ps."teamID" = wt."teamID"
	                      AND ps."yearID" = wt."yearID";

	drop table public.salaries;