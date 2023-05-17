import random
choices = ("Rock", "Paper", "Scissors")
def get_choice():
  for iter, choice in enumerate(choices):
    print(f"{iter + 1}: {choice}.")
  while True:
    choice = input(
      "Choose using corresponding number or type 'Quit' to reset score and quit to menu: ")
    try:
      choice = int(choice) - 1
    except ValueError:
      if choice.upper() == "QUIT":
        menu()
      else:
        print("Please enter an integer")
        continue
    if choice in range(3):
      break
    else:
      print("Please enter an integer within the given range of 1 to 3")
      continue
  return choice
def logic(p1, p2):
  if p1 == p2:
    print(f"Draw! You both chose {choices[p1]}")
    return 0
  elif (p1 == 0 and p2 == 2) or (p1 == 2 and p2 == 1) or (p1 == 1 and p2 == 0):
    print(f"{choices[p1]} beats {choices[p2]}. You won!")
    return "win"
  else:
    print(f"{choices[p2]} beats {choices[p1]}. The computer won.")
    return 'loss'
def play():
  wins, losses, draws = 0, 0, 0
  while True:
    outcome = logic(get_choice(), random.randrange(3))
    if outcome == "win":
      wins += 1
    elif outcome == "loss":
      losses += 1
    else:
      draws += 1
    print(f"Games played: {wins+losses+draws}\nWins: {wins}\nLosses: {losses}")
    if losses != 0:
      print(f"Ratio: {wins/losses}")
    else:
      print(f"W/L Ratio: {wins/(losses+1)}")
def menu():
  input("Welcome to rock paper scissors, press enter to start...")
  play()
if __name__ == '__main__':
  menu()
