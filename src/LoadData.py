from src.ReadCSVFile import *
from src.Player import Player


class PlayerLoad:

    def get_raw_player(self):
        read_csv_file = ReadCSVFile()
        player_data = read_csv_file.get_file_data("players.csv")
        return player_data

    def load_players(self):
        players = []
        raw_player_data = self.get_raw_player()
        for player in raw_player_data:
            players.append(Player(player))
        return players

    def format_players(self):
        display = ""
        players = self.load_players()
        for player in players:
            display += player.get_name() + "\n"
        return display

if __name__ == '__main__':
    player_load = PlayerLoad()
    print(player_load.format_players())