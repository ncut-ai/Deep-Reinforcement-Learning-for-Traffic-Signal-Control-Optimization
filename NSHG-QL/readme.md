# Nash-Stackelberg 分层博弈 Q 学习算法 (NSHG-QL)

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

---

### 1. Introduction

- With the increasing severity of traffic congestion, the research and application of Intelligent Transportation Systems (ITS) have become increasingly important. Traffic signal control, as one of the core tasks of ITS, directly affects the efficiency and safety of traffic flow. Traditional traffic signal control methods are often based on fixed cycles and rules, lacking adaptability to dynamic traffic flows and unable to handle complex traffic environments. In order to solve this problem, reinforcement learning (RL)-based methods have become an effective solution for traffic signal control in recent years. Through Multi-Agent Reinforcement Learning (MARL), traffic signal control can be more flexible and coordinated across multiple intersections.

- In the MARL framework, each traffic signal control agent learns an optimal control strategy through interaction with the environment. However, because traffic signal control involves multiple intersections and the interaction of various traffic flows, traditional Q-learning methods face challenges due to high-dimensional state and action spaces. To address this, this paper proposes a novel Nash-Stackelberg Hierarchical Game Q-learning algorithm (NSHG-QL), which aims to optimize the traffic signal control strategy between multiple intersections through game theory, achieving more efficient and coordinated traffic signal control.

### 2. Method

#### Overview of NSHG-QL Algorithm

- The NSHG-QL algorithm combines Nash-Stackelberg hierarchical games and Q-learning. The core idea of the algorithm is to introduce the game-theoretic relationships between multiple agents into the Q-learning framework. Specifically, in a multi-agent environment, each agent needs to consider not only its own rewards but also the game relationships with other agents to better coordinate traffic signal control between multiple intersections.

#### Q Function Definition

- In Nash-DuelingDQN, the state-action value function is approximated using a deep neural network. The goal of each agent is to learn an approximately optimal policy through interaction with other agents. The Q-value update formula is as follows:

$$
Q_i^*(s_i, a_1, \dots,a_n) = r_i(s_i, a_1, \dots, a_n) + \beta \sum_{s'} p(s'|s_i, a_1, \dots, a_n) \cdot v_i(s', \pi_1^*, \dots, \pi_n)

$$

- Here, $ v_i(s', \pi_1^*, \dots, \pi_n)$ is the discounted reward in the equilibrium strategy of the hierarchical game.

#### Q Value Update Formula

- The Q value update formulas for P-Agent and S-Agent in NSHG-QL are different:
  - The Q value for **P-Agent** is updated based on the upper-level game equilibrium value $ V_{\text{al}}^t_i $:

$$
Q_i^{t+1}(s_t, a_1, \dots, a_n) = (1 - \alpha) Q_i^t(s_t, a_1, \dots, a_n) + \alpha \left[ r_t + \gamma \cdot V_{\text{al}}^t_i \right]
$$

- - The lower-level game equilibrium for **S-Agent** is computed using the Stackelberg solution:

$$
S_{eQ}_j^{t} = \text{SEQ}_j(s_t^{j+1}, \pi_1^*)
$$

The NSHG-QL algorithm updates Q values by incorporating game equilibrium values, considering the strategic relationships between agents in a multi-agent system. Compared to traditional Q-learning methods, NSHG-QL can achieve more coordinated decisions in traffic signal control across multiple intersections, optimizing traffic flow and reducing congestion.

### 3. Experiments

#### Performance Evaluation Metrics

To evaluate the effectiveness of **NSHG-QL**, we will compare its performance using the following metrics:

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

- $ D_t  $ and $D_{t+1}$  represent the total waiting times at time steps  $t$ and $ t+1$, respectively.

- The reward function aims to minimize the waiting time at traffic lights, thus improving traffic flow efficiency.

### 4. Conclusions

In this paper, we propose the NSHG-QL algorithm, which combines the Nash-Stackelberg hierarchical game model with Q-learning, effectively addressing the game coordination problem in multi-intersection signal control. Through experimental verification, we demonstrate the advantages of NSHG-QL in traffic signal control within a multi-agent environment. Future research can explore the application of this algorithm to larger-scale traffic networks, as well as further improve the computational efficiency and robustness of the algorithm.
