def summarize_rounds():
    wins = 0
    losses = 0
    net_change = 0
    rounds = [
        {"bet": "red", "amount": 10, "won": True},
        {"bet": "black", "amount": 5, "won": False},
        {"bet": "red", "amount": 20, "won": True},
        {"bet": "odd", "amount": 15, "won": False},
    ]

    for current_round in rounds:
        if current_round["won"] == True:
            wins += 1
            net_change += current_round["amount"]
        elif current_round["won"] == False:
            losses += 1
            net_change -= current_round["amount"]

    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Net Change: ${net_change}")


def main():
    summarize_rounds()


if __name__ == "__main__":
    main()
