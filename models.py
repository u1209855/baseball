from sqlalchemy import Column, INTEGER, NVARCHAR, TIMESTAMP, ForeignKey, DECIMAL, UniqueConstraint, JSON, \
    FLOAT, VARCHAR, DATE
from database import Base


class Master(Base):
    __tablename__ = "master"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    birthYear = Column(VARCHAR(4))
    birthMonth = Column(INTEGER)
    birthDay = Column(INTEGER)
    birthCountry = Column(VARCHAR(15))
    birthState = Column(VARCHAR(30))
    birthCity = Column(VARCHAR(30))
    deathYear = Column(VARCHAR(4))
    deathMonth = Column(INTEGER)
    deathDay = Column(INTEGER)
    deathCountry = Column(VARCHAR(15))
    deathState = Column(VARCHAR(30))
    deathCity = Column(VARCHAR(30))
    nameFirst = Column(VARCHAR(20))
    nameLast = Column(VARCHAR(20))
    nameGiven = Column(VARCHAR(60))
    weight = Column(INTEGER)
    height = Column(INTEGER)
    bats = Column(VARCHAR(1))
    throws = Column(VARCHAR(1))
    debut = Column(DATE)
    finalGame = Column(DATE)
    retroID = Column(VARCHAR(10))
    bbrefID = Column(VARCHAR(10))


class TeamFranchises(Base):
    __tablename__ = "team_franchises"
    __table_args__ = {"schema": "public"}
    franchID = Column(VARCHAR(3), primary_key=True)
    franchName = Column(VARCHAR(30))
    active = Column(VARCHAR(1))
    NAassoc = Column(VARCHAR(3))


class Teams(Base):
    __tablename__ = "teams"
    __table_args__ = {"schema": "public"}
    yearID = Column(VARCHAR(4))
    teamID = Column(VARCHAR(3), primary_key=True)
    franchID = Column(VARCHAR(3), ForeignKey(TeamFranchises.franchID))
    divID = Column(VARCHAR(1))
    Rank = Column(INTEGER)
    G = Column(INTEGER)
    Ghome = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    DivWin = Column(VARCHAR(1))
    WCWin = Column(VARCHAR(1))
    LgWin = Column(VARCHAR(1))
    WSWin = Column(VARCHAR(1))
    R = Column(INTEGER)
    AB = Column(INTEGER)
    H = Column(INTEGER)
    B2 = Column(INTEGER)
    B3 = Column(INTEGER)
    HR = Column(INTEGER)
    BB = Column(INTEGER)
    SO = Column(INTEGER)
    SB = Column(INTEGER)
    SB = Column(INTEGER)
    CS = Column(INTEGER)
    HBP = Column(INTEGER)
    SF = Column(INTEGER)
    RA = Column(INTEGER)
    ER = Column(INTEGER)
    ERA = Column(INTEGER)
    CG = Column(INTEGER)
    SHO = Column(INTEGER)
    SV = Column(INTEGER)
    IPouts = Column(INTEGER)
    HA = Column(INTEGER)
    HRA = Column(INTEGER)
    BBA = Column(INTEGER)
    BPF = Column(INTEGER)
    SOA = Column(INTEGER)
    E = Column(INTEGER)
    DP = Column(INTEGER)
    FP = Column(INTEGER)
    name = Column(VARCHAR(30))
    park = Column(VARCHAR(45))
    attendance = Column(INTEGER)
    PPF = Column(INTEGER)
    teamIDBR = Column(VARCHAR(3))
    teamIDAhlman = Column(VARCHAR(3))
    teamIDretro = Column(VARCHAR(3))


class Managers(Base):
    __tablename__ = "managers"
    __table_args__ = {"schema": "public"}
    manager_ID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10))
    yearID = Column(VARCHAR(4))
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(2))
    inseason = Column(INTEGER)
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    rank = Column(INTEGER)
    plyMgr = Column(VARCHAR(1))
    UniqueConstraint(playerID, yearID)


class TeamsHalf(Base):
    __tablename__ = "teams_half"
    __table_args__ = {"schema": "public"}
    teamsHalfID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4))
    lgID = Column(VARCHAR(2))
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    half = Column(INTEGER)
    divID = Column(VARCHAR(2))
    divWin = Column(VARCHAR(1))
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    UniqueConstraint(teamID, yearID, half)


