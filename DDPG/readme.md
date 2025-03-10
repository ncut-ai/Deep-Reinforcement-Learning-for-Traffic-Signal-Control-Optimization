## DDPG (Deep Deterministic Policy Gradient)

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

--- 

### 1. **Introduction**

With the rapid development of intelligent transportation systems, optimizing traffic signal control has become a crucial research area. Traditional rule-based traffic signal control methods often struggle to adapt to dynamic and complex traffic conditions. Reinforcement learning techniques, particularly continuous control algorithms like **Deep Deterministic Policy Gradient (DDPG)**, provide a promising approach to optimizing traffic signals in real-time.

This paper proposes a **DDPG-based traffic signal control algorithm**, which leverages **actor-critic architecture** and **deterministic policy gradients** to learn an optimal traffic signal control policy in continuous action spaces. Unlike discrete-action reinforcement learning algorithms such as DQN, DDPG is more suitable for scenarios where precise control of signal timings is necessary.

### 2. **Method**

The **DDPG** algorithm is an **off-policy actor-critic reinforcement learning** method designed for continuous control tasks. It consists of two main networks:

- **Actor Network**: Determines the optimal action (signal timing) given the current state (traffic conditions).
- **Critic Network**: Evaluates the quality of the selected action by estimating the Q-value.

#### **State Space and Action Space**

- **State Space**: The state representation includes traffic flow, vehicle queue length, current signal phase, and intersection pressure.
- **Action Space**: The action represents the duration of each green light phase, which is continuous rather than discrete.

#### **Policy Learning with Deterministic Gradients**

DDPG uses **deterministic policy gradients** to directly optimize the policy. The policy function $\mu(s; \theta^\mu)$ maps states to actions, and the objective is to maximize the expected return:

$$ J(\theta^\mu) = \mathbb{E}_{s \sim \rho^\beta} [ Q(s, \mu(s; \theta^\mu)) ] $$

The policy gradient is computed as:

$$ \nabla_{\theta^\mu} J(\theta^\mu) = \mathbb{E}_{s \sim \rho^\beta} \left[ \nabla_a Q(s, a; \theta^Q) \big|_{a=\mu(s)} \nabla_{\theta^\mu} \mu(s; \theta^\mu) \right] $$

where $Q(s, a; \theta^Q)$ is the Q-value estimated by the critic network.

#### **Q-value Update (Critic Network)**

The critic network is updated using the Bellman equation:

$$ y = r + \gamma Q(s', \mu(s'; \theta^\mu); \theta^Q) $$

where:
- $y$ is the target Q-value,
- $\gamma$ is the discount factor,
- $s'$ is the next state,
- $\mu(s')$ is the next action determined by the actor network.

The loss function for the critic network is:

$$ L(\theta^Q) = \mathbb{E} \left[ (y - Q(s, a; \theta^Q))^2 \right] $$

#### **Experience Replay and Target Networks**

To improve training stability, **experience replay** and **target networks** are used:

- **Experience Replay**: Stores past experiences $(s, a, r, s')$ in a buffer and samples mini-batches to decorrelate training data.
- **Target Networks**: Uses slow-moving copies of the actor and critic networks to stabilize learning:

  $$ \theta^- = \tau \theta + (1 - \tau) \theta^- $$
  
  where $\tau$ is a small update factor.

### 3. **Experiments**

#### Performance Evaluation Metrics

To evaluate the effectiveness of **DDPG**, we compare its performance using the following metrics:

- **Queue Length**: Total number of vehicles waiting at intersections.
- **Waiting Time**: Total waiting time of stopped vehicles at intersections.
- **Average Speed**: The average speed of vehicles approaching the intersections.
- **Incoming/Outgoing Lane Density**: The number of vehicles in the incoming and outgoing lanes at intersections.
- **Pressure**: The difference in vehicle density between incoming and outgoing lanes.

#### Reward Function

The reward function is designed to minimize congestion by reducing vehicle waiting time:

$$ \mathcal{R}_t = D_t - D_{t+1} $$

where:
- $D_t$ and $D_{t+1}$ represent the total waiting times at time steps $t$ and $t+1$, respectively.

### 4. **Conclusions**

This study validates the effectiveness of the **DDPG** algorithm in traffic signal control by enabling continuous action adjustments for signal timing optimization. Compared to traditional discrete-action reinforcement learning methods, **DDPG** demonstrates superior adaptability and performance in handling complex traffic dynamics.

The experiments were conducted using the traffic simulation platform **SUMO**, testing signal control for multiple intersections. The results show that the **DDPG** algorithm significantly improves traffic efficiency by reducing congestion and dynamically adjusting signal timings based on real-time traffic conditions.

