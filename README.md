# RPG text game

This is a simple Python project that simulates an RPG game using JSON.

## Features

- Save player name, level, health, xp ponts, lives, and inventory
- Load player data from a JSON file
- Add items, level up, and apply health bonuses
- More than 300 items
- 100 different events
- the difficulty and power of items gained scales alongside the players level

## Files

- `player-game.py`: The main Python script
- `player.json`: Stores the saved player data
- `command_list.json`:containes the used commands in the game
- `events.json`:contain all the events
- `database.json`:dics that containes all the items sorted in three categories(weapons, shields, potions) with unique ID to each item
## How to Run

```bash
python player-game.py
