class TeamMember:
    def __init__(self, name:str, id:str) -> None:
        self.name = name
        self.id = id
    
    def __str__(self) -> str:
        return self.name + " " + self.id
    
    def toString(self) -> str:
        return self.name

def getTeams(fileName):
    try:
        teamsLength = sum(1 for _ in open(fileName))
        teamsRaw = open(fileName, "r")

    except FileNotFoundError:
        print("File Not Found")
        return None

    teams = []
    for i in range(teamsLength):
        teams.append(teamsRaw.readline()[:-2])
    
    return teams

def sortTeams(teams):
    sortedTeams = []
    for i in range(0, len(teams), 2):
        sortedTeams.append(TeamMember(teams[i], teams[i+1]))
    
    return sortedTeams

def displayTeams(teams):
    for i in range(len(teams)):
        print(teams[i].toString())

def compareTeams(team1, team2):
    return team1 == team2

teams = getTeams("BPA Java State 2019/teams.txt")

sortedTeams = sortTeams(teams)

displayTeams(sortedTeams)