The Actor-Critic (AC) algorithm combines policy networks and value networks to address problems in both continuous and discrete action environments. It learns the optimal policy through the policy network while optimizing the value network, solving the policy optimization problem. The characteristics of the AC algorithm include utilizing complete observational information, no need for internal modeling of the environment, effectively balancing exploration and exploitation, and it is applicable to fields such as robot control and image recognition.

Basic Principle of AC Algorithm
The AC algorithm consists of two core components:

Actor: Responsible for learning and representing the policy function π(a|s). The Actor network outputs the probability distribution of action a based on the current state s.
Critic: Responsible for learning and representing the state value function V(s) or action value function Q(s,a). The Critic network predicts the expected value of cumulative discounted rewards based on the current state s and the action a taken.
The Actor network and Critic network learn interactively and optimize step by step, with the Critic network providing feedback signals to guide the Actor network to adjust the policy in a direction that can achieve higher rewards. This coupled learning approach allows the AC algorithm to maintain the convergence of policy gradient algorithms while significantly improving learning efficiency.

### Application in Traffic Signal Control

In Traffic Signal Control (TSC), the Actor-Critic (AC) method is employed to enable traffic lights (as agents) to learn optimal timing strategies.

*   **State (S)**: Typically includes real-time traffic information at an intersection, such as:
    *   Queue length of vehicles in each approach lane.
    *   Number of vehicles detected by sensors.
    *   Average waiting time of vehicles.
    *   Current signal phase.
    *   Elapsed time in the current phase.

*   **Action (A)**: The agent's action is usually to select the next signal phase to switch to, or to decide whether to extend the current phase. For instance, at a typical four-phase intersection, an action could be choosing one of the four phases.

*   **Reward (R)**: The design of the reward function is crucial and directly impacts the agent's learning effectiveness. The goal is generally to minimize congestion. Common reward functions include:
    *   Negative cumulative vehicle waiting time: $-\sum w_i$ (where $w_i$ is the waiting time of each vehicle).
    *   Negative cumulative queue length: $-\sum q_l$ (where $q_l$ is the queue length of each lane).
    *   Change in system throughput: e.g., the number of vehicles passing through the intersection per unit time.
    *   Reduction in intersection pressure, where pressure can be defined as the difference between the number of incoming and outgoing vehicles.

*   **Actor Network**:
    *   **Input**: Current state S.
    *   **Output**: A probability distribution over actions $\pi(A|S; 	heta_{	ext{actor}})$. For example, if the action is to select the next phase, the Actor outputs the probability of switching to each possible phase.
    *   **Objective**: To learn a policy that maximizes cumulative rewards.

*   **Critic Network**:
    *   **Input**: Current state S (and sometimes action A, depending on whether the Critic estimates the state-value function V(S) or the state-action value function Q(S,A)).
    *   **Output**: An evaluation of the value of the current state (or state-action pair), $V(S; 	heta_{	ext{critic}})$ or $Q(S,A; 	heta_{	ext{critic}})$۔ This value represents the expected cumulative reward obtainable from the current state by following the Actor's policy.
    *   **Objective**: To accurately evaluate the quality of the policy chosen by the Actor, typically updated by minimizing the Temporal Difference (TD) error: $R_t + \gamma V(S_{t+1}) - V(S_t)$.

*   **Network Structure**: Both Actor and Critic often use Deep Neural Networks (DNNs), such as Multi-Layer Perceptrons (MLPs). The input layer corresponds to state features, followed by several hidden layers, and an output layer corresponding to the policy (Actor) or value (Critic).

### Boltzmann Exploration

This AC implementation specifically mentions the use of **Boltzmann Exploration**. This is a probability-based exploration strategy used to balance exploration (trying new actions) and exploitation (choosing the currently known best action) during the learning process.

The probability of selecting action $a$ in state $s$, $\pi(a|s)$, is typically given by the Boltzmann (or Softmax) distribution:

$$
\pi(a|s) = rac{e^{Q(s,a)/	au}}{\sum_{b \in A} e^{Q(s,b)/	au}}
$$

Where:
*   $Q(s,a)$ is the agent's estimate of the value of taking action $a$ in state $s$ (often derived from the Actor's output or combined with the Critic's evaluation).
*   $	au$ (tau) is a positive parameter called "temperature."
    *   When $	au$ is high, the probabilities of selecting any action become more uniform, and the agent tends to explore more.
    *   When $	au$ is low, actions with higher $Q(s,a)$ values have a much greater probability of being selected, and the agent tends to exploit its learned optimal policy.
    *   Often, $	au$ is gradually decreased (annealed) as training progresses, encouraging more exploration in the early stages and more exploitation later.

Compared to strategies like $\epsilon$-greedy, Boltzmann exploration adjusts selection probabilities based on the value estimates of actions, rather than choosing non-optimal actions completely at random, which can be more efficient in some scenarios.
