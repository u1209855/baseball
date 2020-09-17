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


class Master_Wh(Base):
    __tablename__ = "master"
    __table_args__ = {"schema": "wh"}
    playerID_auto = Column(INTEGER, autoincrement=True, primary_key=True)
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
    UniqueConstraint(playerID)


class TeamFranchises(Base):
    __tablename__ = "team_franchises"
    __table_args__ = {"schema": "public"}
    franchID = Column(VARCHAR(3), primary_key=True)
    franchName = Column(VARCHAR(60))
    active = Column(VARCHAR(2))
    NAassoc = Column(VARCHAR(3))


class TeamFranchises_Wh(Base):
    __tablename__ = "team_franchises"
    __table_args__ = {"schema": "wh"}
    franchID_auto = Column(INTEGER, autoincrement=True, primary_key=True)
    franchID = Column(VARCHAR(3))
    franchName = Column(VARCHAR(60))
    active = Column(VARCHAR(2))
    NAassoc = Column(VARCHAR(3))
    UniqueConstraint(franchID)


class Teams(Base):
    __tablename__ = "teams"
    __table_args__ = {"schema": "public"}
    # teamID_auto = Column(INTEGER, autoincrement=True, primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgId = Column(VARCHAR(2))
    teamID = Column(VARCHAR(3), primary_key=True)
    franchID = Column(VARCHAR(3))  # ForeignKey(TeamFranchises.franchID))
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
    ERA = Column(FLOAT)
    CG = Column(INTEGER)
    SHO = Column(INTEGER)
    SV = Column(INTEGER)
    IPouts = Column(INTEGER)
    HA = Column(INTEGER)
    HRA = Column(INTEGER)
    BBA = Column(INTEGER)
    SOA = Column(INTEGER)
    E = Column(INTEGER)
    DP = Column(INTEGER)
    FP = Column(FLOAT)
    name = Column(VARCHAR(60))
    park = Column(VARCHAR(128))
    attendance = Column(INTEGER)
    BPF = Column(INTEGER)
    PPF = Column(INTEGER)
    teamIDBR = Column(VARCHAR(3))
    teamIDAhlman = Column(VARCHAR(3))
    teamIDretro = Column(VARCHAR(3))
    #  UniqueConstraint(teamID, yearID)


class Teams_Wh(Base):
    __tablename__ = "teams"
    __table_args__ = {"schema": "wh"}
    teamID_auto = Column(INTEGER, autoincrement=True, primary_key=True)
    yearID = Column(VARCHAR(4))
    lgId = Column(VARCHAR(2))
    teamID = Column(VARCHAR(3))
    franchID_auto = Column(INTEGER, ForeignKey(TeamFranchises_Wh.franchID_auto))
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
    ERA = Column(FLOAT)
    CG = Column(INTEGER)
    SHO = Column(INTEGER)
    SV = Column(INTEGER)
    IPouts = Column(INTEGER)
    HA = Column(INTEGER)
    HRA = Column(INTEGER)
    BBA = Column(INTEGER)
    SOA = Column(INTEGER)
    E = Column(INTEGER)
    DP = Column(INTEGER)
    FP = Column(FLOAT)
    name = Column(VARCHAR(60))
    park = Column(VARCHAR(128))
    attendance = Column(INTEGER)
    BPF = Column(INTEGER)
    PPF = Column(INTEGER)
    teamIDBR = Column(VARCHAR(3))
    teamIDAhlman = Column(VARCHAR(3))
    teamIDretro = Column(VARCHAR(3))
    UniqueConstraint(yearID, teamID)


class Managers(Base):
    __tablename__ = "managers"
    __table_args__ = {"schema": "public"}
    # manager_ID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    teamID = Column(VARCHAR(3))
    lgID = Column(VARCHAR(2))
    inseason = Column(INTEGER, primary_key=True)
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    rank = Column(INTEGER)
    plyMgr = Column(VARCHAR(1))
    # UniqueConstraint(playerID, yearID, inseason)


