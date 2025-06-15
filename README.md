# 🧙‍♂️ RPG Text Game

A terminal-based role-playing game built in Python, powered by JSON for data storage and state persistence.

This project simulates a classic RPG experience with leveling, loot, combat, and decision-making — all entirely in the terminal.

---

## 🎮 Features

- Save and load player state (name, level, XP, health, lives, inventory)
- Level-up mechanics with dynamic health scaling
- Over **300 unique items** across categories (weapons, shields, potions)
- **100+ distinct combat events**
- Smart reward system — item difficulty scales with player level
- Inventory management (max 20 items, throw items, confirm actions)
- Combat chance system with risk/reward percentage
- Save prompt every 5 events for safety and persistence

---

## 📂 Files

| File              | Purpose |
|-------------------|---------|
| `player-game.py`        | Main game engine (Python script) |
| `player.json`           | Saves player data (level, health, XP, etc.) |
| `database.json`         | Contains all item data (3 categories) with stats |
| `events.json`           | Stores game events and related combat data |
| `command_list.json`     | Defines available in-game commands |

---

## 🚀 How to Run

Make sure all `.json` files are in the same directory as `player-game.py`. Then run:

```bash
python player-game.py