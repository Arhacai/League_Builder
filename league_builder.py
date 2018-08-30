import csv
import json
import random


class LeagueBuilder:
    """
    This program takes a CSV file that contains 18 children's names, their
    parnet's names, and experance levels.
    The output is a teams.txt file which contains three equally skilled and
    numbered teams along with 18 .txt files with the names of each player.
    These files contain a letter for each parent.
    """
    teams = {"Sharks": [], "Raptors": [], "Dragons": []}

    def __init__(self, run=False):
        """
        Instantiate the class importing players from a csv file.
        It can be run on the fly by passing True to the run argument.
        """
        self.players = self.import_players()
        if run:
            self.run()

    def import_players(self):
        """Imports a list of players from a csv file."""
        with open("soccer_players.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            dump = json.dumps([row for row in reader])
            players = json.loads(dump)
            return players

    def get_players_by_experience(self):
        """Checks if a player is experienced or not."""
        experienced = []
        inexperienced = []
        for player in self.players:
            if player['Soccer Experience'] == "YES":
                experienced.append(player)
            else:
                inexperienced.append(player)
        return experienced, inexperienced

    def get_random_player(self, players):
        """Pops a random player from de player list given as parameter"""
        return players.pop(players.index(random.choice(players)))

    def fill_teams(self):
        """
        Fills teams with the same number of players on each one and the same
        number of experienced and inexperienced players.
        """
        experienced, inexperienced = self.get_players_by_experience()
        for team, team_players in self.teams.items():
            while len(team_players) < 6:
                team_players.append(self.get_random_player(experienced))
                team_players.append(self.get_random_player(inexperienced))

    def export_teams(self):
        """Creates a file that displays the teams and their members."""
        file = open("teams.txt", "w")
        for team, players in self.teams.items():
            file.write(team + "\n" + "=" * len(team) + "\n")
            file.write(
                "Name, Soccer Experience, Guardian Name(s)\n"
            )
            for player in players:
                file.write(player['Name'] + ", ")
                file.write(player['Soccer Experience'] + ", ")
                file.write(player['Guardian Name(s)'] + "\n")
            file.write("\n")
        file.close()

    def write_letters(self):
        """
        Creates a txt file for each player with relevant info
        to their guardians.
        """
        for team, players in self.teams.items():
            for player in players:
                file = open("players/{}.txt".format(
                    "_".join(player['Name'].split()).lower()), "w"
                )
                file.write("Dear {}:\n\n".format(player['Guardian Name(s)']))
                file.write("Welcome to the {} team!\n\n".format(team))
                file.write(
                    "Please don't forget to bring {} to the soccer court at "
                    "20:00 on March 20th.\n\nBest regards.".format(
                        player['Name']
                    )
                )
                file.close()

    def run(self):
        self.fill_teams()
        self.export_teams()
        self.write_letters()


if __name__ == "__main__":

   LeagueBuilder(True)