class Managers_Wh(Base):
    __tablename__ = "managers"
    __table_args__ = {"schema": "wh"}
    manager_ID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10))
    yearID = Column(VARCHAR(4))
    teamID_auto = Column(INTEGER, ForeignKey(Teams_Wh.teamID_auto))
    lgID = Column(VARCHAR(2))
    inseason = Column(INTEGER)
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    rank = Column(INTEGER)
    plyMgr = Column(VARCHAR(1))
    UniqueConstraint(playerID, yearID, inseason)


class TeamsHalf(Base):
    __tablename__ = "teams_half"
    __table_args__ = {"schema": "public"}
    # teamsHalfID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2))
    teamID = Column(VARCHAR(3), primary_key=True)  # ForeignKey(Teams.teamID))
    half = Column(INTEGER, primary_key=True)
    divID = Column(VARCHAR(2))
    divWin = Column(VARCHAR(1))
    Rank = Column(INTEGER)
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    UniqueConstraint(teamID, yearID, half)


class TeamsHalf_Wh(Base):
    __tablename__ = "teams_half"
    __table_args__ = {"schema": "wh"}
    teamsHalfID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4))
    lgID = Column(VARCHAR(2))
    teamID_auto = Column(INTEGER, ForeignKey(Teams_Wh.teamID_auto))
    half = Column(INTEGER)
    divID = Column(VARCHAR(2))
    divWin = Column(VARCHAR(1))
    Rank = Column(INTEGER)
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    UniqueConstraint(teamID_auto, yearID, half)

class AwardsShareManagers(Base):
    __tablename__ = "awardssharemanagers"
    __table_args__ = {"schema": "public"}
    # manager_ID = Column(INTEGER)  # ForeignKey(Managers.manager_ID))
    awardID = Column(VARCHAR(20))
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2), primary_key=True)
    playerID = Column(VARCHAR(10), primary_key=True)
    pointsWon = Column(INTEGER)
    pointsMax = Column(INTEGER)
    votesFirst = Column(INTEGER)
    # UniqueConstraint(playerID, yearID, lgID)


class AllStarFull(Base):
    __tablename__ = "allstarfull"
    __table_args__ = {"schema": "public"}
    # allStarFullID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4), primary_key=True)
    gameNum = Column(INTEGER)
    gameID = VARCHAR(12)
    teamID = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(3))
    GP = Column(INTEGER)
    startingPOS = Column(INTEGER)
    # UniqueConstraint(playerID, yearID)


class AwardsManagers(Base):
    __tablename__ = "awardsmanagers"
    __table_args__ = {"schema": "public"}
    # awardsManagersID = Column(INTEGER, primary_key=True, autoincrement=True)
    # manager_ID = Column(INTEGER)  # ForeignKey(Managers.manager_ID))
    playerID = Column(VARCHAR(10), primary_key=True)
    awardID = Column(VARCHAR(30), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2))
    tie = Column(VARCHAR(1))
    notes = Column(VARCHAR(3))
    # UniqueConstraint(playerID, awardID, yearID)


class AwardsPlayers(Base):
    __tablename__ = "awardsplayers"
    __table_args__ = {"schema": "public"}
    # awardsPlayersID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    awardID = Column(VARCHAR(45), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2), primary_key=True)
    tie = Column(VARCHAR(1))
    notes = Column(VARCHAR(10))
    # UniqueConstraint(playerID, awardID, yearID, lgID)


class AwardsSharePlayers(Base):
    __tablename__ = "awardsshareplayers"
    __table_args__ = {"schema": "public"}
    # awardsSharePlayersID = Column(INTEGER, primary_key=True, autoincrement=True)
    awardID = Column(VARCHAR(20), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2))
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    pointsWon = Column(FLOAT)
    pointsMax = Column(INTEGER)
    votesFirst = Column(FLOAT)
    # UniqueConstraint(playerID, awardID, yearID)


class Batting(Base):
    __tablename__ = "batting"
    __table_args__ = {"schema": "public"}
    # battingID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4), primary_key=True)
    stint = Column(INTEGER, primary_key=True)
    teamID = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
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
    # UniqueConstraint(playerID, yearID, stint)


