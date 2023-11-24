import random

from art import logo

print(logo)


user_cards = []
computer_cards = []
def deal_cards():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)
  

# Sum Cards
def sum_cards(cards):
  """Inside sum_cards() check for a blackjact (a hand with only 2
  cards: ace + 10) and return 0 instead of the actual score. 
  0 will     represent a blackjack in our game"""
  if sum(cards) >= 0 and sum(cards) < 17:
    cards.append(deal_cards())
  if sum(cards) == 21 and len(cards) == 2:
    return 0 # Blackjack
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)


# Card Function
for _ in range(2):
  user_cards.append(deal_cards())
  computer_cards.append(deal_cards())

# Display cards
print(f'User Cards: {user_cards} = {sum_cards(user_cards)}')
print(f'Computer Cards: {computer_cards[0]},**')

# Total Cards
user_cards_total = sum_cards(user_cards)
computer_cards_total = sum_cards(computer_cards)

if user_cards_total < 17 and user_cards_total >= 0:
  input("Hit another card. Press enter now: ")
  user_cards.append(deal_cards())
  
if computer_cards_total >= 0 and computer_cards_total < 17:
  computer_cards.append(deal_cards())
