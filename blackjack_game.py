import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if c_score == u_score:
        return "Draw."
    elif c_score == 0:
        return "You lose. Computer has a blackjack."
    elif u_score == 0:
        return "You win, you have a blackjack."
    elif c_score > 21:
        return "You win, computer went over."
    elif u_score > 21:
        return "You went over, you lose."
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose"

def run_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    game_end = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_end:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"These are your cards: {user_cards} and your score is: {user_score}")
        print(f"This is the computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            user_choice = input("Do you want to draw another card? Type 'y' for yes or 'n' for no. ").lower()
            if user_choice == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand was: {user_cards} and the score was: {user_score}")
    print(f"The computer's hand was: {computer_cards} and the score was: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no. ").lower() == "y":
    print("\n" * 20)
    run_game()


