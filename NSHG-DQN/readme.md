# Nash-Stackelberg 分层博弈深度Q学习算法 (NSHG-DQN)

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

---

### 1. Introduction

- With the development of autonomous driving technology and intelligent traffic systems, the problem of collaborative control between multiple intersections to improve traffic efficiency and safety has become an important research topic. Existing traffic signal control methods often rely on fixed green light periods and maximizing signal cycle times, lacking adaptability to dynamic traffic conditions. To address this challenge, collaborative control methods based on **Multi-Agent Reinforcement Learning (MARL)**, particularly the **Nash-Stackelberg Hierarchical Game Model (NSHG)**, provide a new solution.

- This paper proposes a **NSHG-DQN** algorithm, based on the **Nash-Stackelberg Hierarchical Game Model** and **Deep Q-Learning (DQN)**, which combines the hierarchical game theory approach from game theory with reinforcement learning’s deep Q-learning method. This algorithm offers an efficient and adaptive solution for multi-intersection traffic signal control.

### 2. Method

In multi-intersection traffic signal control, the signal lights of multiple intersections influence each other. To solve this problem, we adopt the **Nash-Stackelberg Hierarchical Game Model (NSHG)**, which divides the problem into an upper-level game (P-Agent) and a lower-level game (S-Agent). The P-Agent represents the decision-making authority (e.g., traffic signal control at upstream intersections), while the S-Agent represents the subordinate agents (e.g., traffic signal control at downstream intersections).
In this hierarchical game model, the P-Agent and S-Agent collaborate to optimize their respective signal control strategies through game-theoretic interaction, ultimately achieving the optimal control of the entire traffic system. The solution of the game is based on both Nash equilibrium and Stackelberg equilibrium, which can effectively consider the traffic demands and signal cycles of each intersection.

#### Q Function Definition

- In Nash-DuelingDQN, the state-action value function is approximated using a deep neural network. The goal of each agent is to learn an approximately optimal policy through interaction with other agents. The Q-value update formula is as follows:

$$
Q_i^*(s_i, a_1, \cdots,a_n) = r_i(s_i, a_1, \cdots, a_n) + \beta \sum_{s'} p(s'|s_i, a_1, \cdots, a_n) \cdot v_i(s', \pi_1^*, \cdots, \pi_n)
$$

- Here, $$v_i(s', \pi_1^*, \dots, \pi_n)$$ is the discounted reward in the equilibrium strategy of the hierarchical game.

#### NSHG-DQN Algorithm Overview

- This section presents the **NSHG-DQN** algorithm, a multi-agent reinforcement learning algorithm based on the **Nash-Stackelberg Hierarchical Game Model**. NSHG-DQN is an algorithm that integrates **Deep Q-Learning (DQN)** with game theory to solve multi-intersection traffic signal control.
- In a multi-agent environment, the Q-value function for each agent is defined as $Q_i^*(s_i, a_1, a_2, \dots, a_n)$, where $s_i$ is the local state of agent $$ i $$, and $$ a_1, a_2, \dots, a_n $$ are the joint actions of all agents. To achieve hierarchical game equilibrium, the algorithm replaces the traditional maximization operator with a **Nash equilibrium** and **Stackelberg equilibrium** based on game theory.

## Q-Value Update for P-Agent and S-Agent

In the **NSHG-DQN** algorithm, the Q-value updates for the P-Agent and S-Agent are defined based on their respective game equilibrium values. Below are the details:

### Q-Value Update for P-Agent
The Q-value for the P-Agent is updated based on the upper-level game equilibrium value \(V_{\text{al}}^t_i\), as follows:


$$
Q_i^{t+1}(s_t, a_1, \dots, a_n) = (1 - \alpha) Q_i^t(s_t, a_1, \dots, a_n) + \alpha \left[ r_t + \gamma V_{al}^{t}_{i} \right]
$$


Where:
- \(\alpha\) is the learning rate,
- \(\gamma\) is the discount factor,
- \(r_t\) is the immediate reward at time \(t\),
- \(V_{\text{al}}^t_i\) is the upper-level game equilibrium value of the **P-Agent**.

### Q-Value Update for S-Agent
For the **S-Agent**, its Q-value update is based on the lower-level game equilibrium value \(V_{\text{al}}^t_j\), as follows:

$$
Q_j^{t+1}(s_t, a_1, \dots, a_n) = (1 - \alpha) Q_j^t(s_t, a_1, \dots, a_n) + \alpha \left[ r_t + \gamma V_{\text{al}}^{t}_{j} \right]
$$

Where \(V_{\text{al}}^t_j\) is the lower-level game equilibrium value of the **S-Agent**.

#### Computation of Equilibrium Values

- In **NSHG-DQN**, the upper-level game equilibrium value \( V_{\text{al}}^t_i \) for the P-Agent is computed using the Nash equilibrium, given by:

$$
V_{\text{al}}^t_i = \max_{a_i} Q_i^t(s_i, a_1, \dots, a_n)
$$

  The lower-level game equilibrium value $$V_{\text{al}}^t_j$$ for the S-Agent is computed using the Stackelberg equilibrium:

$$
V_{\text{al}}^t_j = \max_{a_j} Q_j^t(s_j, a_1, \dots, a_n)
$$

Compared to traditional Q-learning algorithms, **NSHG-DQN** does not solely rely on maximizing the individual agent’s Q-values but instead adjusts them based on the equilibrium strategies of the hierarchical game. This approach not only better simulates the collaborative relationships between multiple intersections but also significantly improves the coordination and efficiency of the entire traffic system.

### 3. Experiments

#### Performance Evaluation Metrics

To evaluate the effectiveness of **NSHG-DQN**, we will compare its performance using the following metrics:

- **Queue Length**: Total number of vehicles waiting at intersections.
- **Waiting Time**: Total waiting time of stopped vehicles at intersections.
- **Average Speed**: The average speed of vehicles approaching the intersections.
- **Incoming/Outgoing Lane Density**: The number of vehicles in the incoming and outgoing lanes at intersections.
- **Pressure**: The difference in vehicle density between incoming and outgoing lanes.

#### Reward Function

In this study, the reward function is designed based on the change in vehicle waiting time:

$$
\mathcal{R}_t = D_t - D_{t+1}
$$

where:

- $$D_t$$ and $$D_{t+1}$$  represent the total waiting times at time steps  $$t$$  and  $$t+1$$ , respectively.

- The reward function aims to minimize the waiting time at traffic lights, thus improving traffic flow efficiency.

### 4. Conclusions

This section presents a series of experiments to validate the effectiveness of the **NSHG-DQN** algorithm in multi-intersection traffic signal control. The experimental results demonstrate that the **NSHG-DQN** algorithm significantly improves traffic flow efficiency, reduces congestion time, and adapts well to variations in traffic demand when compared to traditional Q-learning algorithms.
The experiments were conducted using the typical traffic simulation platform **SUMO**, and multiple intersections were set up for signal control. Through various traffic flow and signal cycle configurations, the **NSHG-DQN** algorithm's adaptability to different scenarios was validated.
