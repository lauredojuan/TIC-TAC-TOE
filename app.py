import os

playing_now = "x"

position_board = [
    "1","2","3",
    "4","5","6",
    "7","8","9",
]
board = [
    "_","_","_",
    "_","_","_",
    "_","_","_",
]

def print_board(title):
    print(title)
    print("")
    for i in range(0, len(board)):
            print(board[i]+" ",end = "")
            if i == 2 or i == 5 or i == 8:
                print("")
def print_position_board():
  for i in range(0, len(position_board)):
            print(position_board[i]+" ",end = "")
            if i == 2 or i == 5 or i == 8:
                print("")  
def user_play(position_played):
  if int(position_played) >= 1 and int(position_played) <= 9:
    board[(int(position_played[0]))-1] = "X"

stop = False
while stop == False:
    os.system("clear") 
    print_board("Play or type 'help' for options.")  
    print("") 
    command = ""
    resp = input("Select a position to play_").partition(' ')
    command = resp[0]
    if command == "stop":
      stop = True
    elif command == "reset":
      print("working on it")   
    elif command == "p":
        os.system("clear")
        print_position_board() 
        print("") 
        print_board("Play or type 'help' for options.")
        print("") 
        resp = input("Select a position to play_").partition(' ')
        command = resp[0]
        user_play(command)  
    elif command == "help":
      os.system("clear")
      print_board("")  
      print("changes") 
      print( "Type 'p' to see the positions.")
      print( "Type 'reset' to start a new game.")
      print( "Type 'stop' to exit the game.")
      print( "return to resume game.")
      resp = input("Select an option_").partition(' ')
      command = resp[0]
      # if command == "stop":
      #   stop = True
      # elif command == "p":
      #   os.system("clear")
      #   print_position_board() 
      #   print("") 
      #   print_board("")
      #   print("") 
      #   resp = input("Select a position to play_").partition(' ')
      #   command = resp[0]
      #   user_play(command)
      #   print_board("Play or type 'help' for options.")
    else:
      user_play(command)

    
    
    
