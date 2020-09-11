from sqlalchemy import Column, INTEGER, NVARCHAR, TIMESTAMP, ForeignKey, DECIMAL, UniqueConstraint, JSON, \
    FLOAT, VARCHAR, DATE
from database import Base


class Master(Base):
    __tablename__ = "master"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    birthYear = Column(VARCHAR(4))
    birthDay = Column(INTEGER)
    birthCountry = Column(VARCHAR(15))
    birthState = Column(VARCHAR(30))
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
    debut = Column(DATE)
    finalGame = Column(DATE)
    retroID = Column(VARCHAR(10))
    bbrefID = Column(VARCHAR(10))


class AwardsShareManagers(Base):
    __tablename__ = "awardssharemanagers"
    __table_args__ = {"schema": "public"}
    awardID = Column(VARCHAR(20))
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2), primary_key=True)
    playerID = Column(VARCHAR(10), primary_key=True)
    pointsWon = Column(INTEGER)
    pointsMax = Column(INTEGER)
    votesFirst = Column(INTEGER)


class AllStarFull(Base):
    __tablename__ = "allstarfull"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    gameNum = Column(INTEGER)
    teamID = Column(VARCHAR(3))
    lgID = Column(VARCHAR(3))
    GP = Column(INTEGER)
    startingPOS = Column(INTEGER)


class AwardsManagers(Base):
    __tablename__ = "awardsmanagers"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    awardID = Column(VARCHAR(30), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2))
    tie = Column(VARCHAR(1))
    notes = Column(VARCHAR(3))


class AwardsPlayers(Base):
    __tablename__ = "awardsplayers"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    awardID = Column(VARCHAR(30), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2))
    tie = Column(VARCHAR(1))
    notes = Column(VARCHAR(3))


class AwardsSharePlayers(Base):
    __tablename__ = "awardsshareplayers"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    awardID = Column(VARCHAR(20), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    lgID = Column(VARCHAR(2))
    pointsWon = Column(INTEGER)
    pointsMax = Column(INTEGER)
    votesFirst = Column(INTEGER)


class Batting(Base):
    __tablename__ = "batting"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    stint = Column(INTEGER)
    teamID = Column(VARCHAR(3))
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


class Salaries(Base):
    __tablename__ = "salaries"
    __table_args__ = {"schema": "public"}
    yearID = Column(VARCHAR(4), primary_key=True)
    teamID = Column(VARCHAR(3))
    lgID = Column(VARCHAR(2))
    playerID = Column(VARCHAR(10), primary_key=True)
    salary = Column(INTEGER)


class FieldingOF(Base):
    __tablename__ = "fieldingOF"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    stint = Column(INTEGER)
    glf = Column(INTEGER)
    gcf = Column(INTEGER)
    grf = Column(INTEGER)


class HallofFame(Base):
    __tablename__ = "halloffame"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    votedBy = Column(VARCHAR(20))
    ballots = Column(INTEGER)
    needed = Column(INTEGER)
    votes = Column(INTEGER)
    inducted = Column(VARCHAR(1))
    category = Column(VARCHAR(10))
    needed_note = Column(VARCHAR(10))


class Managers(Base):
    __tablename__ = "managers"
    __table_args__ = {"schema": "public"}
    playerID = Column(VARCHAR(10), primary_key=True)
    yearID = Column(VARCHAR(4), primary_key=True)
    votedBy = Column(VARCHAR(20))
    ballots = Column(INTEGER)
    needed = Column(INTEGER)
    votes = Column(INTEGER)
    inducted = Column(VARCHAR(1))
    category = Column(VARCHAR(10))
    needed_note = Column(VARCHAR(10))


def create_models(engine):
    # print("dropping tables")
    # Base.metadata.drop_all(engine)
    print("creating tables")
    Base.metadata.create_all(engine)
