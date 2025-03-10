# MFQ-MLP

### Table of contents

1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

--- 


### 1. **Introduction**

With the development of intelligent transportation systems and autonomous driving technologies, achieving coordinated control between multiple intersections to improve traffic efficiency and safety has become an important research topic. Existing traffic signal control methods often rely on fixed green light cycles and signal cycle maximization, lacking adaptability to dynamic traffic conditions. To address this issue, cooperative control methods based on **Multi-Agent Reinforcement Learning (MARL)**, especially those using **Multi-Agent Q-value Decomposition (MFQ)** and **Multilayer Perceptron (MLP)** models, offer a promising solution.

This paper proposes a **MFQ-MLP** algorithm, which combines the **Q-value decomposition (MFQ)** method and the **Multilayer Perceptron (MLP)** model from deep learning to achieve multi-intersection traffic signal control through reinforcement learning.

The **MFQ-MLP** algorithm is a reinforcement learning method that combines **Q-value decomposition** and **Multilayer Perceptron (MLP)** models. In the multi-intersection traffic signal control scenario, the signal control of multiple intersections influences each other, requiring a method capable of handling cooperative actions between multiple agents. The **MFQ-MLP** algorithm decomposes the Q-value function for each agent (intersection) using the **MFQ** method, and uses an MLP model to perform feature learning in a high-dimensional space to optimize the traffic signal decisions.

In MFQ-MLP, the Q-value function for all intersections is decomposed into multiple sub-Q-values, and the decision-making and coordination for each intersection are implemented through the MLP network. The key of this method lies in achieving effective information sharing between intersections through Q-value decomposition, while utilizing the MLP network to improve modeling capability and decision-making accuracy in complex environments.

### 2. **Method**

The basic framework of the **MFQ-MLP** algorithm includes the following parts:

- **State Space**: The state of each intersection consists of factors such as the current signal cycle, traffic flow, vehicle queue length, and other traffic-related information.
- **Action Space**: The action space for each intersection includes different green light cycle configurations, signal switching timings, etc.
- **Q-value Function**: The Q-value function for each intersection is decomposed using the **MFQ** method, representing the value of taking a specific action in the current state.

#### **Q-value Decomposition (MFQ)**

The **MFQ (Multi-Agent Q-value Decomposition)** method decomposes the global Q-value function into multiple sub-Q-values to achieve multi-agent cooperative learning. In traffic signal control, the Q-values for each intersection are decomposed into multiple local Q-values, allowing each intersection to independently learn its own Q-value, while collaborating in a global context.

The Q-value decomposition formula is as follows:

$$
Q_{\text{total}}(s, a_1, a_2, \dots, a_n) = \sum_{i=1}^{n} Q_i(s, a_1, \dots, a_n)
$$

Where:

- $$Q_{\text{total}} $$ is the global Q-value,
- $$Q_i$$ is the local Q-value for each intersection $i$.

### **Multilayer Perceptron (MLP)**

In the **MFQ-MLP** algorithm, the **Multilayer Perceptron (MLP)** network is used as a function approximator to extract features from the raw state and predict the Q-value for each intersection. The MLP network performs a series of nonlinear transformations to map the raw input states to the Q-values for each intersection, helping agents to make decisions.

The MLP network structure is as follows:

- **Input Layer**: The input state consists of traffic flow, signal cycle, vehicle queue length, and other relevant information for each intersection.
- **Hidden Layers**: Several fully connected layers to extract features from the input data.
- **Output Layer**: Outputs the Q-values for each intersection to determine the optimal signal control strategy.

### **Q-value Update**

In the **MFQ-MLP** algorithm, the Q-value is updated using the classic Q-learning method. The Q-value for each intersection is updated using the following formula:

$$
Q_i^{t+1}(s_t, a_1, \dots, a_n) = (1 - \alpha) Q_i^t(s_t, a_1, \dots, a_n) + \alpha \left[ r_t + \gamma \max_{a'_i} Q_i^{t+1}(s_t', a_1, \dots, a_n) \right]
$$

Where:

- $$\alpha $$ is the learning rate,
- $$\gamma$$ is the discount factor,
- $$r_t$$ is the immediate reward,
- $$s_t'$$ is the next state,
- $$a'_i$$ is the next action.

Compared to traditional Q-learning algorithms, the **MFQ-MLP** algorithm can handle multi-intersection coordination problems more effectively by combining Q-value decomposition and MLP. The Q-value decomposition allows each intersection to independently learn its own control strategy, while the MLP network improves learning ability and accuracy in high-dimensional environments, significantly improving the performance of traffic signal control.

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
\mathcal{R}_t =  D_t - D_{t+1}
$$ 

where:

- $$D_t$$ and $$D_{t+1}$$ represent the total waiting times at time steps $$t$$ and $$t+1$$ , respectively.

- The reward function aims to minimize the waiting time at traffic lights, thus improving traffic flow efficiency. 

### 4. **Experiments and Results Analysis**

This section verifies the effectiveness of the **MFQ-MLP** algorithm in multi-intersection traffic signal control through experiments. The experimental results show that compared to traditional Q-learning algorithms, the **MFQ-MLP** algorithm significantly improves traffic flow efficiency, reduces congestion time, and performs well in adapting to varying traffic demands.

The experiments were conducted using the traffic simulation platform **SUMO**, testing signal control for multiple intersections. Different traffic flows and signal cycle configurations were used to validate the adaptability and superiority of the **MFQ-MLP** algorithm in various scenarios.
