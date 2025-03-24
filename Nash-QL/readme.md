## Nash-Q Learning (Nash-QL)

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

---

### 1. **Introduction**

Traffic signal control in multi-agent settings often involves competitive and cooperative interactions between multiple intersections. **Nash-Q Learning (Nash-QL)** is an extension of Q-learning tailored for **multi-agent reinforcement learning (MARL)** scenarios where multiple agents interact strategically under **game-theoretic settings**.

This paper proposes a **Nash-QL-based traffic signal control algorithm**, which formulates signal control as a **Markov Game** and uses **Nash equilibria** to update Q-values, ensuring equilibrium-based decision-making for adaptive traffic signal control.

### 2. **Method**

#### **Markov Game Definition**
A Markov Game for **N** interacting agents is defined by:
- **State Space** $S$: Joint state representation of all agents (e.g., traffic conditions at intersections).
- **Action Space** $A_i$: The action set available to agent $i$ (e.g., signal phase selections).
- **Transition Function** $T(s, a_1, ..., a_N, s')$: Defines the transition probabilities.
- **Reward Function** $R_i(s, a_1, ..., a_N)$: Determines the reward each agent receives.

Each agent selects actions **simultaneously**, influencing the shared environment.

#### **Nash Equilibrium-Based Q-Update**
Unlike traditional Q-learning, Nash-QL incorporates **Nash equilibrium solutions** to determine the optimal joint actions.

The Q-value update follows:

$$ Q_i(s, a_1, ..., a_N) = (1 - \alpha) Q_i(s, a_1, ..., a_N) + \alpha \left[ R_i + \gamma \cdot V_i(s') \right] $$

where:
- $\alpha$ is the learning rate,
- $\gamma$ is the discount factor,
- $V_i(s')$ is the **Nash equilibrium value** at the next state, computed as:

$$ V_i(s') = \max_{\pi} \sum_{a_1, ..., a_N} \pi(a_1, ..., a_N) Q_i(s', a_1, ..., a_N) $$

where $\pi(a_1, ..., a_N)$ is the Nash equilibrium strategy.

#### **Equilibrium Computation**
The Nash equilibrium at each step is computed using **iterative best-response algorithms** or **linear programming** techniques to solve the following equation:

$$ \sum_{j \neq i} \pi_j^*(a_j) \nabla_{a_i} Q_i(s, a_1, ..., a_N) = 0 $$

This ensures that no agent can improve its outcome **unilaterally**, aligning with equilibrium-based learning.

### 3. **Experiments**

#### Performance Evaluation Metrics
We evaluate **Nash-QL** using the following metrics:
- **Traffic Flow**: The number of vehicles passing through intersections per unit time.
- **Queue Length**: The total number of waiting vehicles at intersections.
- **Waiting Time**: The cumulative waiting time of all vehicles.
- **Signal Stability**: The variation in signal phase changes to prevent excessive fluctuations.

#### Reward Function
The reward function is designed to encourage equilibrium-driven traffic optimization:

$$ \mathcal{R}_i = - \sum_{j \neq i} \left| P_i - P_j \right| - \lambda \cdot Q_i $$

where:
- $P_i$ is the **traffic pressure** for agent $i$,
- $\lambda$ is a weighting factor,
- $Q_i$ is the queue length at the controlled intersection.

### 4. **Conclusions**

This study demonstrates that **Nash-Q Learning** provides an effective multi-agent reinforcement learning framework for traffic signal control. By incorporating **game-theoretic equilibria**, Nash-QL ensures stable, adaptive, and cooperative decision-making across multiple intersections.

Experimental results from **SUMO simulations** show that **Nash-QL outperforms independent Q-learning** in terms of **traffic flow efficiency** and **signal stability**, making it a promising approach for **decentralized intelligent traffic management**.
