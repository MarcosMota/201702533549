import sys
import time
import getopt

# Verifica se usuario ganhou
def check_board(board,jogador):
    profundidade = 0
    board = ''.join(board)
    for i in range(len(board)):
        if board[i] == "_":
            profundidade = profundidade + 1

    print("Profundidade: {}".format(profundidade))

    return ganhou(board,jogador)

# Verifica se o jogador ganhou
def ganhou(board,jogador):
    list_vitoria = (
        [6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    )

    for vitoria in list_vitoria:
        if (board[vitoria[0]] == board[vitoria[1]] == board[vitoria[2]] == jogador) :
            return True

    return False


# Printa o quadro com as jogas
def print_board(board):
    board = ''.join(board)
    if len(board) == 9:
        print("           ")
        for line in range(3):
            line_str = ''
            line_bar = ['','|','|']
            for item in board[line*3:line*3+3]:
                if item.upper() == 'X':
                    line_str += ' X ' + line_bar.pop()
                elif item.upper() == 'O':
                    line_str += ' O ' + line_bar.pop()
                else:
                    line_str += '   ' + line_bar.pop()
            print(line_str)
            if line == 2:
                print("           ")
            else:
                print("-----------")


if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        jogador = ''
        opts, args = getopt.getopt(argv,"hf:b:v",["first=","board=","verbose="])
        for opt, arg in opts:
            if opt == '-h':
                print("%s -f x -b ____x____"%(__file__))
                sys.exit()
            elif opt == '-f':
                jogador = arg

            elif opt in ("-v", "--verbose"):
                print_board(board)
            elif opt in ("-b", "--board"):
                if len(arg) == 9:
                    board = list(arg)
                else:
                    print("wrong board!")

        if check_board(board,jogador):
            print("Parabens voce ganhou!!!")

    except getopt.GetoptError:
        print("%s -f x -b ____x____"%(__file__))
        sys.exit(2)
