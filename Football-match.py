import csv

wc22 = {
    "A": ["Ecuador", "Netherlands", "Qatar", "Senegal"],
    "B": ["England", "Iran", "USA", "Wales"],
    "C": ["Argentina", "Mexico", "Poland", "Saudi Arabia"],
    "D": ["Australia", "Denmark", "France", "Tunisia"],
    "E": ["Costa Rica", "Germany", "Japan", "Spain"],
    "F": ["Belgium", "Cnada", "Croatia", "Morocco"],
    "G": ["Brazil", "Cameroon", "Serbia", "Switzerland"],
    "H": ["Ghana", "Portugal", "Korea Republic", "Uruguay"],
}

# Format of the list
# [Number of matches played-0, Number of Wins-1, Number of Draws-2, Number of Losses-3, Number of goals scored-4, Number of goals conceded-5, Goal Difference-6, Number of points-7]
# In short
# [MP,W,D,L,GF,GA,GD=GF-GA,Pts]
gameResults = {
    "Ecuador": [0, 0, 0, 0, 0, 0, 0, 0],
    "Netherlands": [0, 0, 0, 0, 0, 0, 0, 0],
    "Qatar": [0, 0, 0, 0, 0, 0, 0, 0],
    "Senegal": [0, 0, 0, 0, 0, 0, 0, 0],
    "England": [0, 0, 0, 0, 0, 0, 0, 0],
    "Iran": [0, 0, 0, 0, 0, 0, 0, 0],
    "USA": [0, 0, 0, 0, 0, 0, 0, 0],
    "Wales": [0, 0, 0, 0, 0, 0, 0, 0],
    "Argentina": [0, 0, 0, 0, 0, 0, 0, 0],
    "Mexico": [0, 0, 0, 0, 0, 0, 0, 0],
    "Poland": [0, 0, 0, 0, 0, 0, 0, 0],
    "Saudi Arabia": [0, 0, 0, 0, 0, 0, 0, 0],
    "Australia": [0, 0, 0, 0, 0, 0, 0, 0],
    "Denmark": [0, 0, 0, 0, 0, 0, 0, 0],
    "France": [0, 0, 0, 0, 0, 0, 0, 0],
    "Tunisia": [0, 0, 0, 0, 0, 0, 0, 0],
    "Costa Rica": [0, 0, 0, 0, 0, 0, 0, 0],
    "Germany": [0, 0, 0, 0, 0, 0, 0, 0],
    "Japan": [0, 0, 0, 0, 0, 0, 0, 0],
    "Spain": [0, 0, 0, 0, 0, 0, 0, 0],
    "Belgium": [0, 0, 0, 0, 0, 0, 0, 0],
    "Canada": [0, 0, 0, 0, 0, 0, 0, 0],
    "Croatia": [0, 0, 0, 0, 0, 0, 0, 0],
    "Morocco": [0, 0, 0, 0, 0, 0, 0, 0],
    "Brazil": [0, 0, 0, 0, 0, 0, 0, 0],
    "Cameroon": [0, 0, 0, 0, 0, 0, 0, 0],
    "Serbia": [0, 0, 0, 0, 0, 0, 0, 0],
    "Switzerland": [0, 0, 0, 0, 0, 0, 0, 0],
    "Ghana": [0, 0, 0, 0, 0, 0, 0, 0],
    "Portugal": [0, 0, 0, 0, 0, 0, 0, 0],
    "South Korea": [0, 0, 0, 0, 0, 0, 0, 0],
    "Uruguay": [0, 0, 0, 0, 0, 0, 0, 0],
}

# What is a python statement that prints Morocco on the screen (use the dictionary wc22)
print(wc22["F"][3])
# What is a python statement that prints the number of points of Denmark (use the dictionary gameResults)
print(gameResults["Denmark"][7])
# What is a python statement that prints the number of losses of Qatar (use the dictionary wc22)???
print(gameResults["Qatar"][3])
# What is a python statement that prints the Goal difference for Uruguay (use the dictionary gameResults)
print(gameResults["Uruguay"][6])
# What is a python statement that fixes the typo in group F, replacing Cnada with Canada (use the dictionary wc22)
wc22["F"][1] = "Canada"


# Write the code of the function printGroup This function creates and returns a string which is the  html table that
# displays the group name and each member of the group name if name is not a valid group, an error message is displayed
# Example string returned if name="A":<table><tr><th>Group
# A</th></tr><tr><td>Ecuador</td></tr><tr><td>Netherlands</td></tr><tr><td>Qatar</td></tr><tr><td>Senegal</td></tr
# ></table>


def printGroup(key):
    try:
        output = "<table><tr><th>{}</th></tr><tr><td>{}</td></tr><tr><td>{}</td></tr><tr><td>{}</td></tr><tr><td>{}</td></tr></table>".format(
            key, wc22[key][0], wc22[key][1], wc22[key][2], wc22[key][3])

        return output
    except KeyError as e:
        print("provide valid group name")


# Write the code of the function testprintGroup
# This function tests the function printGroup:
# - prompts the user for a group name
# - calls the function to create the html string
# - Saves the string into a file name.html where name is the group name: A to G
# - function starts again until the user presses "N"
def testprintGroup():
    while True:
        key = input("please Enter Group name (N to exit):")
        if key == "N":
            break
        html_content = printGroup(key)
        if html_content:
            with open('{}.html'.format(key), 'w') as f:
                f.write(html_content)
            break


