eye = input()
bars = eye.split('()')
print("correct" if len(bars[0])==len(bars[1]) else "fix")