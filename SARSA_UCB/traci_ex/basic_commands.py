import traci

def simulation_start(sumoCmd, port=8813, label="sim1"):
    """Initialize the simulation with traci"""
    traci.start(cmd=sumoCmd, port=port, label=label)
    print(traci.getVersion())


def simulation_step():
    """# Execute one simulation step"""
    traci.simulationStep()


def simulation_close():
    traci.close(wait=False)


def pre_run_simulation_to_prepare(pre_steps):
    """ pre run simulation with doing nothing"""
    traci.simulationStep(traci.simulation.getTime()+pre_steps)
    

def get_simulation_time():
    return traci.simulation.getTime()