class AwardsShareManagers(Base):
    __tablename__ = "awardssharemanagers"
    __table_args__ = {"schema": "public"}
    awardsShareManagersID = Column(INTEGER, primary_key=True, autoincrement=True)
    manager_ID = Column(INTEGER, ForeignKey(Managers.manager_ID))
    playerID = Column(VARCHAR(10))
    yearID = Column(VARCHAR(4))
    lgID = Column(VARCHAR(2))
    awardID = Column(VARCHAR(20))
    pointsWon = Column(INTEGER)
    pointsMax = Column(INTEGER)
    votesFirst = Column(INTEGER)
    UniqueConstraint(playerID, yearID, lgID)


class AllStarFull(Base):
    __tablename__ = "allstarfull"
    __table_args__ = {"schema": "public"}
    allStarFullID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    gameNum = Column(INTEGER)
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(3))
    GP = Column(INTEGER)
    startingPOS = Column(INTEGER)
    UniqueConstraint(playerID, yearID)


class AwardsManagers(Base):
    __tablename__ = "awardsmanagers"
    __table_args__ = {"schema": "public"}
    awardsManagersID = Column(INTEGER, primary_key=True, autoincrement=True)
    manager_ID = Column(INTEGER, ForeignKey(Managers.manager_ID))
    playerID = Column(VARCHAR(10))
    awardID = Column(VARCHAR(30))
    yearID = Column(VARCHAR(4))
    lgID = Column(VARCHAR(2))
    tie = Column(VARCHAR(1))
    notes = Column(VARCHAR(3))
    UniqueConstraint(playerID, awardID, yearID)


class AwardsPlayers(Base):
    __tablename__ = "awardsplayers"
    __table_args__ = {"schema": "public"}
    awardsPlayersID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    awardID = Column(VARCHAR(30))
    yearID = Column(VARCHAR(4))
    lgID = Column(VARCHAR(2))
    tie = Column(VARCHAR(1))
    notes = Column(VARCHAR(3))
    UniqueConstraint(playerID, awardID, yearID)


class AwardsSharePlayers(Base):
    __tablename__ = "awardsshareplayers"
    __table_args__ = {"schema": "public"}
    awardsSharePlayersID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    awardID = Column(VARCHAR(20))
    yearID = Column(VARCHAR(4))
    lgID = Column(VARCHAR(2))
    pointsWon = Column(INTEGER)
    pointsMax = Column(INTEGER)
    votesFirst = Column(INTEGER)
    UniqueConstraint(playerID, awardID, yearID)


class Batting(Base):
    __tablename__ = "batting"
    __table_args__ = {"schema": "public"}
    battingID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    stint = Column(INTEGER)
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(3))
    G = Column(INTEGER)
    AB = Column(INTEGER)
    R = Column(INTEGER)
    H = Column(INTEGER)
    B2 = Column(INTEGER)
    B3 = Column(INTEGER)
    HR = Column(INTEGER)
    RB = Column(INTEGER)
    SB = Column(INTEGER)
    CS = Column(INTEGER)
    BB = Column(INTEGER)
    SO = Column(INTEGER)
    IBB = Column(INTEGER)
    HBP = Column(INTEGER)
    SH = Column(INTEGER)
    SF = Column(INTEGER)
    GIDP = Column(INTEGER)
    UniqueConstraint(playerID, yearID, teamID)


class Salaries(Base):
    __tablename__ = "salaries"
    __table_args__ = {"schema": "public"}
    salariesID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4))
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(2))
    salary = Column(INTEGER)
    UniqueConstraint(yearID, playerID)


class FieldingOF(Base):
    __tablename__ = "fieldingOF"
    __table_args__ = {"schema": "public"}
    fieldingOFID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    stint = Column(INTEGER)
    glf = Column(INTEGER)
    gcf = Column(INTEGER)
    grf = Column(INTEGER)
    UniqueConstraint(playerID, yearID)


class HallofFame(Base):
    __tablename__ = "halloffame"
    __table_args__ = {"schema": "public"}
    hallofFameID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    votedBy = Column(VARCHAR(20))
    ballots = Column(INTEGER)
    needed = Column(INTEGER)
    votes = Column(INTEGER)
    inducted = Column(VARCHAR(1))
    category = Column(VARCHAR(10))
    needed_note = Column(VARCHAR(10))
    UniqueConstraint(playerID, yearID)


class ManagersHalf(Base):
    __tablename__ = "managers_half"
    __table_args__ = {"schema": "public"}
    managersHalfID = Column(INTEGER, primary_key=True, autoincrement=True)
    managerID = Column(INTEGER, ForeignKey(Managers.manager_ID))
    playerID = Column(VARCHAR(10))
    yearID = Column(VARCHAR(4))
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(2))
    inseason = Column(INTEGER)
    half = Column(INTEGER)
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    rank = Column(INTEGER)
    UniqueConstraint(playerID, yearID)


