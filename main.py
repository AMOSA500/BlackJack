import random

from art import logo

print(logo)

# Variable declaration
user_score = 0 
computer_score = 0
user_ = 0
comp_wins = 0
user_cards = []
computer_cards = []

def deal_cards():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(sorted(cards))
  

# Sum Cards
def sum_cards(cards):
  """Inside sum_cards() check for a blackjact (a hand with only 2
  cards: ace + 10) and return 0 instead of the actual score. 
  0 will     represent a blackjack in our game"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0 # Blackjack
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)


# Compare cards
def compare_score(user_score,computer_score):
  global user_wins, comp_wins
  if user_score == computer_score:
    return f'Push, Draw - {user_score} == {computer_score}'
  elif computer_score == 0:
    comp_wins += 1
    return 'Lose, Computer has BlackJack'
  elif user_score == 0:
    user_wins += 1
    return 'Win, User has BlackJack'
  elif user_score > 21:
    comp_wins += 1
    return 'User went over, You lose'
  elif computer_score > 21:
    user_wins +=1 
    return 'Computer went over, User win'
  elif user_score > computer_score:
    user_wins += 1
    return 'User win'
  else:
    comp_wins += 1
    return 'Computer Win'



# Card Starter
def play_game():
  global user_score, computer_score

  # Hand first two cards to player
  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    
  game_over = False
  while not game_over:
    # Display cards
    print(f'User Cards: {user_cards} = {sum_cards(user_cards)}')
    print(f'Computer Cards: {computer_cards[0]},**')
    
    # Total Cards
    user_score = sum_cards(user_cards)
    computer_score = sum_cards(computer_cards)

    # End game if blackjack is achieved or went over
    if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
      game_over = True
    else:
      user_should_hit = input("y - Hit another card\nn - Pass now: ").lower().strip()
      if user_should_hit == 'y':
        user_cards.append(deal_cards())
      else:
        game_over = True

    # hand computer another card if sum of cards is less 17 but not 0
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_cards())
      computer_score = sum_cards(computer_cards)

  # Display score board
  print(f'User final hand {user_cards}, final score {user_score}')
  print(f'Computer final hand {computer_cards}, final score {computer_score}')
  result = compare_score(user_score,computer_score)
  print(result)

  # Divider
  print('-'*10)
  restart = input('Restart the game, Type "Y" or "N": ').lower().strip()
  if restart == 'y':
    user_cards.clear()
    computer_cards.clear()
    user_score = computer_score = 0
    play_game()
  else:
    print('Goodbye')

play_game()

