#created team class with name and list.
class NFLTeam:
    def __init__(self, teamName, playersList):
        self.teamName = teamName
        self.playersList = playersList
 #class for playername and position as lists and add players
class Players:
    def __init__(self, playerName, playerPosition):
        self.playerName = []
        self.playerPosition = []
        self.playerName.append(playerName)
        self.playerPosition.append(playerPosition)
#add players
p1 = Players("Joe Montana", "QB")
p2 = Players("Barry Sanders", "RB")
p3 = Players("Jerry Rice", "WR")
p4 = Players("Graham Gano", "K")
#combine them into a list.
playerList = [p1, p2, p3, p4]
#give team name
teamname = NFLTeam("Panther", playerList)
#print
print ("teamname: ", teamname.teamName)
for player in teamname.playersList:
    print(player.playerName, player.playerPosition)
