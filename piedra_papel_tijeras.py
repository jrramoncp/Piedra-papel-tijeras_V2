import random
  
def get_winner(player, computer):
    if player == computer:
        return "empate"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        return "jugador"
    else:
        return "computer"

def computer_choice(computer): 
    ''' Elecciones del ordenador'''

    if computer == 1:
        return("Ordenador: Piedra")
    elif computer == 2:
        return("Ordenador: Papel")
    else: 
        return("Ordenador: Tijeras")
    

def game():
    ''' Logica para una partida completa al mejor de 5'''

    # Mensaje de bienvenida
    print("¡Jugemos a Piedra, papel o tijeras. El mejor de 5 gana!")

    

    computer_wins = 0 # Marcador ordenador
    player_wins = 0 # Marcador jugador
    games = 0 # Contador de partidas jugadas

    # Bucle de juegos
    while games != 5:  ## El maximo de juegos es 5

        ## Elecciones del jugador y del ordenador

        computer = random.randint(1,3)
        try:
            player = int(input("Escribe: 1.Piedra | 2.Papel | 3.Tijeras\n"))
        except ValueError:
            print("Por favor escribe una opcion válida")
            continue

        winner = get_winner(player, computer)
        print(computer_choice(computer))
        
        ## Comparativa de elecciones y determinación de quien gana cada ronda
        if winner == "jugador":
            print("El jugador gana la ronda")
            player_wins +=1
        elif winner == "computer":
            computer_wins += 1
        else:
            print("Esto es un empate")
        
        print("MARCADOR")
        print(f"Jugador {player_wins}")
        print(f"Ordenador {computer_wins}")
        games +=1
            
    
    ## Mensaje final con el ganador
    if player_wins > computer_wins:
        print("¡Enhorabuena! Has ganado la partida")
    else: 
        print("¡Que pena! Has perdido")

game()
    