# Write the code of the function saveGame
#
# Note that knowing the function signature, you may start doing the next function and come back to this one later
#
# This function receives the result of the game as a string with the following format
# Group, Country1: GoalsScored, Country2: GoalsScored
# Example:
# A, Qatar:0, Ecuador:2"
# the function parses the input (hint: use split)
# then updates the dictionary dResult
# [Number of matches played, Number of Wins, Number of Draws, Number of Losses, Number of goals scored, Number of goals conceded, Goal Difference, Number of points]
#
# As an example if gameResult is "A, Qatar:0, Ecuador:2"
# For Qatar:
#   Game Played is incremented by 1
#   Goal against is incremented by 2
#   Loss is incremented by 1
#
# For Ecuador:
#   Game Played is incremented by 1
#   Goal For is incremented by 2
#   Win is incremented by 1
#   Points is incremented by 3
#

def saveGame(data):
    for match in data:
        team_a, score_a = match[1].split(':')
        team_b, score_b = match[2].split(':')
        global gameResults
        gameResults[team_a][0] += 1
        gameResults[team_b][0] += 1
        if int(score_a) > int(score_b):
            gameResults[team_a][1] += 1
            gameResults[team_b][3] += 1
            gameResults[team_a][6] += int(score_a) - int(score_b)
            gameResults[team_b][6] -= int(score_a) - int(score_b)
            gameResults[team_a][7] += 3
        elif int(score_b) > int(score_a):
            gameResults[team_b][1] += 1
            gameResults[team_a][3] += 1
            gameResults[team_b][6] += int(score_b) - int(score_a)
            gameResults[team_a][6] -= int(score_b) - int(score_a)
            gameResults[team_b][7] += 3
        elif int(score_b) == int(score_a):
            gameResults[team_a][2] += 1
            gameResults[team_b][2] += 1
            gameResults[team_a][7] += 1
            gameResults[team_b][7] += 1

        gameResults[team_a][4] += int(score_a)
        gameResults[team_b][5] += int(score_b)
        gameResults[team_b][4] += int(score_b)
        gameResults[team_a][5] += int(score_a)

    return gameResults


# convert gameResult to a list using split

# Extract the first country name and number of goals scored using split

# Extract the second country name and number of goals scored using split

# then updates the dictionary dResult
# [Number of matches played, Number of Wins, Number of Draws, Number of Losses, Number of goals scored, Number of goals conceded, Goal Difference, Number of points]
# [Mp,W,D,L,GF,GA,GD,Pts]
# if second country wins
# update dResult with appropriate values:
# first country: l+=1 GF+=s1 GA+=s2  MP+=1 GD+=s1-s2
# second country: w+=1 GF+=s2 GA+=s1 MP+=1 GD+=s1-s2 pts+=3

# if first country wins
# update dResult with appropriate values:
# first country: W +=1 GF+=s1 GA+=s2 Pts+=3 Mp+=1 GD+=s1-s2
# second country: L+=1 GF+=s2 GA+=s1 Mp+=1 GD+=s1-s2

# if draw
# update dResult with appropriate values:
# first country d+=1 GF+=s1 GA+=s2  MP+=1 GD+=s1-s2 pts+=1
# second country: d+=1 GF+=s2 GA+=s1 MP+=1 GD+=s1-s2 pts+=1


# Write the code of the function readFileResults
# This function receives the file with game results
# It then populates the dictionary dR
# This function makes use of the saveGame function created previously

def readFile(fName, gameResults):
    with open(fName, 'r') as file:
        data = csv.reader(file)
        dResult = saveGame(data)
        return dResult


# Write the code of the function printgameResults
# This function prints on the screen a html table row that contains
# the current results of the country str
# In order the table row displays:
# Match played | Wins | Losses | Draws | Goals For | Goals Against | Goals differential | Points
#
# Example output on screen
# <tr><td>1/td><td>1/td><td>0/td><td>0/td><td>1/td><td>0/td><td>1/td><td>3/td></tr>

def printgameResults(strCountry, gameResults):
    while True:
        con = strCountry
        resultOfCountry = "<table><tr><th>Country Name</th><tr><td>{}</td></tr></tr><tr><th>Match played</th></tr><tr><td>{}</td></tr><tr><th>Wins</th></tr><tr><td>{}</td></tr><tr><th>Losses</th></tr><tr><td>{}</td></tr><tr><th>Draws</th></tr><tr><td>{}</td></tr><tr><th>Goals For</th></tr><tr><td>{}</td></tr><tr><th>Goals Against</th></tr><tr><td>{}</td></tr><tr><th>Goals differential</th></tr><tr><td>{}</td></tr><tr><th>Points</th></tr><tr><td>{}</td></tr></table>".format(
            con, gameResults[0], gameResults[1], gameResults[2], gameResults[3], gameResults[4],
            gameResults[5], gameResults[6], gameResults[7])
        with open('{}.html'.format(con), 'w') as r:
            r.write(resultOfCountry)
        return resultOfCountry


# Write the code of the function printResults
# This function prints on screen a html table that displays the results
# of all the countries in the group.
# It makes calls to the function printgameResults

def printResults(Groupname, gameResults, wc22):
    countrygroup = ''
    showGroup = printGroup(Groupname)
    for country in wc22[Groupname]:
        showCountry = printgameResults(country, gameResults[country])
        countrygroup += showCountry
        with open('groupresult.html', 'w') as r:
            r.write(showGroup + countrygroup)


# This code should work without any modification
printGroup("B")
readFile("results.txt",gameResults)
printgameResults("Tunisia",gameResults["Tunisia"])
printResults("B", gameResults,wc22)




