

def winnerOrLoser(team1, team2, goal1, goal2):
    winner = ""
    if(goal1 > goal2):
        winner=1
    elif(goal1 < goal2):
        winner=2
    elif(goal1 == goal2):
        winner=None
    return winner

#Compare teams, goals, 2 for win, 1 for even, 0 for loss, make a point list

teams = [["Red","Blue"],["Yellow","Blue"],["Red", "Yellow"]]
goals= [[2,1][1,1],[3,2]]
points =[]

for i in range(0, len(teams)):
    team1=teams[i][0]
    team2=teams[i][1]
    goal1=goals[i][0]
    goal2=goals[i][1]
    winner=winnerOrLoser(team1, team2, goal1, goal2)
 #   if(winner==1):


