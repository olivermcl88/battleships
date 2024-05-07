from LoadData import PlayerLoad
from SignUp import SignUp
class LogIn:
    def get_password(self,username):
        playerLoad = PlayerLoad()
        players = playerLoad.load_players()
        password = ""
        counter = 0
        while password == "" and counter < len(players):
            if username == players[counter].get_username():
                password = players[counter].password
            counter += 1
        return password

    def log_in(self):
        option = input("\nAre you an existing user? 'Y' or 'N'\n------------------------\n")

        while option.upper() != "Y" and option.upper() != "N":
            print("Invalid option. Please try again.")
            option = input("\nAre you an existing user? 'Y' or 'N'\n------------------------\n")

        if option.upper() == "N":
            SignUp().sign_up()
        
        return self.log_in_function()


    def log_in_function(self):
        username = input("Username: ")
        password = self.get_password(username)
        if password == "":
            print("You are not a user.")
            return 0
        else:
            if input("Password: ") == password:
                print("\nLogging in...")
                print("\nWelcome, " + username)
                self.username = username
                return 1
            else:
                return 0
    
    def __init__(self):
        self.username = None
    
    def get_username(self):
        return self.username
