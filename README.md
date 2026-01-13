# 🎮 Adaptive Prisoner’s Dilemma – Rule-Based AI Strategy Game

## 📌 Overview
This project is a **terminal-based Python implementation** of the **Iterated Prisoner’s Dilemma**, where a human player competes against an **adaptive AI agent**.

Unlike a fixed-rule bot, the AI:
- Observes the player’s past actions
- Classifies player behavior dynamically
- Adapts its strategy to maximize long-term reward
- Punishes repeated defection but allows forgiveness

The goal is to demonstrate **game theory concepts and AI decision-making** using simple Python logic.

---

## 🧠 Core Concepts Used
- Prisoner’s Dilemma (Iterated Version)
- Payoff Matrix
- Opponent Behavior Modeling
- Adaptive Decision Making
- Conditional Cooperation & Delayed Forgiveness

---

## 🕹 How the Game Works

### 1. Player Choices
In each round, the player chooses:
- `C` → Cooperate  
- `D` → Defect  

The game runs for a user-defined number of rounds.

---

### 2. Payoff Rules
Scores are updated using the standard Prisoner’s Dilemma payoff matrix:

| Player | AI | Player Score | AI Score |
|------|----|-------------|----------|
| C | C | +3 | +3 |
| D | C | +5 | 0 |
| C | D | 0 | +5 |
| D | D | +1 | +1 |

---

## 🤖 AI Decision Logic

### Step 1: Early Exploration
- For the **first 2 rounds**, the AI always cooperates.
- This allows the AI to observe player behavior without judgment.

---

### Step 2: Player Behavior Analysis
After round 2, the AI calculates:
- Cooperation rate
- Defection rate

Based on these rates, the player is classified as:
- **Cooperative** (≥ 70% cooperation)
- **Aggressive** (≥ 70% defection)
- **Opportunistic** (mixed behavior)

This classification is **recomputed every round**, so the AI can forgive and adapt.

---

### Step 3: Strategy Selection
- **Cooperative player** → Tit-for-Tat  
  (AI copies the player’s previous move)
- **Aggressive player** → Defensive punishment  
  (AI defects only after repeated defection)
- **Opportunistic player** → Cautious Tit-for-Tat  

The AI does **not punish a single defection** and requires **consistent behavior** before changing strategy.

---

### Step 4: Delayed Forgiveness
If the player defected repeatedly, the AI continues to defect **even if the player cooperates once**.
Trust is restored only after consistent cooperation.

This prevents exploitation and models realistic strategic behavior.

---

## 📊 End of Game Analysis
At the end of the game:
- Final scores are displayed
- Player cooperation rate is calculated
- A conclusion is shown indicating whether trust or aggression led to better outcomes

---

## ✅ Key Features
- Rule-based adaptive AI
- Explainable and transparent decisions
- Prevents short-term exploitation
- Forgiveness is possible but earned
- Simple Python logic with strong AI foundations

---

## 🚀 Learning Outcome
This project demonstrates how **AI systems can reason strategically** using game theory principles, making it a strong foundation for:
- Multi-agent systems
- Reinforcement learning
- Decision-making AI

---

## 📝 Note
This is a **rule-based AI agent**.  
The focus is on **logic, reasoning, and adaptability**, which are core AI concepts.
