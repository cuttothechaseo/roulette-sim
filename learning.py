def summarize_rounds(rounds):
    wins = 0
    losses = 0
    net_change = 0

    for current_round in rounds:
        if current_round["won"] == True:
            wins += 1
            net_change += current_round["amount"]
        else:
            losses += 1
            net_change -= current_round["amount"]

    if net_change > 0:
        status = "Profit"
    elif net_change < 0:
        status = "Loss"
    else:
        status = "Even"

    summary = {
        "Wins": wins,
        "Losses": losses,
        "Net Change": net_change,
        "Status": status,
    }

    return summary


def get_color(number, red_numbers):
    if number in red_numbers:
        return "red"
    elif number == 0:
        return "green"
    else:
        return "black"


def main():
    rounds = [
        {"bet": "red", "amount": 10, "won": True},
        {"bet": "black", "amount": 5, "won": False},
        {"bet": "red", "amount": 20, "won": True},
        {"bet": "odd", "amount": 15, "won": False},
    ]
    summary = summarize_rounds(rounds)
    print(summary)
    red_numbers = [1, 3, 5]
    numbers = [0, 1, 2, 3, 4, 5]
    for number in numbers:
        get_color(number, red_numbers)
    print(number)


if __name__ == "__main__":
    main()
