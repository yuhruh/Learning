import random

Choice = {
    'r':'rock',
  'p':'paper',
  'sc':'scissors',
  'sp':'spock',
  'l':'lizard'
}

win = {
    'rock': {'scissors', 'lizard'},
    'paper': {'rock', 'spock'},
    'scissors':{'paper', 'lizard'},
    'lizard':{'paper', 'spock'},
    'spock':{'rock', 'scissors'}
    }

def display_result(player, computer): #if player choose is happened to the key then player won, vice versa.
    if computer in win.get(player):
        print "You won!"
    elif player in win.get(computer):
        print "Compuetr won!"
    else:
        print "It's tie."
        
def score(player, computer, p_score, c_score):
    if computer in win.get(player):
        p_score += 1
        if p_score == 5:
            print "You are the winner! Your score achieves 5 first!"
        else:
            print "Your score is {}".format(p_score)
        return p_score
    elif player in win.get(computer):
        c_score += 1
        if c_score == 5:
            print "Computer is the winner! Computer's score achieves 5 first!"
        else:
            print "Computer's score is {}".format(c_score)
        return c_score
    else:
        print "No one scored"
            
player_score = 0
computer_score = 0
while True:
    while True:
        player_choice = raw_input("Which would you like to choose?\nr for rock\np for paper\nl for lizard\nsc for scissors\nsp for spock\n")
        if Choice.has_key(player_choice):
            print "You choose {}".format(Choice[player_choice])
            break
        else:
            print "That's not a valid choice."
        
    computer_choice = random.choice(Choice.keys())
    print "Computer choose {}".format(Choice[computer_choice])
    
    display_result(Choice[player_choice], Choice[computer_choice])
    
    if Choice[computer_choice] in win.get(Choice[player_choice]):
        player_score += 1
        if player_score == 5:
            print "You are the winner! Your score achieves 5 first!"
            break
        else:
            print "Your score is {}".format(player_score)
    elif Choice[player_choice] in win.get(Choice[computer_choice]):
        computer_score += 1
        if computer_score == 5:
            print "Computer is the winner!Computer's score achieves 5 first!"
            break
        else:
            print "Computer's score is {}".format(computer_score)
    else:
        print "No one scored" 
    
    #score(Choice[player_choice], Choice[computer_choice], player_score, computer_score)
        
    answer = raw_input("Do you want to play again?(Y to play again/Press any key to leave)\n")
    if answer.lower() == 'y':
        print "That's do it again!"
    else:
        break
    