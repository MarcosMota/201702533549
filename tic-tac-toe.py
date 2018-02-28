import sys
import time
import getopt

# Verifica se usuario ganhou
def check_board(board):
    profundidade = 0
    board = ''.join(board)
    for i in range(len(board)):
        if board[i] == "_":
            profundidade = profundidade + 1

    print("Profundidade: {}".format(profundidade))
    ganhou(board)
    # Se foi concluido
    if "_" not in board:
        print("concluido")

def ganhou(board):
    list_vitoria = (
        [6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    )

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
        opts, args = getopt.getopt(argv,"hf:b:v",["first=","board=","verbose="])
        for opt, arg in opts:
            if opt == '-h':
                print("%s -f x -b ____x____"%(__file__))
                sys.exit()
            elif opt in ("-v", "--verbose"):
                print_board(board)
                check_board(board)
            elif opt in ("-b", "--board"):
                if len(arg) == 9:
                    board = list(arg)
                else:
                    print("wrong board!")

    except getopt.GetoptError:
        print("%s -f x -b ____x____"%(__file__))
        sys.exit(2)
