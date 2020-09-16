INSERT INTO wh.master ("playerID", "birthYear", "birthMonth", "birthDay", "birthCountry", "birthState", "birthCity", "deathYear", "deathMonth", "deathDay", "deathCountry", "deathState", "deathCity", "nameFirst", "nameLast", "nameGiven", weight, height, bats, throws, debut, "finalGame", "retroID", "bbrefID")
	select "playerID", "birthYear", "birthMonth", "birthDay", "birthCountry", "birthState", "birthCity", "deathYear", "deathMonth", "deathDay", "deathCountry", "deathState", "deathCity", "nameFirst", "nameLast", "nameGiven", weight, height, bats, throws, debut, "finalGame", "retroID", "bbrefID"
	FROM public.master;

DROP TABLE public.master;