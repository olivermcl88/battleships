import csv
from src.ReadCSVFile import ReadCSVFile

class SignUp:
    def __init__(self):
        self.reader = ReadCSVFile()

    def get_password(self, username):
        file_data = self.reader.get_file_data("players.csv")
        for row in file_data:
            if row[0] == username:
                return row[3]  # Return the password associated with the username address
        return None  # Return None if username address not found

    def sign_up(self):
        username = input("Enter your username: ")

        # Check if the username already exists
        if self.get_password(username):
            print("Username already exists. Please choose another one.")
            return

        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        password = input("Enter your password: ")


        # Open the players.csv file in append mode
        with open('resource/players.csv', mode='a', newline='') as file:
            # Create a CSV writer object
            writer = csv.writer(file)

            # Write the new player data to the CSV file
            writer.writerow([username, first_name, last_name, password])    

        print("Sign up successful!")