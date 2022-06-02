t = int(input())

def fox_says():
    recording = input()
    recording_split = recording.split()
    animals_sound = []
    word = ''
    while word != 'what does the fox say?':
        word = input()
        word_split = word.split()
        if word_split[-1] == 'say?': break
        animals_sound.append(word_split[-1])
    for i in animals_sound:
        while i in recording_split: recording_split.remove(i)
    print(' '.join(recording_split))

for i in range(t): fox_says()