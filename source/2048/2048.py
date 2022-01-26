"""
0 -> left -> rotate 0 degrees
1 -> up -> rotate -90 degrees
2 -> right -> rotate -180 degrees
3 -> down -> rotate 90 degrees
"""
def pattern(puzzle):
    for i in range(4):
        puzzle[i] = [x for x in puzzle[i] if x != 0]
        for _ in range(4-len(puzzle[i])):
            puzzle[i].append(0)
    for i in range(4):
        for j in range(3):
            if puzzle[i][j+1] == 0 and j<2: 
                puzzle[i][j+1], puzzle[i][j+2] = puzzle[i][j+2], puzzle[i][j+1]
            if puzzle[i][j] == puzzle[i][j+1]:
                puzzle[i][j] += puzzle[i][j+1] 
                puzzle[i][j+1] = 0
            if puzzle[i][j+1] == 0 and j<2: 
                puzzle[i][j+1], puzzle[i][j+2] = puzzle[i][j+2], puzzle[i][j+1]
    return puzzle

def rotateClockWise(matrix):  # rotate 90 degrees
    return list(zip(*matrix[::-1]))

def rotateCounterClockWise(matrix):  # rotate -90 degrees
    return list(zip(*matrix))[::-1]

def showPuzzle(puzzle):
    for i in range(4):
        for j in range(4):
            print(puzzle[i][j], end=' ')
        print()

def inputPuzzle():
    puzzle = []
    for i in range(4):
        miniPuzzle = []
        input_puzzle = input().split()
        for j in range(4):
            miniPuzzle.append(int(input_puzzle[j]))
        puzzle.append(miniPuzzle)
    patternOption = int(input())
    
    if patternOption == 0:
        showPuzzle(
            pattern(
                puzzle
                )
            )
    elif patternOption == 1:
        showPuzzle(
            rotateClockWise(
                pattern(
                    rotateCounterClockWise(  # rotate -90
                        puzzle
                        )
                    )
                )
            )
    elif patternOption == 2:
        showPuzzle(
            rotateClockWise(
                rotateClockWise(
                    pattern(
                        rotateCounterClockWise(  # rotate -90
                            rotateCounterClockWise(  # rotate -90
                                puzzle
                            )
                        )
                    )
                )
            )
        ) 
    elif patternOption == 3:
        showPuzzle(
            rotateCounterClockWise(
                pattern(
                    rotateClockWise( # rotate +90
                        puzzle
                    )
                )
            )
        )
inputPuzzle()