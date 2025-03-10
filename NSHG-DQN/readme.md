## Nash-DQN (Nash Deep Q-Network)

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

--- 

### 1. **Introduction**

Traffic signal control in multi-agent environments poses a significant challenge due to the complex interactions between different intersections. Traditional **Deep Q-Networks (DQN)** focus on optimizing individual agents' rewards but often fail to account for strategic interactions in a multi-agent setting.

To address this issue, this paper proposes a **Nash-DQN-based traffic signal control algorithm**, which leverages Nash Equilibrium principles in multi-agent reinforcement learning (MARL). By integrating **game-theoretic concepts** with deep Q-learning, Nash-DQN enables agents to learn equilibrium-based policies for optimizing traffic signal control under **competitive and cooperative** scenarios.

### 2. **Method**

Nash-DQN extends the traditional **Q-learning** framework by incorporating **Nash Equilibria** in multi-agent decision-making. Instead of selecting actions solely based on individual Q-values, agents compute Nash Equilibria in their joint action space to make optimal decisions.

#### **State Space and Action Space**

- **State Space**: Each intersection's state consists of traffic flow, queue lengths, phase durations, and neighboring intersections' signal states.
- **Action Space**: The action represents the choice of traffic light phase and duration for each intersection.

#### **Nash Q-Value Computation**

The Nash Q-value function is defined as:

$$ Q_i(s, a_i, a_{-i}) $$

where:
- $s$ is the state,
- $a_i$ is agent $i$'s action,
- $a_{-i}$ represents the joint actions of all other agents.

The Nash-DQN algorithm updates the Q-values by solving a **Nash Equilibrium** at each step:

$$ Q_i(s, a_i) = r_i + \gamma \sum_{s'} P(s' | s, a_i, a_{-i}) V_i(s') $$

where:
- $r_i$ is the immediate reward,
- $\gamma$ is the discount factor,
- $P(s' | s, a_i, a_{-i})$ is the transition probability,
- $V_i(s')$ is the expected value of the next state given Nash equilibrium actions.

#### **Equilibrium Policy Learning**

Instead of using traditional **$\epsilon$-greedy action selection**, Nash-DQN selects actions based on a Nash equilibrium strategy:

1. Construct the **joint Q-matrix** for all agents.
2. Compute a Nash Equilibrium strategy using **game-theoretic solvers**.
3. Choose actions based on the computed Nash Equilibrium.

### 3. **Experiments**

#### **Performance Evaluation Metrics**

The Nash-DQN algorithm is evaluated using the following metrics:

- **Average Vehicle Delay**: The mean time vehicles spend waiting at intersections.
- **Traffic Flow Efficiency**: The number of vehicles passing through intersections per unit time.
- **Intersection Congestion Levels**: Measured using vehicle queue lengths.

#### **Reward Function**

The reward function considers both local and neighboring intersection congestion:

$$ \mathcal{R}_i = - (D_i + \sum_{j \in \mathcal{N}(i)} w_j D_j) $$

where:
- $D_i$ is the queue length at intersection $i$,
- $\mathcal{N}(i)$ represents neighboring intersections,
- $w_j$ is a weight factor for neighboring intersections.

#### **Comparison with Other Methods**

The Nash-DQN algorithm is compared against:

- **Independent DQN**: Each intersection learns its policy independently.
- **Nash-Q Learning**: A tabular Nash-based method.
- **Fixed-Time Control**: Traditional rule-based signal timing.

### 4. **Conclusions**

This study demonstrates that **Nash-DQN** outperforms standard reinforcement learning approaches in multi-agent traffic signal control by leveraging **Nash Equilibria**. The algorithm enables **better coordination among intersections**, reducing congestion and improving overall traffic efficiency.

The experimental results show that Nash-DQN significantly reduces vehicle waiting time and improves intersection throughput compared to **Independent DQN** and **traditional control methods**. Future work will explore **scalability** and **real-world deployment** challenges for Nash-DQN in large-scale urban traffic networks.
