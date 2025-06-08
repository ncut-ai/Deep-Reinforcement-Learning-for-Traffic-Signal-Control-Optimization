# Nash-QL (Nash Q-Learning)

## 1. Introduction

Nash Q-Learning (Nash-QL) is a Multi-Agent Reinforcement Learning (MARL) algorithm that combines the game theory concept of Nash Equilibrium with traditional Q-Learning. In environments where multiple agents coexist and their actions are interdependent (e.g., multiple traffic signals managing traffic flow), Nash-QL aims for each agent to make decisions by considering not only its own Q-values but also the Nash Equilibrium behavior of other agents, thereby hoping to achieve a stable joint policy.

Unlike single-agent Q-learning, Nash-QL explicitly addresses the non-stationarity of the environment caused by other agents' changing policies. It assumes agents interact in a shared (or partially observable) state, where each agent's rewards and state transitions can be affected by the actions of others.

## 2. Method

The core of Nash-QL lies in modifying the Q-value update rule of traditional Q-learning, specifically by incorporating the solution of a Nash Equilibrium when calculating the target Q-value.

*   **Q-Table or Q-Function**:
    *   In its simplest form (e.g., for small, discrete state and action spaces), each agent $i$ maintains a Q-table $Q_i(s, a_1, \dots, a_N)$, storing the expected return for agent $i$ when the joint action $(a_1, \dots, a_N)$ is taken in the joint state $s$.
    *   For more complex state spaces, function approximation (e.g., linear functions or simple neural networks) can be used to represent $Q_i(s, \mathbf{a})$, where $\mathbf{a} = (a_1, \dots, a_N)$ is the joint action.

*   **Q-Value Update**:
    The traditional Q-learning update rule is:
    $$
    Q(s,a) \leftarrow Q(s,a) + lpha \left( r + \gamma \max_{a'} Q(s',a') - Q(s,a) ight)
    $$
    In Nash-QL, for agent $i$, the update rule for its Q-function $Q_i(s, \mathbf{a})$ becomes:
    $$
    Q_i(s, \mathbf{a}) \leftarrow (1-lpha)Q_i(s, \mathbf{a}) + lpha \left( r_i + \gamma 	ext{NashQ}_i(s', \mathbf{Q_1}(s', \cdot), \dots, \mathbf{Q_N}(s', \cdot)) ight)
    $$
    Where:
    *   $lpha$ is the learning rate.
    *   $r_i$ is the immediate reward received by agent $i$ after joint action $\mathbf{a}$ is taken in state $s$.
    *   $\gamma$ is the discount factor.
    *   $s'$ is the next state.
    *   $	ext{NashQ}_i(s', \cdot)$ represents the Nash Equilibrium Q-value for agent $i$ in the next state $s'$. This value is derived by solving an N-player game defined by the current Q-functions (or stable versions like target Q-tables) $Q_1, \dots, Q_N$ for all agents at state $s'$. A payoff matrix (formed by Q-values for different joint actions) is constructed for state $s'$, and a Nash Equilibrium point $(a_1^*, \dots, a_N^*)$ is found. $	ext{NashQ}_i(s', \cdot)$ is then $Q_i(s', a_1^*, \dots, a_N^*)$ at this equilibrium.

*   **Solving for Nash Equilibrium**:
    *   This is a critical computational step in Nash-QL. For each next state $s'$, a stage game defined by the current Q-functions $Q_j(s', \cdot)$ of all agents $j$ must be constructed.
    *   Algorithms like Lemke-Howson for two-player games, or more complex methods for N-player games (e.g., iterative best response, variations of fictitious play, or solvers for specific game structures) are needed to compute a Nash Equilibrium.
    *   The computed Nash Equilibrium can be a pure strategy (each agent selects a deterministic action) or a mixed strategy (each agent selects actions probabilistically).
    *   **Challenge**: Computing Nash Equilibria is computationally intensive, especially with many agents or large action spaces.

*   **Action Selection**:
    *   During learning, agent $i$ selects action $a_i$ in the current state $s$ using an $\epsilon$-greedy strategy.
    *   The "greedy" part involves selecting the action that maximizes its Q-value within the Nash Equilibrium computed for state $s$. This also requires solving for a Nash Equilibrium.
    *   Alternatively, for simplification, individual Q-value maximization can be used, assuming other agents follow fixed or learned policies.

## 3. Application in Traffic Signal Control

Nash-QL can be applied to control multiple interdependent traffic signals.

*   **Agents**: Each intersection's traffic signal is an independent agent.
*   **State (S)**: Can be the local state of each intersection (e.g., queue lengths, waiting vehicles, current phase) or a combined state including information from neighboring intersections.
*   **Action (A)**: The action for each agent (signal) is to choose the next signal phase (typically discrete).
*   **Reward (R)**:
    *   Can be designed as a local reward (e.g., based on waiting time reduction at its own intersection).
    *   Can also be a global reward or one that considers neighborhood impact, to foster cooperation or manage competition, depending on the game setup (e.g., fully cooperative, fully competitive, or general-sum game).
*   **Game Model**:
    *   At each decision point, each signal chooses an action (phase). The combination of these actions jointly determines the next state of the overall (or local) traffic system and the reward each signal receives.
    *   Nash-QL attempts to find a stable combination of phase selection strategies such that no signal can unilaterally change its phase choice to improve its expected return (in the equilibrium sense).

## 4. Key Features and Challenges

*   **Multi-Agent Decision Making**: Explicitly models the strategic interdependencies among agents.
*   **Game Theory Foundation**: Central to the algorithm is the integration of Q-learning with Nash Equilibrium computation.
*   **Convergence**: Convergence of Nash-QL is more challenging to guarantee than single-agent Q-learning. It may converge to any of multiple Nash Equilibria or, in some cases (especially in general-sum games with function approximation), may not converge.
*   **Computational Cost**: The computation of Nash Equilibria is the primary bottleneck, particularly for systems with many agents and complex action spaces.
*   **Information Requirement**: To solve for Nash Equilibrium, an agent might need to know the Q-functions (or at least the actions or policies) of other agents, which can pose communication or observability challenges.

Nash-QL provides a robust theoretical framework for addressing cooperation and competition in multi-agent environments. However, its practical application in complex systems like large traffic networks often necessitates simplifications, such as using approximate Nash Equilibrium solvers or applying it to smaller clusters of agents.