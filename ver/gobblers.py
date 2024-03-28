#!/bin/python3

class Gobbler:
    size = 0
    player_id = 0

    def __init__(self, player_id, size):
        self.player_id = player_id
        self.size = size
    
    def __gt__(self, other_gob):
        return self.size > other_gob.size if other_gob is not None else True

class Player:
  gobblers = None
  id = None

  def __init__(self, id):
    self.id = id

    self.gobblers = list()
    for i in range(3):
      for j in range(2):
        self.gobblers.append(Gobbler(self.id, i+1))

# Global variables
P1 = Player(1)
P2 = Player(2)
CURRENT_PLAYER = P1

# Init board with empty arrays
board = list()
for x in range(3):
  board.append(list())
  for y in range(3):
    board[x].append(list())

def move_gobbler():
  need_moved = True
  pick_hand = False

  while need_moved:
        
    # Avoid asking when starting game
    pick_hand = True if len(CURRENT_PLAYER.gobblers) == 6 else False

    if not pick_hand:
      res = input("Prends tu le gobbler dans ta main ? (Oui ou Non) : ").lower()
      pick_hand = True if res == "oui" else False

    if pick_hand and len(CURRENT_PLAYER.gobblers):
      gobbler_src_size = int(input("Quelle taille veux tu prendre des gobblers de ta main ? (1, 2 ou 3) : "))
      gobbler_src = None

      # Get gobbler from hand
      for i in range(len(CURRENT_PLAYER.gobblers) - 1):
        if CURRENT_PLAYER.gobblers[i].size == gobbler_src_size:
          gobbler_src = CURRENT_PLAYER.gobblers.pop(i)
          break
    else:
      x_src = int(input("Depuis quelle colonne veux tu le prendre ? (x) : "))
      y_src = int(input("Depuis quelle ligne veux tu le prendre ? (y) : "))

      gobbler_src = board[x_src][y_src].pop() if len(board[x_src][y_src]) else None

    # Get dest coord
    x_dest = int(input("Sur quelle colonne veux tu le placer ? (x) : "))
    y_dest = int(input("Sur quelle ligne veux tu le placer ? (y) : "))

    # Check if we can drop the gobbler on destination
    if gobbler_src > get_top_gobbler(x_dest, y_dest):
      need_moved = False
      board[x_dest][y_dest].append(gobbler_src)

    # let's undo this
    else:
      print("Tu ne peux pas poser ce gobbler ici, réessaye")
      if pick_hand:
        CURRENT_PLAYER.gobblers.append(gobbler_src)
      else:
        board[x_src][y_src].append(gobbler_src)

def get_top_gobbler(x, y):
  cell = board[x][y]
  return cell[len(cell) - 1] if len(cell) else None

def switch_current_player():
  global CURRENT_PLAYER 

  if CURRENT_PLAYER.id == P1.id:
    CURRENT_PLAYER = P2
  else:
    CURRENT_PLAYER = P1


# Check for a winner
def has_winner():
  win = None

  # Checking rows
  for x in range(3):
    win = True
    for y in range(3):
      gobbler = get_top_gobbler(x, y)
      if gobbler:
        if get_top_gobbler(x, y).player_id != CURRENT_PLAYER.id:
          win = False
          break
      else:
        win = False
    if win:
      return win

    # checking columns
    for x in range(3):
      win = True
      for y in range(3):
        gobbler = get_top_gobbler(x, y) 
        if gobbler:
          if get_top_gobbler(y, x).player_id != CURRENT_PLAYER.id:
            win = False
            break
        else:
          win = False
      if win:
        return win

    # checking diagonals
    win = True
    for x in range(3):
      gobbler = get_top_gobbler(x, y) 
      if gobbler:
        if get_top_gobbler(x, x).player_id != CURRENT_PLAYER.id:
          win = False
          break
      else:
        win = False
    if win:
      return win

    win = True
    for x in range(3):
      gobbler = get_top_gobbler(x, y) 
      if gobbler:
        if get_top_gobbler(x, 3 - 1 - x).player_id != CURRENT_PLAYER.id:
          win = False
          break
      else:
        win = False

    return win

def print_board():
  print("Voici le plateau : ")
  for x in range(3):
    line = "|"
    for y in range(3):
      top_gobbler = get_top_gobbler(x, y)
      line += f"{top_gobbler.player_id}{top_gobbler.size}|" if top_gobbler else "--|"
    print(line)
    line = ""

# Main loop
def game():
    
  print("Bienvenue dans Gobblers !")
  print("C'est au joueur 1 de commencer")
  print("Que le meilleur gagne !")

  while True:
    print(f"\nC'est au tour du jouer {CURRENT_PLAYER.id}")
    print_board()
    move_gobbler()

    if has_winner():
      break

    switch_current_player()

  print(f"Bravo player {CURRENT_PLAYER.id} ! Tu as gagné !")

def main():
  game()

if __name__ == "__main__":
  main()

