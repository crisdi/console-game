import os

# FUNCTIONS #
def display_title_bar():
  # Clears the terminal
  os.system('cls')

  # Display title message
  print("\t-----------------------------------------")
  print("\t----     Welcome to console game     ----")
  print("\t-----------------------------------------")

def get_player_choice():
  # List of choices
  print("\n[1] See a list of players.")
  print("[2] About the game.")
  print("[q] Quit.")

  return input("What would you like to do? ")

def show_players():
  print("\nHere are the people I know.\n")
  for player in players: 
    print(player.title())

def get_new_player():
  new_player = input("\nPlease tell me this players name: ")
  if new_player in players:
    print("\n%s already have this player, thank you anyway." % new_player.title())
  else:
    players.append(new_player)
    print("\nGood job, time to add %s!\n" % new_player.title())

# MAIN #

# Loop where player can choose 
players = []

choice = ''
display_title_bar()
while choice != 'q':

  choice = get_player_choice()

  # Respond to user input
  display_title_bar()
  if choice == "1":
    print("\nHere is the players.\n")
  elif choice == "2":
    print("\nThis game is set to thrill your nerves... Have fun!\n")
  elif choice == "q":
    print("\nThanks for playing, bye!")
  else:
    print("\nWrong input.")
