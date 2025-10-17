import traci

def switch_to_tls_program(*args):
    """Switch to the specified traffic light control program"""
    tls_id = args[0][0]
    p_id = args[0][1]
    traci.trafficlight.setProgram(tlsID=tls_id,programID=p_id)

def multi_junctions_switch_to_tls_program(*args):
    """Switch traffic light control programs for multiple intersections simultaneously"""
    tls_ids = args[0][0]
    p_id = args[0][1]
    for tls_id in tls_ids:
        traci.trafficlight.setProgram(tlsID=tls_id,programID=p_id)