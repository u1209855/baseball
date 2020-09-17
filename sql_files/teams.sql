INSERT into wh.teams (
 "yearID", "lgId", "teamID", "franchID_auto", "divID", "Rank", "G", "Ghome", "W", "L", "DivWin", "WCWin", "LgWin", "WSWin", "R", "AB", "H", "B2", "B3", "HR", "BB", "SO", "SB", "CS", "HBP", "SF", "RA", "ER", "ERA", "CG", "SHO", "SV", "IPouts", "HA", "HRA", "BBA", "SOA", "E", "DP", "FP", name, park, attendance, "BPF", "PPF", "teamIDBR", "teamIDAhlman", "teamIDretro")
SELECT "yearID", "lgId", "teamID", tf."franchID_auto", "divID", "Rank", "G", "Ghome", "W", "L", "DivWin", "WCWin", "LgWin", "WSWin", "R", "AB", "H", "B2", "B3", "HR", "BB", "SO", "SB", "CS", "HBP", "SF", "RA", "ER", "ERA", "CG", "SHO", "SV", "IPouts", "HA", "HRA", "BBA", "SOA", "E", "DP", "FP", name, park, attendance, "BPF", "PPF", "teamIDBR", "teamIDAhlman", "teamIDretro"
	FROM public.teams pt
	LEFT JOIN wh.team_franchises tf ON pt."franchID" = tf."franchID";

drop table public.teams;