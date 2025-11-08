def calculate(playerCount, caseCount):
    playerData = {}
    totalGames = caseCount * playerCount * (playerCount - 1) // 2
    
    for _ in range(totalGames):
        stringCase = input().strip()
        if not stringCase:
            continue
            
        splittedString = stringCase.split()
        if len(splittedString) < 4:
            continue
            
        player1Name = splittedString[0]
        player1Choice = splittedString[1]
        player2Name = splittedString[2]
        player2Choice = splittedString[3]
        
        # Initialize players
        if player1Name not in playerData:
            playerData[player1Name] = [0, 0]  # [win, lose]
        if player2Name not in playerData:
            playerData[player2Name] = [0, 0]
        
        # Game logic
        if player1Choice == player2Choice:
            continue
        elif (player1Choice == "rock" and player2Choice == "scissors") or \
            (player1Choice == "scissors" and player2Choice == "paper") or \
            (player1Choice == "paper" and player2Choice == "rock"):
            playerData[player1Name][0] += 1
            playerData[player2Name][1] += 1
        else:
            playerData[player1Name][1] += 1
            playerData[player2Name][0] += 1
    
    # output all player 1..playerCount
    for i in range(1, playerCount + 1):
        player_id = str(i)
        if player_id in playerData:
            wins, losses = playerData[player_id]
            total = wins + losses
            if total == 0:
                print("-")
            else:
                print(f"{wins/total:.3f}")
        else:
            print("-")
    
    print()

def main():
    while True:
        try:
            userInput = input().strip()
            if userInput == '0':
                break
            if userInput:
                n, k = map(int, userInput.split())
                calculate(n, k)
        except EOFError:
            break

if __name__ == "__main__":
    main()