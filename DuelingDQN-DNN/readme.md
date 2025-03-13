# DuelingDQN-DNN

---

### Table of contents 
1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

---
### 1. Introduction 

- Dueling DQN-DNN is an advanced reinforcement learning algorithm that combines Dueling Double Q-Networks (Dueling DQN) with Deep Neural Networks (DNN). It enhances decision-making by separately estimating state values and action advantages, improving the efficiency of Q-value approximation. The architecture splits the network into two streams: one for value and another for advantage, which are later combined to compute the final Q-values. This separation allows the model to better evaluate actions, especially in states where action choice is less critical. By integrating DNNs, the algorithm scales effectively to handle high-dimensional inputs like images. Dueling DQN-DNN achieves more stable learning and faster convergence compared to traditional DQN approaches.

### 2. Method 

- #### Q-Value Decomposition Formula

The Q-value decomposition formula splits the Q-value into a state value function and an advantage function, improving the modeling of state values and action advantages.

$$
Q(s, a; \theta) = V(s; \theta) + \left(A(s, a; \theta) - \frac{1}{|A|} \sum_{a'} A(s, a'; \theta)\right)
$$

Here, $$Q(s, a; \theta)$$ represents the Q-value for taking action $$a$$ in state $$s$$ . $$V(s; \theta)$$ denotes the state value function, representing the overall value of state $$s$$ . $$A(s, a; \theta)$$ is the advantage function, representing the relative advantage of action $$a$$ compared to other actions. $$|A|$$ is the total number of possible actions.

---

- #### Bellman Equation for Target Q-Value

The Bellman equation is used to compute the target Q-value, guiding the model's learning process by estimating future rewards.

$$
y_i = r + \gamma \max_{a'} Q(s', a'; \theta^-)
$$

Here, $$y_i$$ represents the target Q-value. $$r$$ denotes the immediate reward received after taking action $$a$$ in state $$s$$ . $$\gamma$$ is the discount factor controlling the importance of future rewards ( $$0 \leq \gamma \leq 1$$ ). $$Q(s', a'; \theta^-)$$ is the Q-value for the next state $$s'$$ and action $$a'$$ , estimated by the target network.

---

- #### Mean Squared Error (MSE) Loss Function
The Mean Squared Error (MSE) loss function measures the difference between the predicted Q-values and the target Q-values, optimizing the model's parameters.

$$
L(\theta) = \mathbb{E} \left[ \left( y_i - Q(s, a; \theta) \right)^2 \right]
$$

Here, $$L(\theta)$$ represents the loss function, measuring the error between predicted and target Q-values. $$y_i$$ denotes the target Q-value computed using the Bellman equation. $$Q(s, a; \theta)$$ is the predicted Q-value for state $$s$$ and action $$a$$ .

---

- #### Epsilon-Greedy Policy
The Epsilon-Greedy policy balances exploration and exploitation by selecting random actions with probability \( \epsilon \) and optimal actions with probability \( 1 - \epsilon \).

$$
a = 
\begin{cases} 
\text{random action}, & \text{with probability } \epsilon \\
\arg\max_a Q(s, a; \theta), & \text{with probability } 1 - \epsilon
\end{cases}
$$

Here, $$a$$ represents the selected action. $$\epsilon$$ denotes the exploration rate, controlling the probability of random actions. $$Q(s, a; \theta)$$ is the Q-value for state $$s$$ and action $$a$$ , used to select the optimal action.

---

- #### Target Network Update Formula
The target network update formula improves training stability by periodically copying the weights from the main network to the target network.

$$
\theta^- \leftarrow \tau \theta + (1 - \tau) \theta^-
$$

Here, $$\theta$$ represents the parameters of the main network. $$\theta^-$$ denotes the parameters of the target network. $$\tau$$ is the interpolation factor, typically set to 1 for complete copying.

---

### 3. Experiments

Experiments were conducted using the SUMO simulator to evaluate the Dueling DQN-DNN algorithm in urban traffic scenarios. The model was trained on a simulated intersection with varying traffic densities, using vehicle queue lengths and waiting times as state inputs. Performance metrics included average delay, throughput, and congestion levels. Results showed that Dueling DQN-DNN outperformed traditional DQN and fixed-time traffic control methods, reducing average delays by up to 20%. The separated value and advantage streams enabled faster convergence, with the agent adapting effectively to dynamic traffic patterns. These findings validate the algorithm's efficacy in real-world traffic management applications.

### 4. Conclusions 
The Dueling DQN-DNN algorithm, integrated with SUMO (Simulation of Urban MObility), provides an efficient framework for traffic signal control by leveraging state-of-the-art reinforcement learning techniques. By decomposing Q-values into state value and advantage streams, the algorithm enhances decision-making in complex traffic scenarios. The DNN architecture enables the agent to process high-dimensional state representations from SUMO, such as vehicle positions and queue lengths. Through experience replay and target network updates, the model achieves stable and convergent learning. Combined with SUMO's realistic traffic simulation, this approach optimizes traffic flow, reduces congestion, and minimizes delays at intersections. Overall, Dueling DQN-DNN demonstrates strong potential for intelligent transportation systems.

