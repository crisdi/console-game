import os 
import Player

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

choice = ''
display_title_bar()

while choice != 'q':

  choice = get_input()

  # REspond to user input
  display_title_bar()
  if choice == "1":
    print("\nAttack!\n")
  elif choice == "2":
    print("\nFlee.\n")
  elif choice == "q":
    print("\nThanks for playing, bye!")
  else:
    print("\nWrong input.")
