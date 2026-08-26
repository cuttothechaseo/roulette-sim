# Roulette Simulator

A terminal-based European roulette game built in Python. The current version
supports red and black bets, bankroll tracking, input validation, and repeated
rounds.

## Features

- Spins a European roulette wheel with numbers 0 through 36
- Classifies results as red, black, or green
- Accepts red or black bets
- Validates bet colors and whole-dollar bet amounts
- Prevents bets that are zero, negative, or greater than the current bankroll
- Updates the bankroll after each win or loss
- Continues until the player quits or runs out of money

## Requirements

- Python 3

The project uses only Python's standard library, so no packages need to be
installed.

## Run the Game

From the project directory:

```bash
python3 roulette.py
```

The player begins with a $100 bankroll. Each round, the game asks for a bet
amount and a color, spins the wheel, reports the result, and updates the
bankroll.

## Project Structure

- `roulette.py` — the playable roulette game
- `learning.py` — exercises used to review the Python concepts needed by the game
- `value_flow_practice.py` — focused practice passing returned values between functions
- `LEARNING_STYLE.md` — learning goals and tutoring preferences
- `ROULETTE_PROJECT.md` — the original project roadmap

## What I Practiced

- Functions, parameters, arguments, and return values
- Passing data between cooperating functions
- Separating individual responsibilities from program orchestration
- Lists, sets, loops, and conditionals
- Input validation with `try` and `except`
- Maintaining and updating state across repeated rounds
- Using a `main()` function to coordinate program flow

## Current Scope

Version 1 is intentionally limited to even-money red and black bets on a
European roulette wheel. It is a playable game rather than a full statistical
simulation tool.

Possible future additions include:

- Odd/even, high/low, and straight-up number bets
- Automated simulation mode
- Win/loss percentages and summary statistics
- Strategy comparisons
- American roulette with 0 and 00
