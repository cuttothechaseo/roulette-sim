import random

RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}


def spin_wheel():
    spun_number = random.randint(0, 36)
    return spun_number


def get_color(number):
    if number in RED_NUMBERS:
        return "red"
    elif number == 0:
        return "green"
    else:
        return "black"


def is_winning_color_bet(bet_color, result_color):
    if bet_color == result_color:
        return True
    else:
        return False


def get_bet_color():
    valid_colors = ["red", "black"]

    while True:
        bet_color = input("Bet on red or black:").lower()
        if bet_color in valid_colors:
            return bet_color
        else:
            print("Please choose red or black:")


def get_bet_amount(bankroll):
    while True:
        try:
            bet_amount = int(input(f"You have {bankroll}: Enter your bet:"))
            if bet_amount <= 0:
                print("Your bet must be greater than 0.")
            elif bet_amount > bankroll:
                print("Your bet must not exceed your bankroll.")
            else:
                return bet_amount
        except ValueError:
            print("Invalid bet. Please enter a whole number.")


def update_bankroll(bankroll, bet_amount, bet_won):
    if bet_won is True:
        bankroll += bet_amount
        return bankroll
    else:
        bankroll -= bet_amount
        return bankroll


def play_round(bankroll):
    bet_amount = get_bet_amount(bankroll)
    bet_color = get_bet_color()
    spun_number = spin_wheel()
    result_color = get_color(spun_number)
    bet_won = is_winning_color_bet(bet_color, result_color)
    print(f"Bet: {bet_color}")
    print(f"The wheel landed on {spun_number} {result_color}")
    if bet_won is True:
        print("You won!")
    else:
        print("You lost.")
    bankroll = update_bankroll(bankroll, bet_amount, bet_won)
    return bankroll


def get_play_again():
    valid_response = ["yes", "no"]

    while True:
        response = input("Play again? (Yes/No):").lower()
        if response in valid_response:
            if response == "yes":
                return True
            else:
                return False
        else:
            print("Please choose yes or no.")


def main():
    bankroll = 100
    play_again = True

    while bankroll > 0 and play_again is True:
        bankroll = play_round(bankroll)
        print(f"Bankroll: {bankroll}")
        if bankroll == 0:
            print("Out of money.")
        else:
            play_again = get_play_again()


if __name__ == "__main__":
    main()
