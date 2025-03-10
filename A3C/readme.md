# A3C

---

### Table of contents 
1. [Introduction](#1-introduction)
2. [Method](#2-method)
3. [Experiments](#3-experiments)
4. [Conclusions](#4-conclusions)

---
### 1. Introduction 
- A3C is a combination of the Actor-Critic framework with asynchronous training mechanisms, offering an advanced deep reinforcement learning algorithm. The core idea is to accelerate the learning process and enhance stability by having multiple parallel worker threads interact with the environment and update shared neural network parameters concurrently. Each thread independently executes policies, collects experiences, and updates weights to the global network at certain intervals. This method not only effectively avoids high variance issues common in traditional reinforcement learning but also significantly speeds up the learning process.

### 2. Method 

- #### Actor's Objective Function

The Actor's objective function combines the policy gradient loss and entropy regularization to optimize the policy. It maximizes the expected advantage while encouraging exploration through entropy.

$$
L_{\text{actor}} = \mathbb{E} \left[ \log \pi(a_t | s_t; \theta) A(s_t, a_t) - \beta H(\pi(s_t; \theta)) \right]
$$

Here, $$L_{\text{actor}}$$ is the objective function for the Actor. $$\pi(a_t | s_t; \theta)$$ denotes the probability distribution of taking action $$a_t$$ given state $$s_t$$. $$A(s_t, a_t)$$ is the advantage function that measures how much better it is to take action $$a_t$$. $$\beta$$ is the entropy regularization coefficient, and $$H(\pi(s_t; \theta))$$ is the entropy of the policy, encouraging exploration.

---

- #### Critic's Mean Squared Error Loss

The Critic's loss function measures the difference between the predicted state value and the n-step TD target. It minimizes the mean squared error to improve the accuracy of the value function estimation.

$$
L_{\text{critic}} = \mathbb{E} \left[ (R_t - V(s_t))^2 \right]
$$

Here, $$L_{\text{critic}}$$ is the loss function for the Critic. $$R_t$$ is the n-step TD target, representing the discounted cumulative reward starting from state $$s_t$$. $$V(s_t)$$ is the predicted value of state $$s_t$$ by the Critic model.

---

- #### n-step TD Target

The n-step TD target calculates the discounted cumulative reward starting from the current state, incorporating both immediate rewards and the estimated value of future states.

$$
R_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \dots + \gamma^n V(s_{t+n})
$$

Here, $$R_t$$ is the n-step TD target. $$r_t, r_{t+1}, \dots$$ are the immediate rewards at the current and future steps. $$\gamma$$ is the discount factor controlling the importance of future rewards. $$V(s_{t+n})$$ is the estimated value of state $$s_{t+n}$$.

---

- #### Advantage Function

The advantage function quantifies how much better it is to take a specific action compared to the average behavior. It is computed as the difference between the n-step TD target and the predicted state value.

$$
A(s_t, a_t) = R_t - V(s_t)
$$

Here, $$A(s_t, a_t)$$ is the advantage function measuring how much better it is to take action $$a_t$$. $$R_t$$ is the n-step TD target. $$V(s_t)$$ is the predicted value of state $$s_t$$ by the Critic model.

---

- #### Policy Gradient Update Rule

The policy gradient update rule adjusts the policy parameters by following the gradient of the log-probability of actions weighted by their advantages. This ensures that actions with higher advantages are more likely to be chosen in the future.

$$
\theta_{\text{actor}} \leftarrow \theta_{\text{actor}} + \alpha \nabla_\theta \log \pi_\theta(a|s) A(s,a)
$$

Here, $$\alpha$$ represents the learning rate, $$\pi_\theta(a|s)$$ denotes the probability distribution of taking action $$a$$ given state $$s$$, and $$A(s,a)$$ is the advantage function that measures how much better it is to take action $$a$$ compared to average behavior.

---

- #### Entropy Regularization Term

The entropy regularization term encourages exploration by penalizing deterministic policies. It measures the uncertainty or randomness of the policy distribution, promoting a balance between exploitation and exploration.

$$
H(\pi(s_t; \theta)) = -\sum_a \pi(a | s_t; \theta) \log \pi(a | s_t; \theta)
$$

Here, $$H(\pi(s_t; \theta))$$ is the entropy of the policy. $$\pi(a | s_t; \theta)$$ denotes the probability distribution of taking action $$a$$ given state $$s_t$$. $$a$$ is an action in the action space.

---

### 4. Conclusions 
When applying A3C to traffic signal control within SUMO, different agents can be set for various intersections. These agents use SUMO's API to obtain real-time traffic data (such as vehicle waiting times, queue lengths, etc.) as input states. Based on this information, agents decide when to switch the traffic light colors aiming to minimize total waiting time and optimize traffic flow. SUMO allows simulating complex traffic scenarios, enabling the A3C model to train and test under conditions close to the real world.
