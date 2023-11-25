"""
BLACKJACK CARD GAME
This game was referenced from - https://games.washingtonpost.com/games/blackjack
"""
import random

from art import logo

print(logo)

# Variable declaration
user_score = 0 
computer_score = 0
user_bank = 1000
comp_bank = 0
user_cards = []
computer_cards = []

def deal_cards():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  random.shuffle(cards)
  return random.choice(cards)
  

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
def compare_score(user_score,computer_score,price):
  global user_bank, comp_bank
  if user_score == computer_score:
    return f'Push, Draw - {user_score} == {computer_score}'
  elif computer_score == 0:
    comp_bank += price
    user_bank -= price
    return 'Lose, Computer has BlackJack'
  elif user_score == 0:
    comp_bank -= price
    user_bank += price
    return 'Win, User has BlackJack'
  elif user_score > 21:
    comp_bank += price
    user_bank -= price
    return 'User went over, You lose'
  elif computer_score > 21:
    comp_bank -= price
    user_bank += price
    return 'Computer went over, User win'
  elif user_score > computer_score:
    comp_bank -= price
    user_bank += price
    return 'User win'
  else:
    comp_bank += price
    user_bank -= price
    return 'Computer Win'

# Bank printing room
def bank_deal():
  price_list = [1,5,25,50,100,500,1000]
  check = False
  while not check:
    price = int(input(f'Enter your deals within {price_list}: \n£'))
    if price in price_list or price <= user_bank:
      check = True
      return price
    else:
      print(f'{price} is not in bank notes')

# Divider
def page_divider():
  print('-'*30)


# Card Starter
def play_game():
  global user_score, computer_score,user_bank,comp_bank

  # Deals
  price = bank_deal()
  game_over = False
  
  # Hand first two cards to player
  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

  # Keep game running
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
  page_divider()
  print(f'User final hand {user_cards}, final score {user_score}')
  print(f'Computer final hand {computer_cards}, final score {computer_score}')
  result = compare_score(user_score,computer_score,price=price)
  print(result)
  page_divider()
  page_divider()
  print(f'User Bank Balance: £{user_bank}')
  

  # Divider
  page_divider()
  restart = input('Restart the game, Type "Y" or "N": ').lower().strip()
  if restart == 'y' and user_bank > 0:
    user_cards.clear()
    computer_cards.clear()
    user_score = computer_score = 0
    play_game()
  elif restart == 'n':
    print('Goodbye')
  else:
    print('Low Bank balance, house wins')

play_game()

