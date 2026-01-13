def payoff_matrix(player_move, ai_move, scores):
    if player_move == 'C' and ai_move == 'C':
        scores['player'] +=3
        scores['ai'] +=3
    elif player_move == 'D' and ai_move == 'C':
        scores['player'] += 5
        scores['ai'] += 0
    elif player_move == 'C' and ai_move == 'D':
        scores['player'] += 0
        scores['ai'] += 5
    else:
        scores['player'] += 1
        scores['ai'] += 1


print("---------------------------------------------------------------------") 
print("                    Adaptive Prisoner's Dilemma                      ")
print("---------------------------------------------------------------------") 

total_rounds = int(input("Total number of rounds to play: "))
round_no = 1
scores  ={'player': 0, 'ai': 0}

player_history = []
ai_history = []

while(round_no <= total_rounds):
    print("\nRound ", round_no)
    player_move = input("Enter Your Move (C/D): ").upper()
    if (player_move not in ['C', 'D']):
        print("Invalid Input. Try again.")
        continue  # round does not increase
    
    player_history.append(player_move)

    # --------------- AI Decision Logic ---------------

    # 1. Early exploration (no judgment)
    if (round_no <= 2):  
        ai_move = 'C'
    else:
        count_c = player_history.count('C')
        count_d = player_history.count('D')

        c_rate = count_c / round_no
        d_rate = count_d / round_no


        # 2. Classify player (re-evaluated every round)
        if c_rate >= 0.7:
            player_type = 'C' # C -> Cooperative
        elif d_rate >= 0.7:
            player_type = 'D' # D -> Aggressive / Defect
        else:
            player_type = 'O' # O -> Opportunistic


        # 3. Strategy Selection
        if player_type == 'C':
            ai_move = player_history[-2] # Tit-for-Tat (previous round)

        elif player_type == 'D':
            # punish onlu if recent behaviour supports it
            if player_history[-1] == 'D' and player_history[-2] == 'D':
                ai_move = 'D'
            else:
                ai_move = 'C'  # forgiveness

        else: # Opportunistic
            ai_move = player_history[-2]
        
    ai_history.append(ai_move)

    payoff_matrix(player_move, ai_move, scores)

        
    print("AI Chose: ", ai_move)

    print(f"You total score :{scores['player']}")
    print(f"AI total score :{scores['ai']}")

    round_no += 1


print("\n-------------------- Game Over -------------------")
print("Final Player Score: ", scores['player'])
print("Final AI Score: ", scores['ai'])

cooperation_rate = player_history.count('C') / total_rounds
print("Player Cooperation Rate :", round(cooperation_rate, 2)*100)

if(cooperation_rate >= 0.6):
    print("Trust led to better outcomes 😊")
else:
    print("Aggressive play reduced mutual gains 😟")