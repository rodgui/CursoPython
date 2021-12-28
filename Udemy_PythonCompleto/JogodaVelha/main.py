from IPython.display import clear_output
import random

# Variáveis globais
board = [' '] * 10
game_state = True
announce = ''

# Nota: o jogo ignorará o índice 0
def reset_board():
    global board,game_state
    board = [' '] * 10
    game_state = True

def display_board(board):
    ''' Esta função imprime o tabuleiro de modo que o numpad possa ser usado como uma referência '''
    clear_output()
    #Xprint('   |   |')
    print('1. ' + board[1] + ' |2. ' + board[2] + ' |3. ' + board[3])
    #print('   |   |')
    print('-----------')
    #print('   |   |')
    print('4. ' + board[4] + ' |5. ' + board[5] + ' |6. ' + board[6])
    #print('   |   |')
    print('-----------')
    #print('   |   |')
    print('7. ' + board[7] + ' |8. ' + board[8] + ' |9. ' + board[9])
    #print('   |   |')

def player_input():
    '''Seleciona quem será X ou O'''
    clear_output()
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Você quer ser X ou O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    ''' Marca posição no board'''
    board[position] = marker

def win_check(board,mark):
    ''' Check Horizontals,Verticals, and Diagonals for a win '''
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # vitória pelo topo
    (board[4] == mark and board[5] == mark and board[6] == mark) or # pelo meio
    (board[1] == mark and board[2] == mark and board[3] == mark) or # por baixo
    (board[7] == mark and board[4] == mark and board[1] == mark) or # pela esquda
    (board[8] == mark and board[5] == mark and board[2] == mark) or # pelo meio
    (board[9] == mark and board[6] == mark and board[3] == mark) or # pela direita
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = input('Escolha sua jogada: (1-9) ')
    return int(position)

def replay():
    return input('Quer jogar novamente? "SIM(s) ou NAO(n)" ').lower().startswith('s')

clear_output()
print('\n \n Bem vindo ao jogo da velha \n\n')

while True:
    # Resetao tabuleiro
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('\n \n \n'+ turn + ' começa! \n\n\n')
    game_on = True

    while game_on:
        # Vez do jogador 1
        if turn == 'Player 1':           
            display_board(theBoard)
            print('\n-- Vez Player 1 --\n ')
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            # Checar vitória do jogador 1
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('\n Parabéns! Você venceu! \n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Empate!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Vez do jogador 2
            
            display_board(theBoard)
            print('\n-- Vez Player 2 --\n ')
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            # Checar vitória do jogador 2
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('\n Player 2 venceu! \n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Empate')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break