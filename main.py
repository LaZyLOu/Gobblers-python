#!/bin/python3
from colorama import Fore, init

init()

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

  def __init__(self, id, player, color):
    self.id = id
    self.player = player
    self.color = color

    self.gobblers = list()
    for i in range(3):
      for j in range(2):
        self.gobblers.append(Gobbler(self.id, i+1))

# Variables
P1 = Player(1, "Bleu", Fore.CYAN)
P2 = Player(2, "Jaune", Fore.YELLOW)
CURRENT_PLAYER = P1

# Initialisation du plateau vide
board = list()
for x in range(3):
  board.append(list())
  for y in range(3):
    board[x].append(list())

def move_gobbler():
  need_moved = True
  pick_hand = False

  while need_moved:
        
    # Evite de demander au premier tour
    pick_hand = True if len(CURRENT_PLAYER.gobblers) == 6 else False

    if not pick_hand:
      res = input("Prends tu le gobbler dans ta main ? (Oui ou Non) : ").lower()
      pick_hand = True if res == "oui" else False

    if pick_hand and len(CURRENT_PLAYER.gobblers):

      while True:
        gobbler_src_size = int(input("Quelle taille veux tu prendre des gobblers de ta main ? (1, 2 ou 3) : "))

        if gobbler_src_size > 3 or gobbler_src_size < 1:
          continue

        else:
          break   

      gobbler_src = None
        
        ################################################

      # Récupérer le gobbler depuis sa main
      for i in range(len(CURRENT_PLAYER.gobblers) - 1):
        if CURRENT_PLAYER.gobblers[i].size == gobbler_src_size:
          gobbler_src = CURRENT_PLAYER.gobblers.pop(i)
          break
    else:
        # Récupérer le gobbler depuis le plateau
      x_src = int(input("Depuis quelle colonne veux tu le prendre ? (x) : "))
      y_src = int(input("Depuis quelle ligne veux tu le prendre ? (y) : "))

        #Get gobbler
      gobbler_src = board[x_src][y_src].pop() if len(board[x_src][y_src]) else None

    ##############################################################
    
    # Placer le gobbler sur le plateau
    x_dest = int(input("Sur quelle colonne veux tu le placer ? (x) : "))
    y_dest = int(input("Sur quelle ligne veux tu le placer ? (y) : "))

    # Vérifier que l'on peut poser le gobbler à cet emplacement
    if gobbler_src > get_top_gobbler(x_dest, y_dest):
      need_moved = False
      board[x_dest][y_dest].append(gobbler_src)

    # On recommence
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


# Vérifier s'il y a un arrangement gagnant
def has_winner():
  win = None

  # Vérifier les lignes
  for x in range(3):
    win = True
    for y in range(3):
      gobbler = get_top_gobbler(x, y)
      if get_top_gobbler(x, y) != None:
        if get_top_gobbler(x, y).player_id != CURRENT_PLAYER.id:
          win = False
          break
      else:
        win = False
    if win:
      return win

    # Vérifier les colonnes
    for x in range(3):
      win = True
      for y in range(3):
        gobbler = get_top_gobbler(x, y) 
        if get_top_gobbler(y, x) != None:
          if get_top_gobbler(y, x).player_id != CURRENT_PLAYER.id:
            win = False
            break
        else:
          win = False
      if win:
        return win

    # Vérifier les diagonales
    win = True
    for x in range(3):
      gobbler = get_top_gobbler(x, y) 
      if get_top_gobbler(x, x) != None:
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
      if get_top_gobbler(x, 3 - 1 - x) != None:
        if get_top_gobbler(x, 3 - 1 - x).player_id != CURRENT_PLAYER.id:
          win = False
          break
      else:
        win = False

    return win

def print_board():
  print(" Voici le plateau : \n")
  for x in range(3):
    line = "|"
    for y in range(3):
      top_gobbler = get_top_gobbler(x, y)

      player_ = ""
      
      try:
        gobbler = [top_gobbler.player_id, top_gobbler.size]

        if gobbler[0] == 1:
          player_ = Fore.CYAN + str(gobbler[1]) + Fore.RESET
          

        elif gobbler[0] == 2:
          player_ = Fore.YELLOW + str(gobbler[1]) + Fore.RESET
        
      except:
        pass   
      
      line += f"\t{player_}\t|" if top_gobbler else "\t-\t|"

    print(line)
    line = ""
    
# Programme principal
def game():
    
  print("Bienvenue dans Gobblers !")
  print(f"C'est au joueur {CURRENT_PLAYER.color + CURRENT_PLAYER.player + Fore.RESET} de commencer")
  print("Que le meilleur gagne !")

  while True:

    print(f"\nC'est au tour du joueur {CURRENT_PLAYER.color + CURRENT_PLAYER.player + Fore.RESET}")
    move_gobbler()
    print_board()
    
    
    if has_winner():
      break

    switch_current_player()


  print(f"Bravo player {CURRENT_PLAYER.color + CURRENT_PLAYER.player + Fore.RESET} ! Tu as gagné !")

def main():
  game()

if __name__ == "__main__":
  
  try:
    main()

  except KeyboardInterrupt:
    exit()
