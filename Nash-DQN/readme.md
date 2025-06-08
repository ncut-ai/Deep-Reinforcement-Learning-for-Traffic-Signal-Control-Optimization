# Nash-DQN (Nash Deep Q-Network)

## 1. Introduction

Nash Deep Q-Network (Nash-DQN) is a Multi-Agent Reinforcement Learning (MARL) algorithm that integrates the game theory concept of Nash Equilibrium with Deep Q-Networks (DQN). In MARL environments, especially when multiple agents coexist and their actions influence each other (e.g., multiple traffic signals controlling adjacent intersections), an agent's optimal decision depends not only on its own state but also on the strategies of other agents. Nash-DQN aims to find a stable joint policy in such interactive settings.

Traditional single-agent DQN learns a Q-function $Q(s,a)$ to maximize its own cumulative reward. However, directly applying single-agent DQN in multi-agent systems can fail to converge to desirable solutions because the environment becomes non-stationary from each agent's perspective (as other agents' policies change during learning).

The core idea of Nash-DQN is that, when updating Q-values or selecting actions, it considers a Nash Equilibrium point among all agents in the current state, rather than just maximizing an individual agent's Q-value. This means each agent's chosen action is its best response to the actions taken by other agents under the Nash Equilibrium.

## 2. Method

Nash-DQN extends the traditional DQN framework primarily by incorporating Nash Equilibrium computation into the Q-value update target calculation and/or the action selection phase.

*   **Network Architecture**:
    *   Each agent $i$ typically has its own Deep Q-Network $Q_i(s, a_i, \mathbf{a}_{-i}; 	heta_i)$ or $Q_i(s, \mathbf{a}; 	heta_i)$, where $s$ is the global state or local observation, $a_i$ is agent $i$'s action, $\mathbf{a}_{-i}$ is the joint action of all other agents, and $\mathbf{a}$ is the joint action of all agents.
    *   The network takes the state as input and outputs the Q-values for each possible action $a_i$ of agent $i$. These Q-values may depend on the actions of other agents.

*   **Q-Value Update**:
    The standard DQN loss function for agent $i$ is:
    $$
    L(	heta_i) = \mathbb{E} \left[ (y_i - Q_i(s, a_i; 	heta_i))^2 ight]
    $$
    where the target value $y_i = r_i + \gamma \max_{a'} Q_i(s', a'; 	heta_i^-)$.

    In Nash-DQN, the calculation of the target value $y_i$ is modified. Instead of simply maximizing over agent $i$'s action space, it is based on the Q-values at the Nash Equilibrium in the next state $s'$.
    $$
    y_i = r_i + \gamma 	ext{NashQ}_i(s', \mathbf{Q_1}(s', \cdot), \dots, \mathbf{Q_N}(s', \cdot); 	heta_1^-, \dots, 	heta_N^-)
    $$
    More specifically:
    $$
    y_i = r_i + \gamma Q_i(s', a_1^*, \dots, a_N^*; 	heta_i^-)
    $$
    where $(a_1^*, \dots, a_N^*)$ is the Nash Equilibrium joint action in state $s'$, calculated based on all agents' target Q-networks $Q_j(\cdot; 	heta_j^-)$. $	ext{NashQ}_i(s', \cdot)$ denotes the Nash Equilibrium Q-value for agent $i$ in state $s'$, obtained by solving a game defined by the current Q-functions of all agents (usually their target networks).

*   **Solving for Nash Equilibrium**:
    *   At each step requiring the target Q-value (or during action selection), the algorithm needs to construct a game for the current state (or next state $s'$).
    *   The players in this game are all $N$ agents.
    *   The payoff for each agent $j$ is given by its Q-function $Q_j(s', a_1, \dots, a_N)$.
    *   A Nash Equilibrium solver (e.g., Lemke-Howson algorithm for two-player games, or other iterative methods for N-player games) is needed to find a Nash Equilibrium strategy profile $(\pi_1^*(s'), \dots, \pi_N^*(s'))$ or a pure-strategy Nash Equilibrium action profile $(a_1^*, \dots, a_N^*)$ for that state.
    *   If a mixed-strategy Nash Equilibrium is found, the Nash Q-value is the expected Q-value under this mixed strategy.
    *   **Challenge**: Solving for Nash Equilibrium can be computationally expensive, especially as the number of agents and actions increases. Practical implementations might use approximate solvers or assumptions about the game type (e.g., zero-sum, cooperative) to simplify this.

*   **Action Selection**:
    *   During execution, agent $i$ can also select actions based on a Nash Equilibrium analysis for the current state $s$. Alternatively, for simplification, an $\epsilon$-greedy strategy can be used, where the "greedy" part involves selecting the action that maximizes its individual Q-value, assuming other agents follow their current policies or some equilibrium strategy.

*   **Experience Replay** and **Target Networks**:
    *   Nash-DQN also employs experience replay and target networks to stabilize the learning process, similar to standard DQN.

## 3. Application in Traffic Signal Control

Nash-DQN is suitable for scenarios where multiple traffic signals act as interacting agents.

*   **Agents**: Each intersection's traffic signal is an agent.
*   **State (S)**:
    *   Can be local observations for each agent (e.g., queue lengths, traffic flow, current phase at its own intersection) potentially augmented with information from neighboring intersections.
    *   Could also be a global state encompassing all relevant intersections.
*   **Action (A)**: The action for each traffic signal agent is to choose the next signal phase (a discrete action space).
*   **Reward (R)**:
    *   Can be based on local metrics (e.g., reduction in average vehicle waiting time at its own intersection).
    *   Can also be based on global or regional metrics (e.g., reduction in total waiting time for all vehicles in an area) to promote cooperation.
*   **Game Formulation**:
    *   In a given state, the combination of phases chosen by each signal light leads to different systemic or local outcomes (e.g., total waiting time). These outcomes (or their Q-value estimates) form the payoff matrix for the game.
    *   The algorithm seeks a combination of phase choices where no single traffic light can improve its (individual or common) reward by unilaterally changing its phase selection – this is the Nash Equilibrium point.

## 4. Key Features and Challenges

*   **Multi-Agent Coordination**: Explicitly models the strategic interactions between agents, aiming for stable joint policies.
*   **Game Theory Foundation**: Combines reinforcement learning with the concept of Nash Equilibrium.
*   **Applicability**: Suited for scenarios with multiple interacting decision-makers requiring decentralized or distributed control.
*   **Computational Complexity**: Solving for Nash Equilibrium is a major bottleneck, especially with many agents or large action spaces.
*   **Uniqueness/Multiplicity of Equilibria**: A game may have multiple Nash Equilibria, and the choice of which equilibrium to target can affect learning outcomes.
*   **Dependence on Model Accuracy**: Although model-free RL, the game formulation relies on accurate Q-value estimates, which indirectly reflect environmental dynamics.

Nash-DQN offers a theoretically sounder approach to learning in multi-agent environments, but its practical application often requires simplifications or approximations for the Nash Equilibrium computation.