class SeriesPost(Base):
    __tablename__ = "series_post"
    __table_args__ = {"schema": "public"}
    seriesPostID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4))
    round = Column(VARCHAR(5))
    teamIDWinner = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgIDWinner = Column(VARCHAR(2))
    teamIDLoser = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgIDLoser = Column(VARCHAR(2))
    wins = Column(INTEGER)
    losses = Column(INTEGER)
    ties = Column(INTEGER)
    UniqueConstraint(yearID, round)


class BattingPost(Base):
    __tablename__ = "batting_post"
    __table_args__ = {"schema": "public"}
    battingPostID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    stint = Column(INTEGER)
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(3))
    G = Column(INTEGER)
    AB = Column(INTEGER)
    R = Column(INTEGER)
    H = Column(INTEGER)
    B2 = Column(INTEGER)
    B3 = Column(INTEGER)
    HR = Column(INTEGER)
    RB = Column(INTEGER)
    SB = Column(INTEGER)
    CS = Column(INTEGER)
    BB = Column(INTEGER)
    SO = Column(INTEGER)
    IBB = Column(INTEGER)
    HBP = Column(INTEGER)
    SH = Column(INTEGER)
    SF = Column(INTEGER)
    GIDP = Column(INTEGER)
    UniqueConstraint(playerID, yearID, teamID)


class Fielding(Base):
    __tablename__ = "fielding"
    __table_args__ = {"schema": "public"}
    fieldingID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    stint = Column(INTEGER)
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(3))
    POS = Column(VARCHAR(2))
    G = Column(INTEGER)
    GS = Column(INTEGER)
    InnOuts = Column(INTEGER)
    PO = Column(INTEGER)
    A = Column(INTEGER)
    E = Column(INTEGER)
    DP = Column(INTEGER)
    PB = Column(INTEGER)
    WP = Column(INTEGER)
    SB = Column(INTEGER)
    CS = Column(INTEGER)
    ZR = Column(INTEGER)
    UniqueConstraint(playerID, yearID)


class Pitching(Base):
    __tablename__ = "pitching"
    __table_args__ = {"schema": "public"}
    pitchingID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    stint = Column(INTEGER)
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(2))
    W = Column(INTEGER)
    L = Column(INTEGER)
    G = Column(INTEGER)
    GS = Column(INTEGER)
    CG = Column(INTEGER)
    SHO = Column(INTEGER)
    SV = Column(INTEGER)
    IPouts = Column(INTEGER)
    H = Column(INTEGER)
    ER = Column(INTEGER)
    HR = Column(INTEGER)
    BB = Column(INTEGER)
    SO = Column(INTEGER)
    BAopp = Column(FLOAT)
    ERA = Column(FLOAT)
    IBB = Column(INTEGER)
    WP = Column(INTEGER)
    HBP = Column(INTEGER)
    BK = Column(INTEGER)
    BFP = Column(INTEGER)
    GF = Column(INTEGER)
    R = Column(INTEGER)
    SH = Column(INTEGER)
    SF = Column(INTEGER)
    GIDP = Column(INTEGER)
    UniqueConstraint(playerID, teamID, yearID)


class PitchingPost(Base):
    __tablename__ = "pitching_post"
    __table_args__ = {"schema": "public"}
    pitchingPostID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4))
    round = Column(VARCHAR(3))
    teamID = Column(VARCHAR(3), ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(2))
    W = Column(INTEGER)
    L = Column(INTEGER)
    G = Column(INTEGER)
    GS = Column(INTEGER)
    CG = Column(INTEGER)
    SHO = Column(INTEGER)
    SV = Column(INTEGER)
    IPouts = Column(INTEGER)
    H = Column(INTEGER)
    ER = Column(INTEGER)
    HR = Column(INTEGER)
    BB = Column(INTEGER)
    SO = Column(INTEGER)
    BAopp = Column(FLOAT)
    ERA = Column(FLOAT)
    IBB = Column(INTEGER)
    WP = Column(INTEGER)
    HBP = Column(INTEGER)
    BK = Column(INTEGER)
    BFP = Column(INTEGER)
    GF = Column(INTEGER)
    R = Column(INTEGER)
    SH = Column(INTEGER)
    SF = Column(INTEGER)
    GIDP = Column(INTEGER)
    UniqueConstraint(teamID, playerID, yearID)


def create_models(engine):
    print("dropping tables")
    Base.metadata.drop_all(engine)
    print("creating tables")
    Base.metadata.create_all(engine)