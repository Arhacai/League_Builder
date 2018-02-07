import csv
import random

# Imports a list of players from a cvs file.
def import_players():
	with open('soccer_players.csv', newline='') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		rows = list(filereader)
		for row in rows:
			del row[1]	# Deletes the 'Height' element from list because is not shown on the final exported txt.
		return rows

# Separate experienced from non experienced players
def get_player_by_experience(player):
	if player[1] == "YES":
		experience[0].append(player)
	if player[1] == "NO":
		experience[1].append(player)

# Takes a player randomly from the experience and non_experienced groups and add it to a team up to 6 people max in each one.
def fill_teams_evenly_and_randomly():
	for name, players in teams.items():
		while len(players) < 6:
			players.append(experience[0].pop(experience[0].index(random.choice(experience[0]))))
			players.append(experience[1].pop(experience[1].index(random.choice(experience[1]))))

# Creates a new file called teams.txt where it prints the info about the teams and their players.
def export_teams_to_txt():
	file = open("teams.txt", "w")

	for name, players in teams.items():
		file.write(name + "\n" + "=" * len(name) + "\n")
		for player in players:
			file.write(", ".join(player) + "\n")
		file.write("\n")
	file.close()

# Creates a txt file for each player with relevant info to their guardians.
def welcome_letters():
	for name, players in teams.items():
		for player in players:
			file = open("{}.txt".format("_".join(player[0].split()).lower()), "w")

			file.write("Dear {}:\n\n".format(player[2]))
			file.write("Welcome to the {} team!\n\n".format(name))
			file.write("Please don't forget to bring {} to the soccer court at 17:00 on February 20th.\n\nBest regards.".format(player[0]))
			file.close()


################################
# BEGINING OF THE MAIN SCRIPT #
################################
if __name__ == "__main__":

	# Initialize main variables
	teams = {"Sharks": [], "Raptors": [], "Dragons": []}
	experience = [[], []]

	soccer_players = import_players()

	for player in soccer_players:
		get_player_by_experience(player)

	fill_teams_evenly_and_randomly()
	export_teams_to_txt()
	welcome_letters()