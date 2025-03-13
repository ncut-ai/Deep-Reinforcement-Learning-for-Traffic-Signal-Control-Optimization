# DDQN-DNN

---

### Table of contents 
1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

---

### 1. Introduction 
- DDQN-DNN (Double Deep Q-Network with Deep Neural Networks) is an advanced reinforcement learning algorithm that combines Double Q-learning with deep neural networks to improve stability and performance. It addresses the overestimation issue in traditional DQN by decoupling action selection and evaluation, using two separate networks for more accurate Q-value estimation. The DNN component allows the model to handle high-dimensional state spaces, making it suitable for complex environments. By leveraging experience replay and target networks, DDQN-DNN enhances learning efficiency and convergence. This approach is widely used in applications like game playing and robotics.

### 2. Method 

- #### Q-Learning Update Formula
Q-Learning is the foundational update formula in reinforcement learning, used to compute the target Q-value.

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

Here, $$Q(s, a)$$ is the Q-value for state $$s$$ and action $$a$$. $$r$$ is the immediate reward received after taking action $$a$$ in state $$s$$. $$\gamma$$ is the discount factor that determines the importance of future rewards. $$\max_{a'} Q(s', a')$$ is the maximum Q-value for the next state $$s'$$ over all possible actions $$a'$$. $$\alpha$$ is the learning rate that controls the step size of the update.

---

- #### Double DQN Improvement Formula
Double DQN reduces overestimation bias by decoupling action selection and Q-value evaluation.

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma Q_{\text{target}}(s', \arg\max_{a'} Q_{\text{main}}(s', a')) - Q(s, a) \right]
$$

Here, $$Q_{\text{main}}(s', a')$$ is the Q-value predicted by the main network to select the best action $$a'$$. $$Q_{\text{target}}(s', a')$$ is the Q-value predicted by the target network to evaluate the selected action. This separation minimizes overestimation bias in Q-values.

---

- #### Loss Function Formula
The loss function measures the difference between the predicted Q-value and the target Q-value, typically using Mean Squared Error (MSE).

$$
\text{Loss} = \frac{1}{N} \sum_{i=1}^N \left( y_i - Q(s_i, a_i) \right)^2
$$

Here, $$y_i = r + \gamma Q_{\text{target}}(s', \arg\max_{a'} Q_{\text{main}}(s', a'))$$ is the target Q-value. $$Q(s_i, a_i)$$ is the predicted Q-value for state $$s_i$$ and action $$a_i$$. $$N$$ is the batch size used in training.

---

- #### Target Network Update Formula
The target network's weights are periodically updated from the main network to stabilize training.

$$
\theta_{\text{target}} \leftarrow \tau \theta_{\text{main}} + (1 - \tau) \theta_{\text{target}}
$$

Here, $$\theta_{\text{main}}$$ represents the weights of the main network, and $$\theta_{\text{target}}$$ represents the weights of the target network. $$\tau$$ is the interpolation parameter that controls how much of the main network's weights are copied to the target network. In your implementation, $$\tau = 1$$, meaning a direct copy.

---

- #### ε-Greedy Action Selection Formula
The ε-Greedy strategy balances exploration and exploitation by selecting random actions with probability $$\epsilon$$ and the best-known action otherwise.

$$
a =
\begin{cases}
\text{random action}, & \text{with probability } \epsilon \\
\arg\max_a Q(s, a), & \text{otherwise}
\end{cases}
$$

Here, $$a$$ is the selected action. With probability $$\epsilon$$, a random action is chosen to encourage exploration. Otherwise, the action with the highest Q-value $$\arg\max_a Q(s, a)$$ is selected for exploitation.

### 3. Experiments

To evaluate the DDQN-DNN algorithm, we conducted experiments using SUMO (Simulation of Urban MObility) to simulate urban traffic environments. The model was trained to optimize traffic signal control, with the state space including vehicle density and queue lengths, and the action space consisting of phase switching decisions. Over multiple episodes, DDQN-DNN demonstrated faster convergence and reduced average waiting times compared to traditional DQN, owing to its improved Q-value estimation. The integration with SUMO showcased its ability to adapt to dynamic traffic patterns, effectively minimizing congestion in simulated urban scenarios. These results validate the algorithm's efficacy in real-world-inspired traffic management tasks.

### 4. Conclusions 
In conclusion, the DDQN-DNN algorithm effectively addresses the overestimation issue of traditional DQN by decoupling action selection and evaluation, leading to more stable and accurate Q-value predictions. When integrated with SUMO (Simulation of Urban MObility), DDQN-DNN demonstrates its capability to optimize traffic signal control by learning adaptive policies that minimize congestion and improve traffic flow. The use of experience replay and target networks further enhances training stability, making it suitable for dynamic and complex urban traffic scenarios simulated in SUMO. This combination highlights the potential of reinforcement learning in intelligent transportation systems.
