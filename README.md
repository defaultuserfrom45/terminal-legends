# ⚔️ Terminal Legends

A terminal-based role-playing game where you fight monsters, level up, and become the ultimate champion.

---

## 🧭 About the Game

**Terminal Legends** is a text-based RPG developed in Python.  
The game runs entirely in the terminal and focuses on strategy, progression, and character development.

You will create your own hero, battle enemies, earn rewards, and ultimately face the final boss.

---

## 🎯 Goal

Your objective is simple:

- Reach **Level 3**
- Prepare your character through battles and upgrades
- Defeat the **Dragon Boss**
- Become the champion of Terminal Legends

---

## 🎮 Gameplay Overview

During the game you can:

- Fight randomly generated monsters
- Gain **XP** and level up
- Earn **gold** from battles
- Buy upgrades in the shop
- Use potions to heal yourself
- Save and load your progress
- Unlock and fight the final boss

---

## 🧙 Character Classes

At the start of the game, you can choose between three classes:

### 🛡️ Warrior
- High health
- Balanced damage
- **Special Ability: Heavy Strike**
  - Deals extra damage

---

### 🔥 Mage
- Lower health
- High damage
- **Special Ability: Fireball**
  - Deals strong damage
  - Costs a small amount of HP

---

### 🗡️ Rogue
- Balanced stats
- Fast attacks
- **Special Ability: Double Attack**
  - Hits twice in one turn

---

## ⚔️ Combat System

The game uses a **turn-based combat system**.

In each fight, you can choose to:

- Attack
- Use your special ability
- Use a potion
- Run away (not possible in boss fights)

Enemies scale with your level, so the game becomes more challenging as you progress.

---

## 🏪 Shop System

After battles, you earn gold which you can spend in the shop:

- Buy potions (healing)
- Increase your attack
- Increase your maximum HP

---

## 🐉 Boss Battle

Once you reach **Level 3**, you unlock the final challenge:

- Fight the **Dragon**
- No escape is possible
- Defeat it to win the game

---

## 💾 Save & Load System

- Save your progress at any time
- Load your character from the main menu
- Data is stored locally in a file (`savegame.json`)

---

## ⚙️ Installation

Make sure you have Python **3.10 or higher** installed.

### 1. Clone the repository

```bash
git clone https://github.com/DEIN-USERNAME/terminal-legends.git
cd terminal-legends
```

### 2. Install the project

```bash
uv pip install -e .
```

---

## ▶️ Run the Game

Start the game with:

```bash
uv run -m terminal_legends
```

---

## 💡 Alternative (without uv)

If you do not use uv, you can run the game with:

```bash
python -m terminal_legends
```

---

## 👤 Author

Yasin Sabanoglu

