from init.init_SARSA import *


if __name__ == '__main__':
    '''
    Initialize Agent and learning algorithm parameters
    '''
    tls_agents = initialize_agents_by(agent_setting,rl_setting)  #
    '''
        Start training episodes
    '''
    for ep in range(basic_setting['episode']):
        print('-------------Training Episode: ', ep, '-------------')
        start_env(sumo_cmd=basic_setting['sumo_start_config_cmd'])  # Initialize environment
        prerun_env(pre_steps=basic_setting['pre_steps'])  # Environment warm-up
        # Start running the simulation environment
        start_time = get_env_time()  # Time when the simulation environment starts
        while get_env_time() < start_time + basic_setting['simulation_time']:

            for agent in agent_setting.keys():  # Iterate through all agents
                # Check if the current action of the agent has been completed
                if tls_agents[agent].is_current_strategy_over() == False:  # Current action is still in progress...
                    continue  # If the agent's strategy has not been completed, skip this iteration
                # get_current_state(agent=tls_agents[agent])  # Get state
                # select_action(agent=tls_agents[agent])  # Select action
                # Deploy action into the environment
                deploy_action_into_env(agent=tls_agents[agent])
            # Execute one step of the simulation
            simulation_step()
            # Decrease the time counter of all agents' strategy execution by 1
            time_count_step(agent_list=tls_agents)
            # Iterate through all agents
            for agent in agent_setting.keys():
                # Check again if the current action of the agent has been completed
                if tls_agents[agent].is_current_strategy_over() == False:  # Current action is still in progress...
                    continue  # If the agent's strategy has not been completed, skip this iteration
                # Get state
                get_current_state(agent=tls_agents[agent])
                # Select action
                select_action(agent=tls_agents[agent])
                # Get reward
                get_reward(agent=tls_agents[agent])
                # Update Q-table
                update_q_table(agent=tls_agents[agent])

        # End of episode
        print("Episode ended：", ep)
        '''Close the simulation'''
        close_env()

        '''Save episode data'''
        sd.save_ep_data(ep=ep)

        '''Save SUMO output data'''
        save_sumo_output_data(ep)

    '''
    End of run, save data to file
    '''
    sd.save_data_to_file()

