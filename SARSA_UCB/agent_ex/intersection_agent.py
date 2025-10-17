import random
import pandas as pd
import numpy as np
import save_data.save_data as sd # 保存数据

class IntersectionAgent:
    """
    Intersection Agent Class
    Q-values are implemented using strings
    """

    def __init__(self, agent_setting, rl_setting):
        """Initialization"""
        print('Initializing Agent...')
        self.agent_id = agent_setting['cross_ids']  # agent_id denoted as cross id
        self.cross_id = self.agent_id
        self.tls_id = agent_setting['tls_ids']  # Traffic light id
        self.state_config = agent_setting['states']  # basic info about states of the agent
        self.action_config = agent_setting['actions']  # action config
        self.reward_config = agent_setting['rewards']  # reward config
        # Initialize basic parameters
        state_names = self.state_config['names']
        action_names = self.action_config['names']
        self.state_num = len(state_names)
        self.action_num = len(action_names)
        self.state_names = state_names
        self.action_names = action_names
        self.action_duration = [i[2] for _, i in self.action_config['paras'].items()]  # Action duration
        """Initialization"""
        print('RL learning...')
        self.learning_model = rl_setting['learning_model']  # basic parameters for RL algo
        self.action_selection_model = rl_setting['action_selection']  # action selection
        #
        self.q_table = self.__init_q_table_from_states_and_actions(state_names, action_names)  # initialize q table
        #
        self.state_action_count_table = self.__init_state_action_count_table_from_states_and_actions(state_names,
                                                                                                     action_names)  # State-action pair visit count table
        #
        self.state_prev = ""
        self.state_current = ""
        self.action_prev = random.choice(action_names)
        self.action_current = random.choice(action_names)
        self.action_prev_index = 0
        self.action_current_index = self.action_names = action_names
        self.reward_current = 0.0
        #
        """Record the current agent's action type and remaining duration of the current action"""
        self.current_strategy_remain_time = 0  # Remaining time for the current strategy; 0 means a new strategy is needed

    def __init_q_table_from_states_and_actions(self, state_name_list, action_name_list):
        """Create Q-table, initialized with zeros, dynamically expanding with added indices"""
        q_table = pd.DataFrame(0, index=[], columns=action_name_list)
        return q_table

    def __init_state_action_count_table_from_states_and_actions(self, state_name_list, action_name_list):
        """Create state-action visit count table to track occurrences of state-action pairs"""
        state_action_count_table = pd.DataFrame(1, index=[], columns=action_name_list)  # Initialized to 1
        return state_action_count_table

    def is_current_strategy_over(self):
        """Check if the current action has finished"""
        if self.current_strategy_remain_time == 0:
            return True  # The current action is completed
        else:
            return False

    def save_current_state(self, state_val):
        """Save the current state and store the previous state"""
        self.state_prev = self.state_current
        self.state_current = state_val

    def select_action(self):
        """Action selection using UCB algorithm"""
        state = self.state_current
        # check state in q table
        self.__check_state_exist(state)
        self.__check_state_exist_in_count_table(state)
        # Compute and select action
        action_selected = self.upper_confidence_bounds(state=state,
                                                  q_table=self.q_table,
                                                  state_action_count_table=self.state_action_count_table)
        # Increment count for the selected action
        self.__add_to_state_action_count_table_by(state=state, action=action_selected)
        action_index = self.action_names.index(action_selected)  # Get the index of the selected action
        # Save action and set the timer
        self.save_action_set_time_counter(action_index)

    def upper_confidence_bounds(self, state, q_table, state_action_count_table):
        """Implementation of the UCB algorithm"""
        q_state_action = q_table.loc[state, :]  # loc is used to retrieve the values of a specific column: it fetches all columns for the observation row in the q_table
        state_action_count = state_action_count_table.loc[state, :]  # Retrieve the counts for all actions of the current state
        # Compute UCB values using the formula
        equation_2nd_part = np.sqrt(np.log(np.sum(state_action_count)) / state_action_count)
        equation_final_result = equation_2nd_part - q_state_action
        #
        action_selected = np.random.choice(
            equation_final_result[equation_final_result == np.max(equation_final_result)].index)  # np.max（）：Get the maximum value along the row
        return action_selected

    def __add_to_state_action_count_table_by(self, state, action):
        """Increment the count for a specific state-action pair in the count table"""
        self.state_action_count_table.loc[state, action] += 1

    def save_action_set_time_counter(self, action_index):
        """Save action index, name, and set the timer"""
        self.action_prev_index = self.action_current_index
        self.action_current_index = action_index
        self.action_current = self.action_config['names'][action_index]
        # Set the action execution timer and remaining time
        self.current_strategy_remain_time = self.action_duration[action_index]

    def time_count_step(self):
        """Decrement the execution time of the current strategy by one step"""
        if self.current_strategy_remain_time > 0:
            self.current_strategy_remain_time -= 1
        else:  # Reset the timer to zero
            self.current_strategy_remain_time = 0

    def save_reward(self, val):
        """Save the current reward"""
        print(self.agent_id, '-REWARD:', val)
        self.reward_current = val
        sd.save_reward(self.agent_id, val)  # Save the reward value

    def __check_state_exist(self, state):
        """Check if the state exists in the Q table"""
        q_table_idx = self.q_table.index
        if q_table_idx.isin([state]).any():
            pass
        else:
            df = pd.DataFrame(0, index=[state], columns=self.action_names)
            self.q_table = pd.concat([self.q_table, df])  # Add the new state to the Q table

    def __check_state_exist_in_count_table(self, state):
        """Check if the state exists in the count table"""
        q_table_idx = self.state_action_count_table.index
        if q_table_idx.isin([state]).any():
            pass
        else:
            df = pd.DataFrame(1, index=[state], columns=self.action_names)  # Initialize count to 1
            self.state_action_count_table = pd.concat([self.state_action_count_table, df])  # Add the new state to the count table

    def update_q_table_SARSA(self):
        """Update the Q table using the SARSA algorithm"""
        self.__check_state_exist(self.state_prev)
        self.__check_state_exist(self.state_current)
        # Retrieve parameters
        alpha = self.learning_model['learning_rate']
        gamma = self.learning_model['gamma']
        #
        prev_q = self.q_table.loc[self.state_prev, self.action_prev]  # Get previous and current Q-values
        current_q = self.q_table.loc[self.state_current, self.action_current]
        # Update Q-value using the SARSA formula
        q_new = (1 - alpha) * prev_q + alpha * (self.reward_current + gamma * current_q)
        # Save the updated Q-value to the Q table
        self.q_table.loc[self.state_prev, self.action_current] = q_new
