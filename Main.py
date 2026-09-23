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

print("Enter the team name?")
name2 = input("Team name: ")
wins2 = int(input("Wins: "))
ties2 = int(input("Ties: "))
losses2 = int(input("Losses: "))
points2 = (wins * 1) + (ties * 2)
summary = f"Team name: {name2} Wins: {wins2} Ties: {ties2} Losses: {losses2} Points: {points2}"
print(summary)

print("Enter the team name?")
name3 = input("Team name: ")
wins3 = int(input("Wins: "))
ties3 = int(input("Ties: "))
losses3 = int(input("Losses: "))
points3 = (wins * 0) + (ties * 4)
summary = f"Team name: {name3} Wins: {wins3} Ties: {ties3} Losses: {losses3} Points: {points3}"
print(summary)