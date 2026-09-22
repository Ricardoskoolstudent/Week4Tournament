#############################################
# Name: Ricardo Camilo
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
print("Enter the team name?")
name = input("Team name: ")
wins = int(input("Wins: "))
ties = int(input("Ties: "))
losses = int(input("Losses: "))
points = (wins * 2) + (ties * 1)
summary = f"Team name: {name} Wins: {wins} Ties: {ties} Losses: {losses} Points: {points}"
print(summary)
if 20 > 1:
    max_points = points
top_team_name = name