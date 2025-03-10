## DuelingDDQN-DNN (D3QN)

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

--- 

### 1. **Introduction**

With the development of intelligent transportation systems and autonomous driving technologies, achieving coordinated control between multiple intersections to improve traffic efficiency and safety has become an important research topic. Existing traffic signal control methods often rely on fixed green light cycles and signal cycle maximization, lacking adaptability to dynamic traffic conditions. To address this issue, reinforcement learning-based approaches, particularly **Dueling Double Deep Q-Networks (DuelingDDQN or D3QN)** combined with **Deep Neural Networks (DNN)**, offer a promising solution.

This paper proposes a **DuelingDDQN-DNN (D3QN)** algorithm, which enhances the standard DDQN model by incorporating a **Dueling Network Architecture**, effectively separating the value and advantage functions for improved traffic signal decision-making.

### 2. **Method**

The basic framework of the **DuelingDDQN-DNN** algorithm includes the following parts:

- **State Space**: The state of each intersection consists of factors such as the current signal phase, traffic flow, vehicle queue length, and other traffic-related information.
- **Action Space**: The action space includes different signal switching strategies.
- **Q-value Function**: The Q-value function is decomposed into a value function and an advantage function to enhance learning stability.

#### **Dueling Q-Network**

In a traditional **DQN**, the Q-value function is represented as:

$$ Q(s, a) $$

where \( s \) is the state and \( a \) is the action. However, in the **Dueling Architecture**, the Q-value function is decomposed into:

$$ Q(s, a) = V(s) + A(s, a) $$

where:
- \( V(s) \) represents the state value,
- \( A(s, a) \) represents the advantage function, which captures the relative benefit of each action.

To ensure uniqueness, the advantage function is modified as:

$$ Q(s, a) = V(s) + \left(A(s, a) - \frac{1}{|A|} \sum_{a'} A(s, a') \right) $$

where \( |A| \) is the number of actions.

This structure allows the model to better estimate the relative importance of different actions and stabilize training.

### **Q-value Update (Double DQN Mechanism)**

To reduce overestimation bias, **Double DQN (DDQN)** updates the Q-value using separate networks:

$$ y = r + \gamma Q_{\text{target}}(s', \arg\max_a Q_{\text{online}}(s', a; \theta); \theta^-) $$

where:
- \( Q_{\text{online}} \) is the online Q-network,
- \( Q_{\text{target}} \) is the target Q-network,
- \( \theta \) and \( \theta^- \) are the parameters of the online and target networks, respectively.

This modification helps mitigate the instability caused by overestimation in Q-learning.

### 3. **Experiments**

#### Performance Evaluation Metrics

To evaluate the effectiveness of **DuelingDDQN-DNN**, we compare its performance using the following metrics:

- **Queue Length**: Total number of vehicles waiting at intersections.
- **Waiting Time**: Total waiting time of stopped vehicles at intersections.
- **Average Speed**: The average speed of vehicles approaching the intersections.
- **Incoming/Outgoing Lane Density**: The number of vehicles in the incoming and outgoing lanes at intersections.
- **Pressure**: The difference in vehicle density between incoming and outgoing lanes.

#### Reward Function

In this study, the reward function is designed based on the change in vehicle waiting time:

$$ \mathcal{R}_t = D_t - D_{t+1} $$

where:

- \( D_t \) and \( D_{t+1} \) represent the total waiting times at time steps \( t \) and \( t+1 \), respectively.
- The reward function aims to minimize the waiting time at traffic lights, thus improving traffic flow efficiency.

### 4. **Conclusions**

This study validates the effectiveness of the **DuelingDDQN-DNN (D3QN)** algorithm in multi-intersection traffic signal control. The experimental results show that compared to traditional Q-learning and standard DDQN, the **DuelingDDQN-DNN** algorithm significantly improves traffic flow efficiency, reduces congestion time, and performs well in adapting to varying traffic demands.

The experiments were conducted using the traffic simulation platform **SUMO**, testing signal control for multiple intersections. Different traffic flows and signal cycle configurations were used to validate the adaptability and superiority of the **DuelingDDQN-DNN** algorithm in various scenarios。

