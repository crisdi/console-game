import os 
import Player
import Enemy

player = Player

# FUNCTIONS #
def display_title_bar():
  # Clears the terminal
  os.system('cls')

  # Display title message
  print("\t-----------------------------------------")
  print("\t----     Welcome to console game     ----")
  print("\t-----------------------------------------")

def get_input():
  # List of choices
  print("\n[1] Attack.")
  print("[2] Flee.")
  print("[q] Quit.")

  return input("Choose an action")

# MAIN #
choice = ''
display_title_bar()

while choice != 'q':

  choice = get_input()

  # Respond to user input
  display_title_bar()
  if choice == "1":
    
    playerDamage = Player.dealDamage()
    print("You attack enemy for " + str(playerDamage) + " damage")
    Enemy.takeDamage(playerDamage)

  elif choice == "2":

    print("\nFlee.\n")

  elif choice == "q":

    print("\nThanks for playing!")

  else:
    
    print("\nWrong input.")
