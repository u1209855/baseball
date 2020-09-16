INSERT into wh.team_franchises ("franchID", "franchName", active, "NAassoc")
SELECT "franchID", "franchName", active, "NAassoc"
	FROM public.team_franchises;

	drop table public.team_franchises;