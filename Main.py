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
points2 = (wins * 3) + (ties * 2)
summary = f"Team name: {name2} Wins: {wins2} Ties: {ties2} Losses: {losses2} Points: {points2}"
print(summary)

print("Enter the team name?")
name3 = input("Team name: ")
wins3 = int(input("Wins: "))
ties3 = int(input("Ties: "))
losses3 = int(input("Losses: "))
points3 = (wins * 4) + (ties * 3)
summary = f"Team name: {name3} Wins: {wins3} Ties: {ties3} Losses: {losses3} Points: {points3}"
print(summary)

print("Enter the team name?")
name4 = input("Team name: ")
wins4 = int(input("Wins: "))
ties4 = int(input("Ties: "))
losses4 = int(input("Losses: "))
points4 = (wins * 5) + (ties * 4)
summary = f"Team name: {name4} Wins: {wins4} Ties: {ties4} Losses: {losses4} Points: {points4}"
print(summary)

print("Enter the team name?")
name5 = input("Team name: ")
wins5 = int(input("Wins: "))
ties5 = int(input("Ties: "))
losses5 = int(input("Losses: "))
points5 = (wins * 6) + (ties * 5)
summary = f"Team name: {name5} Wins: {wins5} Ties: {ties5} Losses: {losses5} Points: {points5}"
print(summary)

print("Enter the team name?")
name6 = input("Team name: ")
wins6 = int(input("Wins: "))
ties6 = int(input("Ties: "))
losses6 = int(input("Losses: "))
points6 = (wins * 7) + (ties * 6)
summary = f"Team name: {name6} Wins: {wins6} Ties: {ties6} Losses: {losses6} Points: {points6}"
print(summary)

if points > points6:
    points6 = points
    name6 = name

print("\n=== TOURNAMENT STANDING===")
print("team info")

print((f"\nTOP OF THE STANDINGS:{name6} with {points6} Points!"))