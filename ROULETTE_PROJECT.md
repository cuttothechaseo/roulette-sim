# ROULETTE_PROJECT.md

## Project Overview

Build a terminal-based roulette simulator in Python.

The project should begin as a playable roulette game and later evolve into a simulation tool that can run many roulette spins automatically and analyze betting strategies.

This is a learning project, so the implementation should remain simple and understandable before becoming more sophisticated.

## Core Project Idea

The program should eventually be able to:

- simulate a roulette wheel spin
- allow a player to place simple bets
- determine whether the bet wins or loses
- calculate payouts
- update a bankroll
- repeat for multiple rounds
- simulate many rounds automatically
- track results
- calculate summary statistics

## Recommended Scope

Start with European roulette for simplicity:

- numbers 0 through 36
- one green zero
- red and black numbers
- even and odd bets
- high and low bets
- straight-up number bets

More complex bets can be added later.

## Suggested Development Progression

### Phase 1 — Roulette Wheel

Create the basic wheel logic.

Learn or reinforce:
- random number generation
- lists
- dictionaries or sets if useful
- mapping numbers to categories such as red, black, or green

Goal:
Generate a valid roulette result and describe it clearly.

### Phase 2 — One Bet

Add one simple bet type.

Examples:
- red or black
- even or odd
- one specific number

Learn or reinforce:
- user input
- validation
- conditionals
- function parameters
- return values

Goal:
Place one bet, spin once, and determine whether the bet won.

### Phase 3 — Bankroll

Add money tracking.

The player should have:
- starting bankroll
- bet amount
- win/loss result
- updated bankroll

Learn or reinforce:
- state
- numeric calculations
- repeated rounds
- while loops
- stopping conditions

Goal:
Play multiple rounds until the player quits or runs out of money.

### Phase 4 — Multiple Bet Types

Support several simple bet types.

Potential bets:
- red / black
- odd / even
- high / low
- straight-up number

Learn or reinforce:
- dictionaries
- branching logic
- organizing related logic into functions
- reusable validation

Goal:
The player can choose among multiple bets without duplicating large amounts of code.

### Phase 5 — Simulation Mode

Add a mode that automatically runs many spins.

Examples:
- 100 spins
- 1,000 spins
- 10,000 spins

Learn or reinforce:
- for loops
- counters
- accumulators
- repeated function calls
- separating one-round logic from simulation logic

Goal:
Run a betting strategy automatically without human input.

### Phase 6 — Results Analysis

Track outcomes across simulations.

Potential metrics:
- total wins
- total losses
- win percentage
- ending bankroll
- profit or loss
- highest bankroll
- lowest bankroll
- average result per spin

Learn or reinforce:
- counters
- averages
- percentages
- min / max
- storing historical results
- interpreting simulation output

Goal:
Summarize what happened instead of only printing every spin.

### Phase 7 — Betting Strategies

Compare simple strategies.

Potential strategies:
- flat betting
- always bet red
- random color betting
- Martingale
- fixed percentage betting

Learn or reinforce:
- strategy functions
- state across repeated rounds
- function composition
- comparing multiple simulations
- edge cases such as insufficient bankroll

Goal:
Experimentally compare strategies and understand why changing bet sizing does not change the underlying house edge.

## Concepts This Project Should Reinforce

- variables
- strings
- integers and floats
- lists
- dictionaries
- conditionals
- Boolean logic
- for loops
- while loops
- functions
- parameters
- return values
- imports
- random module
- input validation
- counters
- accumulators
- percentages
- averages
- state mutation
- simulation
- program flow
- function orchestration

## New or Less-Familiar Concepts

The project may naturally introduce:

- probability
- frequency versus probability
- expected value
- house edge
- repeated trials
- simulation design
- aggregation
- separating interactive mode from simulation mode
- simple strategy abstraction

These concepts should be introduced only when needed.

## Architecture Philosophy

Do not create the full function structure in advance.

Let the project reveal which functions are needed.

A function should be created when there is a clear responsibility that:
- repeats
- deserves a name
- is easier to reason about separately
- can be reused

Avoid unnecessary classes at first.

This project can be completed procedurally using functions, lists, dictionaries, and loops.

Classes can be considered later only if they solve a real organizational problem.

## Possible Later Extensions

Only after the core simulator works:

- American roulette with 0 and 00
- more bet types
- CSV export
- save simulation results
- charts
- matplotlib visualization
- comparison of European vs. American roulette
- Monte Carlo analysis
- configurable strategies
- command-line arguments

## Definition of Success

The project is successful if the learner can explain:

- how one spin is generated
- how a bet is evaluated
- how bankroll changes
- how repeated spins are simulated
- how results are accumulated
- how summary statistics are calculated
- how functions pass data between each other

Finishing quickly is less important than understanding the flow well enough to rebuild the project later without AI.
