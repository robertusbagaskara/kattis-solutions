saxophone = {
    'c': [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    'd': [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    'e': [0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    'f': [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    'g': [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    'a': [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'b': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'C': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'D': [1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    'E': [1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    'F': [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    'G': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    'A': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'B': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
}

def recordFinger(music):
    presentNote = [0 for i in range(10)]
    counter = [0 for i in range(10)]
    for note in music:
        for finger in range(10):
            if presentNote[finger] == 0 and saxophone[note][finger]==1:
                counter[finger] += 1
            presentNote[finger] = saxophone[note][finger]
    return counter

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        music = input()
        print(" ".join(str(i) for i in recordFinger(music)))