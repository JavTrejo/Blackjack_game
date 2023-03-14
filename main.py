import random

Cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def get_cards(user):
    """Gets two random cards for the user"""
    for i in range(2):
        i = random.choice(Cards)
        user.append(i)
    return user


def add_cards(cards):
    """Adds the total value of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def check_amount(bet, money_left):
    """Checks if you put a valid bet amount"""
    if bet > money_left:
        print(f"Your betting more than what you have in your current bankroll place a smaller bet")
        want_to_play()


def compare_hands(player, dealer):
    """Compares the hand between the player and the dealer"""

    if player > 21 and dealer > 21:
        return f"You went over twenty-one your total was {player} you lose"
    elif player == dealer == 0:
        return "Both you and the dealer have a blackjack it's a draw"
    elif player == dealer:
        return f"Both you and the dealer got {player} it's a draw"
    elif dealer == 0:
        return f"Dealer has a blackjack you have {player} you lose"
    elif player == 0:
        return f"You have a blackjack you win"
    elif player > 21:
        return f"You went over twenty-one your total was {player} you lose"

    elif dealer > 21:
        return f"Dealer total is {dealer} your total is {player} you win "

    elif dealer > player:
        return f"You lose your total is {player} versus the dealer's total {dealer}"
    else:
        return f"You win your total is {player} versus the dealer's total {dealer}"


Current_Bankroll = 100

bet_amount = 0


def want_to_play():
    global Current_Bankroll, bet_amount
    player_cards = []
    dealer_cards = []
    player_cards = get_cards(player_cards)
    dealer_cards = get_cards(dealer_cards)
    player_total = add_cards(player_cards)
    dealer_total = add_cards(dealer_cards)
    while dealer_total < 17:
        if dealer_total == 0:
            break
        dealer_cards.append(random.choice(Cards))
        dealer_total = add_cards(dealer_cards)
        if dealer_total >= 17:
            break

    print(f"Your current bankroll is {Current_Bankroll}")
    if Current_Bankroll == 0:
        print("You have no more money in your bankroll game over")
        exit()
    while True:
        try:
            bet_amount = int(input("How much do you want to bet? "))
        except ValueError:
            print("Must put a whole number")
            continue
        else:
            break

    check_amount(bet_amount, Current_Bankroll)

    print(
        f"Your cards are {player_cards}, your total is {sum(player_cards)} \ndealers first card is a {dealer_cards[0]}")
    double = True
    max_bet = bet_amount * 2
    if max_bet > Current_Bankroll:
        double = False

    while double:
        double_down = input("would you like to double down?:'y' or 'n' ").lower()
        if double_down == 'y':
            bet_amount *= 2
            player_cards.append(random.choice(Cards))
            player_total = add_cards(player_cards)
            print(f"Your new cards are {player_cards} your new total is {player_total}")
            print(compare_hands(player_total, dealer_total))
            if "win" in compare_hands(player_total, dealer_total):
                Current_Bankroll += bet_amount
            elif "draw" in compare_hands(player_total, dealer_total):
                Current_Bankroll += 0
            else:
                Current_Bankroll -= bet_amount
            keep_playing = input("Do you want to play a game of Blackjack:? 'y' or 'n' ").lower()
            if keep_playing == 'y':
                want_to_play()
            else:
                quit()

        elif double_down == 'n':
            double = False
        else:
            print("Invalid answer starting a new round")
            want_to_play()
    hit = True
    while hit:
        extra_card = input("Do you want to hit?: 'y' or 'n' ").lower()
        if extra_card == 'y':
            player_cards.append(random.choice(Cards))
            player_total = add_cards(player_cards)

            if player_total > 21:
                break
            print(f"Your new cards are {player_cards} your new total is {player_total}")
        elif extra_card == 'n':
            hit = False
        else:
            print("Invalid answer starting a new round")
            want_to_play()
    print(compare_hands(player_total, dealer_total))
    if "win" in compare_hands(player_total, dealer_total):
        Current_Bankroll += bet_amount
    elif "draw" in compare_hands(player_total, dealer_total):
        Current_Bankroll += 0
    else:
        Current_Bankroll -= bet_amount
    keep_playing = input("Do you want to play a game of Blackjack:? 'y' or 'n' ").lower()
    if keep_playing == 'y':
        want_to_play()
    else:
        quit()


while input("Do you want to play a game of Blackjack:? 'y' or 'n' ").lower() == 'y':
    want_to_play()
