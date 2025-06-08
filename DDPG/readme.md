# DDPG (Deep Deterministic Policy Gradient)

## 1. Introduction

Deep Deterministic Policy Gradient (DDPG) is a model-free, off-policy Actor-Critic algorithm for reinforcement learning in continuous action spaces. It combines ideas from Deep Q-Networks (DQN) and Deterministic Policy Gradients (DPG), enabling effective policy learning in environments with continuous actions.

The core idea of DDPG is to concurrently learn a Q-function (Critic) and a policy (Actor). The Critic evaluates the quality (Q-value) of taking a certain action in a given state, while the Actor learns a deterministic policy that outputs the optimal action based on the Critic's evaluation.

## 2. Method

DDPG involves two main neural networks: an Actor network and a Critic network. Additionally, to stabilize the training process, DDPG maintains corresponding target networks for both.

*   **Actor Network ($\mu(S; 	heta^\mu)$)**:
    *   **Role**: Learns a deterministic policy that maps a state $S$ directly to a specific action $A$.
    *   **Input**: State $S$.
    *   **Output**: A deterministic action $A = \mu(S; 	heta^\mu)$.
    *   **Update**: The Actor network's parameters $	heta^\mu$ are updated by maximizing the Q-value provided by the Critic network, using a policy gradient method. The objective is to make the Actor output actions that receive higher Q-values from the Critic. The gradient of the objective function $J$ can be approximated as:
        $$

abla_{	heta^\mu} J pprox \mathbb{E}_{s_t \sim \mathcal{D}} \left[
abla_a Q(s, a; 	heta^Q)|_{s=s_t, a=\mu(s_t)}
abla_{	heta^\mu} \mu(s; 	heta^\mu)|_{s=s_t} ight]
        $$
        Simply put, the Actor network is updated in the direction that increases the Q-values.

*   **Critic Network ($Q(S, A; 	heta^Q)$)**:
    *   **Role**: Learns an action-value function (Q-function) that estimates the expected return for taking action $A$ in state $S$.
    *   **Input**: State $S$ and Action $A$.
    *   **Output**: Q-value $Q(S, A; 	heta^Q)$.
    *   **Update**: The Critic network's parameters $	heta^Q$ are updated by minimizing the Mean Squared Bellman Error (MSBE), similar to Q-Learning. Its loss function is:
        $$
        L(	heta^Q) = \mathbb{E}_{(s_t, a_t, r_t, s_{t+1}) \sim \mathcal{D}} \left[ \left( Q(s_t, a_t; 	heta^Q) - y_t ight)^2 ight]
        $$
        where $y_t$ is the target Q-value, calculated as:
        $$
        y_t = r_t + \gamma Q'(s_{t+1}, \mu'(s_{t+1}; 	heta^{\mu'}); 	heta^{Q'})
        $$
        $Q'$ and $\mu'$ are the target Critic network and target Actor network, respectively. $\mathcal{D}$ is the experience replay buffer.

*   **Target Networks**:
    *   DDPG maintains a target network for both the Actor ($\mu'(S; 	heta^{\mu'})$) and the Critic ($Q'(S, A; 	heta^{Q'})$).
    *   The parameters of the target networks are periodically and slowly updated from the main network parameters using "soft updates" (Polyak averaging):
        $$
		heta' \leftarrow 	au 	heta + (1-	au) 	heta'
        $$
        where $	au \ll 1$ (e.g., $	au = 0.001$ or $0.005$). This makes the calculation of target Q-values more stable, thus improving the stability of the overall learning process.

*   **Experience Replay**:
    *   DDPG uses an experience replay buffer $\mathcal{D}$ to store transitions $(s_t, a_t, r_t, s_{t+1}, 	ext{done})$ generated from the agent's interaction with the environment.
    *   During training, mini-batches of experience are randomly sampled from this buffer to update the Actor and Critic networks. This helps to break correlations between data samples and improves learning efficiency and stability.

*   **Exploration**:
    *   Since DDPG learns a deterministic policy, sufficient exploration is crucial. This is typically achieved by adding noise to the Actor's output actions during training.
    *   Commonly used noise includes time-correlated Ornstein-Uhlenbeck (OU) noise or simpler zero-mean Gaussian noise.
    *   $A_t = \mu(S_t; 	heta^\mu) + \mathcal{N}_t$
    *   During testing or evaluation, no noise is added, and the deterministic actions from the Actor network are used directly.

## 3. Application in Traffic Signal Control

DDPG is well-suited for traffic signal control problems where the action space is continuous, such as directly controlling the duration of green lights.

