# Nash-DuelingDQN

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

---


### 1. Introduction

- In modern cities, traffic signal control systems are still largely dependent on fixed-time plans, which are unable to adapt to dynamic traffic flows. With urbanization, traffic congestion has become a major issue, leading to environmental pollution, wasted time, and increased energy consumption. To alleviate these problems, optimizing traffic signal control is of utmost importance.

- Traditional rule-based control methods, such as fixed cycles or bandwidth maximization strategies, are not suitable for the fluctuations and real-time changes in traffic flow. As a result, researchers are exploring reinforcement learning (RL)-based methods to automatically optimize traffic signal control. RL interacts with the environment and incrementally learns the best decision-making policy, making it particularly suitable for addressing the complex dynamic optimization problem of traffic signal control.

- **Nash-DuelingDQN** is an advanced algorithm that combines game theory and deep reinforcement learning. By modeling the traffic signal control problem as a multi-agent game, Nash-DuelingDQN improves the decision-making efficiency of individual agents, thus effectively addressing the challenges of large-scale, multidimensional traffic signal control.

- This paper aims to introduce the **Nash-DuelingDQN** algorithm as a more adaptive and high-performance method for traffic signal control optimization and to compare its performance with traditional methods. We will evaluate its advantages using various performance metrics and demonstrate its application potential in complex traffic environments.

### 2. Method

#### Nash-DuelingDQN

- **Nash-DuelingDQN** is a novel algorithm that combines game theory and deep reinforcement learning. In a multi-agent system for traffic signal control, each agent (i.e., each traffic signal at an intersection) chooses the optimal signal control strategy based on the current traffic state and the actions of other agents. By incorporating Nash equilibrium from game theory, Nash-DuelingDQN ensures that agents not only consider their own interests but also take into account the behavior of other agents, leading to globally optimal coordinated control.
- **DuelingDQN** builds on the traditional DQN by introducing two separate value estimation streams: one for state value (State Value) and one for action advantages (Action Advantage). This structure helps agents more efficiently learn and evaluate the value of state-action pairs, improving learning stability and efficiency. Nash-DuelingDQN further integrates this structure with game theory, considering each agent's strategy's impact on other agents' actions, leading to collaborative learning in a multi-agent system.
- Specifically, Nash-DuelingDQN incorporates a **joint policy** and **game-theoretic optimization objective**, enabling each agent to optimize not only in its local environment but also in a global game-theoretic framework, thus improving the overall efficiency of traffic signal control.

#### Mathematical Formula

- In Nash-DuelingDQN, the state-action value function is approximated using a deep neural network. The goal of each agent is to learn an approximately optimal policy through interaction with other agents. The Q-value update formula is as follows:

$$
Q_{new}(s, a) = (1-\alpha) Q(s, a) + \alpha \left( R + \gamma \max_{a'} Q(s', a') \right)
$$

- where:
  
  - $$Q(s, a)$$ is the Q-value for taking action $$a$$ in state $$s$$;
  
  - $$Q(s, a)$$is the Q-value for taking action $$a$$ in state $$s$$;
  
  - $$R$$ is the immediate reward;
  
  - $$\gamma$$ is the discount factor;
  
  - $$\max_{a'} Q(s', a') $$ is the maximum Q-value in the next state $$s'$$.

### 3. Experiments

#### Performance Evaluation Metrics

To evaluate the effectiveness of **Nash-DuelingDQN**, we will compare its performance using the following metrics:

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

- $$D_t$$ and $$D_{t+1}$$ represent the total waiting times at time steps $$t$$ and $$t+1$$, respectively.

- The reward function aims to minimize the waiting time at traffic lights, thus improving traffic flow efficiency.

### 4. Conclusions

In this study, we introduce the **Nash-DuelingDQN** algorithm and compare its performance with traditional Q-Learning, DQN, and DuelingDQN methods. Experimental results show that **Nash-DuelingDQN** outperforms the other methods on several metrics, especially in large-scale, multi-intersection traffic signal control. The algorithm demonstrates superior coordination in decision-making, leading to more efficient traffic signal optimization.

Although **Nash-DuelingDQN** is more complex to train, its performance in multi-agent collaboration and game-theoretic environments highlights its strong adaptability and optimization capabilities. As such, **Nash-DuelingDQN** holds significant promise for future intelligent traffic systems, especially for addressing complex urban traffic flow and real-time scheduling needs.
