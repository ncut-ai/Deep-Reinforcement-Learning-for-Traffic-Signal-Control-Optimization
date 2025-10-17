import traci


def adjust_number(x):
    """Keep only the first two digits of the number, e.g., 2399, 2305 become 2400"""
    if 0 < x < 1:
        return round(x, 2)  # If the number is less than 1, round to two decimal places
    elif abs(x) < 100:
        return round(x)  # If the number is less than 100, round to the nearest integer
    else:
        return adjust_number(x / 10) * 10


def adjust_decorator(func):
    """Define a decorator"""

    def wrapper(*args):
        val = func(*args)
        val = adjust_number(val)
        return val

    return wrapper


@adjust_decorator
def get_interval_occ_on_e2(e2_id):
    """Retrieve interval occupancy from the E2 detector"""
    val = traci.lanearea.getLastIntervalOccupancy(detID=e2_id)
    return val


@adjust_decorator
def get_interval_speed_on_e2(e2_id):
    """Retrieve interval average speed from the E2 detector"""
    val = traci.lanearea.getLastIntervalMeanSpeed(detID=e2_id)
    return val


@adjust_decorator
def get_interval_vol_on_e2(e2_id):
    """Retrieve interval vehicle count from the E2 detector"""
    val = traci.lanearea.getLastIntervalVehicleNumber(detID=e2_id)
    return val


@adjust_decorator
def get_interval_jam_length_on_e2(e2_id):
    """Retrieve interval congestion length from the E2 detector"""
    val = traci.lanearea.getLastIntervalMaxJamLengthInMeters(detID=e2_id)
    return val


@adjust_decorator
def get_occ_on_e2(e2_id):
    """Retrieve last step occupancy from the E2 detector"""
    val = traci.lanearea.getLastStepOccupancy(detID=e2_id)
    return val


@adjust_decorator
def get_speed_on_e2(e2_id):
    """Retrieve last step average speed from the E2 detector"""
    val = traci.lanearea.getLastStepMeanSpeed(detID=e2_id)
    return val


@adjust_decorator
def get_vol_on_e2(e2_id):
    """Retrieve last step vehicle count from the E2 detector"""
    val = traci.lanearea.getLastStepVehicleNumber(detID=e2_id)
    return val


@adjust_decorator
def get_jam_length_on_e2(e2_id):
    """Retrieve last step congestion length from the E2 detector"""
    val = traci.lanearea.getJamLengthMeters(detID=e2_id)
    return val


def get_interval_time_loss_on_e3_as_reward(e3_id):
    """Retrieve time loss from the E3 detector as a reward, using its reciprocal"""
    val = traci.multientryexit.getLastIntervalMeanTimeLoss(detID=e3_id)
    if val == -1 or val == 0:
        return 0
    else:
        return 1 / (val)