class Salaries(Base):
    __tablename__ = "salaries"
    __table_args__ = {"schema": "public"}
    # salariesID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    teamID = Column(VARCHAR(3), primary_key=True)  # ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(2))
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    salary = Column(INTEGER)
    # UniqueConstraint(yearID, teamID, playerID)


class FieldingOF(Base):
    __tablename__ = "fieldingof"
    __table_args__ = {"schema": "public"}
    # fieldingOFID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4), primary_key=True)
    stint = Column(INTEGER, primary_key=True)
    glf = Column(INTEGER)
    gcf = Column(INTEGER)
    grf = Column(INTEGER)
    # UniqueConstraint(playerID, yearID, stint)


class HallofFame(Base):
    __tablename__ = "halloffame"
    __table_args__ = {"schema": "public"}
    # hallofFameID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4), primary_key=True)
    votedBy = Column(VARCHAR(20), primary_key=True)
    ballots = Column(INTEGER)
    needed = Column(INTEGER)
    votes = Column(INTEGER)
    inducted = Column(VARCHAR(1))
    category = Column(VARCHAR(30))
    needed_note = Column(VARCHAR(10))
    # UniqueConstraint(playerID, yearID, votedBy)


class ManagersHalf(Base):
    __tablename__ = "managers_half"
    __table_args__ = {"schema": "public"}
    # managersHalfID = Column(INTEGER, primary_key=True, autoincrement=True)
    # managerID = Column(INTEGER)  # ForeignKey(Managers.manager_ID))
    playerID = Column(VARCHAR(10), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    teamID = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(2))
    inseason = Column(INTEGER)
    half = Column(INTEGER, primary_key=True)
    G = Column(INTEGER)
    W = Column(INTEGER)
    L = Column(INTEGER)
    rank = Column(INTEGER)
    # UniqueConstraint(playerID, yearID, half)


class SeriesPost(Base):
    __tablename__ = "series_post"
    __table_args__ = {"schema": "public"}
    # seriesPostID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    round = Column(VARCHAR(5), primary_key=True)
    teamIDWinner = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
    lgIDWinner = Column(VARCHAR(2))
    teamIDLoser = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
    lgIDLoser = Column(VARCHAR(2))
    wins = Column(INTEGER)
    losses = Column(INTEGER)
    ties = Column(INTEGER)
    # UniqueConstraint(yearID, round)


class BattingPost(Base):
    __tablename__ = "batting_post"
    __table_args__ = {"schema": "public"}
    # battingPostID = Column(INTEGER, primary_key=True, autoincrement=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    round = Column(VARCHAR(5), primary_key=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    teamID = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
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
    # UniqueConstraint(playerID, yearID, round)


class Fielding(Base):
    __tablename__ = "fielding"
    __table_args__ = {"schema": "public"}
    # fieldingID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4), primary_key=True)
    stint = Column(INTEGER, primary_key=True)
    teamID = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
    lgID = Column(VARCHAR(3))
    POS = Column(VARCHAR(2), primary_key=True)
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
    # UniqueConstraint(playerID, yearID, stint, POS)


class Pitching(Base):
    __tablename__ = "pitching"
    __table_args__ = {"schema": "public"}
    # pitchingID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4), primary_key=True)
    stint = Column(INTEGER, primary_key=True)
    teamID = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
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
    # UniqueConstraint(playerID, stint, yearID)


class PitchingPost(Base):
    __tablename__ = "pitching_post"
    __table_args__ = {"schema": "public"}
    # pitchingPostID = Column(INTEGER, primary_key=True, autoincrement=True)
    playerID = Column(VARCHAR(10), primary_key=True)  # ForeignKey(Master.playerID))
    yearID = Column(VARCHAR(4), primary_key=True)
    round = Column(VARCHAR(5), primary_key=True)
    teamID = Column(VARCHAR(3))  # ForeignKey(Teams.teamID))
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
    # UniqueConstraint(round, playerID, yearID)


def create_models(engine):
    print("dropping tables")
    Base.metadata.drop_all(engine)
    print("creating tables")
    Base.metadata.create_all(engine)