*   **State (S)**: Similar to other RL algorithms, can include:
    *   Queue lengths and waiting times for each lane.
    *   Detector data (vehicle counts, occupancy).
    *   Current signal phase and elapsed time in that phase.

*   **Action (A)**: DDPG's main advantage lies in handling continuous actions. In traffic control, actions could be:
    *   **Direct control of green light duration for the next phase**: e.g., outputting a continuous value within a [min, max] range representing the duration.
    *   **Control of parameters for phase switching thresholds**: e.g., adjusting a continuous parameter that determines when to switch phases.
    *   Note: If DDPG is used for selecting discrete phases, its output needs additional processing (e.g., applying argmax to multiple output nodes, where each node represents a Q-value estimate for a phase—though this is closer to DQN's approach; DDPG's Actor typically outputs the action directly). If DDPG in this codebase is used for discrete phase selection, the design of its Actor's output layer and action selection mechanism warrants special attention.

*   **Reward (R)**: Designed to optimize traffic flow, for example:
    *   Minimizing average vehicle delay or waiting time.
    *   Maximizing intersection throughput.
    *   Reducing queue lengths.

*   **Network Structure**:
    *   Both Actor and Critic typically use Deep Neural Networks (DNNs), such as MLPs.
    *   The Actor network's output layer activation function should be chosen based on the action range (e.g., `tanh` can scale output to [-1, 1], which can then be linearly transformed to the actual action range).
    *   The Critic network takes state and action as input and outputs a single Q-value.

## 4. Pseudocode Outline

1.  Initialize Actor network $\mu(S; 	heta^\mu)$ and Critic network $Q(S, A; 	heta^Q)$ with parameters $	heta^\mu, 	heta^Q$.
2.  Initialize target networks $\mu'$ and $Q'$ with parameters $	heta^{\mu'} \leftarrow 	heta^\mu$, $	heta^{Q'} \leftarrow 	heta^Q$.
3.  Initialize experience replay buffer $\mathcal{D}$.
4.  **Loop** for each episode:
5.  &nbsp;&nbsp;&nbsp;&nbsp;Initialize exploration noise (e.g., OU noise or Gaussian noise).
6.  &nbsp;&nbsp;&nbsp;&nbsp;Receive initial state $S_1$.
7.  &nbsp;&nbsp;&nbsp;&nbsp;**Loop** for each step $t=1, T$:
8.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select action $A_t = \mu(S_t; 	heta^\mu) + \mathcal{N}_t$ based on current policy and exploration noise.
9.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Execute action $A_t$, observe reward $R_t$ and new state $S_{t+1}$.
10. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store transition $(S_t, A_t, R_t, S_{t+1}, 	ext{done})$ in $\mathcal{D}$.
11. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Randomly sample a mini-batch of $N$ transitions $(S_i, A_i, R_i, S_{i+1}, 	ext{done}_i)$ from $\mathcal{D}$.
12. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate target Q-values: $y_i = R_i + \gamma (1-	ext{done}_i) Q'(S_{i+1}, \mu'(S_{i+1}; 	heta^{\mu'}); 	heta^{Q'})$.
13. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update Critic network by minimizing the loss: $L = rac{1}{N} \sum_i (y_i - Q(S_i, A_i; 	heta^Q))^2$.
14. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update Actor network using the sampled policy gradient: $
abla_{	heta^\mu} J pprox +rac{1}{N} \sum_i
abla_A Q(S_i, A; 	heta^Q)|_{A=\mu(S_i)}
abla_{	heta^\mu} \mu(S_i; 	heta^\mu)$.
15. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Soft update target networks:
    $$
	heta^{Q'} \leftarrow 	au 	heta^Q + (1-	au) 	heta^{Q'}
    $$
    $$
	heta^{\mu'} \leftarrow 	au 	heta^\mu + (1-	au) 	heta^{\mu'}
    $$
16. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$S_t \leftarrow S_{t+1}$.
17. &nbsp;&nbsp;&nbsp;&nbsp;**End** inner loop.
18. **End** outer loop.

## 5. Key Features

*   **Off-Policy**: Can learn from old data in the experience replay buffer.
*   **Deterministic Policy**: The Actor outputs deterministic actions rather than a probability distribution over actions.
*   **Continuous Action Spaces**: Natively supports continuous action spaces, a key advantage over DQN.
*   **Actor-Critic Architecture**: Simultaneously learns a policy (Actor) and a value function (Critic).
*   **Target Networks and Soft Updates**: Enhance learning stability.
