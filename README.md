# Adaptive Prisoner's Dilemma

This project simulates a repeated Prisoner’s Dilemma game where the AI adapts dynamically to the player's behaviour instead of following a fixed strategy.

---

## 🎮 Gameplay

- Enter `C` to Cooperate or `D` to Defect.
- The AI analyses your past actions and adjusts its moves every round.
- Final results reveal your overall cooperation behaviour.

---

## 📊 Payoff Matrix

| Player | AI | Player Score | AI Score |
|--------|----|--------------|----------|
| C      | C  | +3           | +3       |
| D      | C  | +5           | 0        |
| C      | D  | 0            | +5       |
| D      | D  | +1           | +1       |

---

## 🗂 Behaviour Tracking

The AI stores both player and AI moves and calculates cooperation and defection rates to understand behavioural patterns.

---

## 🧪 Exploration Phase

For the first two rounds, the AI always cooperates to observe the player’s natural tendencies.

---

## 🧠 Player Classification

| Condition | Player Type |
|----------|-------------|
| ≥ 70% Cooperation | Cooperative |
| ≥ 70% Defection | Aggressive |
| Else | Opportunistic |

The player is reclassified every round.

---

## 🤖 Strategy Adaptation

- **Cooperative players** → Tit-for-Tat
- **Aggressive players** → Punish only after repeated betrayal
- **Opportunistic players** → Mirror previous move

---

## 🏁 Game Result

At the end, the program displays your total scores and cooperation rate, showing how trust or aggression impacted the outcome.
