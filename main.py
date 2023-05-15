import getpass

valid_inputs = ("rock", "paper", "scissors")

players = {
  "Taylor": "",
  "Joe": ""
}

def get_input():
  for key in players:
    while True:
      choice = getpass.getpass(f"{key}: ").lower()
      if choice in valid_inputs:
        players[key] = choice
        break
      else:
        print(f"{key}! You chose an invalid option. Try again...")
  
def play():
  p1, p2 = players.values()
  if p1 == p2:
    print("")
  if (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
    for key, value in players.items():
      if value == p1:
        print(f"{key} wins!")
        return
  else:
    for key, value in players.items():
      if value == p2:
        print(f"{key} wins!")
        return
  print("Draw")

def main():
  while True:
    get_input()
    play()


if __name__ == '__main__':
  main()
