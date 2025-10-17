# SARSA with UCB (SARSA-UCB)

## 1. Introduction

SARSA (State-Action-Reward-State-Action) is an on-policy, online Temporal Difference (TD) reinforcement learning algorithm. It directly learns an action-value function, Q(s,a), which represents the expected return for taking action 'a' in state 's' and thereafter following the current policy.

UCB (Upper Confidence Bound) is a classic exploration-exploitation balancing strategy, commonly used in multi-armed bandit problems. It encourages trying out arms (or actions) with high uncertainty or those that have been explored less frequently by adding a confidence bonus to their value estimates.

SARSA-UCB combines these two ideas: it uses SARSA as the primary learning update rule and employs a UCB-based strategy for action selection to effectively balance exploration and exploitation during the learning process.

## 2. Method

*   **SARSA Update Rule**:
    The core of SARSA is its Q-value update formula. After an agent takes action $a$ in state $s$, receives reward $r$, transitions to a new state $s'$, and then selects action $a'$ in $s'$ according to its current policy, the Q-value $Q(s,a)$ is updated as follows:
    $$
    Q(s,a) \leftarrow Q(s,a) + lpha \left[ r + \gamma Q(s',a') - Q(s,a) ight]
    $$
    Where:
    *   $lpha$ is the learning rate.
    *   $\gamma$ is the discount factor.
    *   The tuple $(s, a, r, s', a')$ gives SARSA its name. Because the update depends on the next state $s'$ and the next action $a'$ that will actually be taken in $s'$, it is an on-policy algorithm—it evaluates the policy it is currently executing.

*   **UCB Action Selection**:
    When selecting an action in state $s$, SARSA-UCB uses a UCB1-like approach instead of simple random exploration (like $\epsilon$-greedy). For each possible action $a_i$ in state $s$, a UCB value is calculated:
    $$
	ext{UCB}(s, a_i) = Q(s, a_i) + C \sqrt{rac{\ln N(s)}{N(s, a_i)}}
    $$
    The action with the highest UCB value is then chosen:
    $$
    a = rg\max_{a_i} 	ext{UCB}(s, a_i)
    $$
    Where:
    *   $Q(s, a_i)$ is the current estimate of the value of taking action $a_i$ in state $s$.
    *   $N(s)$ is the total number of times state $s$ has been visited (or the total number of decisions made so far).
    *   $N(s, a_i)$ is the number of times action $a_i$ has been selected in state $s$.
    *   $C$ is a positive constant, known as the exploration constant, which controls the degree of exploration: a larger $C$ encourages more exploration.

    **Handling $N(s, a_i) = 0$**: If an action $a_i$ has never been tried in state $s$ (i.e., $N(s, a_i)=0$), its UCB value is typically treated as infinite, ensuring it gets selected to encourage initial exploration of all actions.

    The UCB policy encourages exploration through its second term (the confidence bound). If an action has been chosen infrequently ($N(s, a_i)$ is small), or if the state $s$ has been visited many times ($N(s)$ is large), this term increases, thereby boosting the probability of that action being selected.

*   **Algorithm Flow**:
    1.  Initialize Q(s,a) table (e.g., to zeros or optimistically). Initialize $N(s)$ and $N(s,a)$ counters to 0.
    2.  Get the initial state $s$.
    3.  Select action $a$ from state $s$ using the UCB policy.
    4.  **Loop** (until terminal state or max steps):
        a.  Take action $a$, observe reward $r$ and new state $s'$.
        b.  Select next action $a'$ from state $s'$ using the UCB policy.
        c.  Update $Q(s,a)$: $Q(s,a) \leftarrow Q(s,a) + lpha \left[ r + \gamma Q(s',a') - Q(s,a) ight]$.
        d.  Increment counters: $N(s) \leftarrow N(s) + 1$, $N(s,a) \leftarrow N(s,a) + 1$.
        e.  $s \leftarrow s'$, $a \leftarrow a'$.
    5.  **End** loop.

## 3. Application in Traffic Signal Control

SARSA-UCB can be used to learn control policies for traffic signals.

*   **State (S)**:
    *   Typically a discretized representation of the traffic state, e.g., by categorizing queue lengths, vehicle arrival rates, etc., into several levels.
    *   Can also include the current signal phase, elapsed time in the phase, etc.
    *   Since UCB requires counts of state visits and state-action pair visits, highly continuous or high-dimensional state spaces might need state aggregation or function approximation, which complicates the direct application of UCB. If a Q-table is used directly, states must be discrete.

*   **Action (A)**:
    *   A discrete set of actions, such as selecting the next signal phase to activate or deciding whether to extend the current phase.

*   **Reward (R)**:
    *   Designed to reflect traffic efficiency, e.g., based on changes in waiting time, queue length, or throughput.

*   **Q-function and Counters**:
    *   For small state and action spaces, $Q(s,a)$, $N(s)$, and $N(s,a)$ can be stored in tabular form.
    *   For larger state spaces, function approximators might be needed for $Q(s,a)$, but accurately maintaining UCB counters $N(s)$ and $N(s,a)$ becomes difficult and may require hash-based approximate counting or other techniques.

## 4. Key Features and Considerations

*   **On-Policy**: SARSA learns the value of the policy it is currently executing, including its exploration steps.
*   **Exploration Mechanism**: UCB provides a more sophisticated exploration mechanism than $\epsilon$-greedy, guiding exploration based on uncertainty and favoring less-tried actions that have higher potential.
*   **Convergence**: SARSA is guaranteed to converge to the optimal policy under certain conditions (e.g., appropriate decay of the learning rate, infinite visits to all state-action pairs). UCB helps in systematically exploring these pairs.
*   **Sensitivity to Parameter C**: The exploration constant C in UCB significantly impacts performance and requires careful tuning.
*   **State/Action Space Size**: Traditional tabular SARSA-UCB is primarily suitable for small to medium-sized discrete state and action spaces. For larger problems, integration with function approximation is necessary, which can complicate the theoretical guarantees and implementation of UCB.

SARSA-UCB, by combining SARSA's online learning capability with UCB's intelligent exploration strategy, offers an effective solution for reinforcement learning problems, especially in scenarios requiring a careful balance between exploration and exploitation.