import csv
from LoadData import PlayerLoad

class WinnersReward:
    def update_user_score(username):
        updated_rows = []
        found = False
        with open('resource/player.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    new_score = int(row[4]) + 50
                    row[4] = str(new_score)
                    found = True
                    print(f"New score for {username}: {new_score}")
                updated_rows.append(row)

        if found:
            with open('resource/player.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)


           