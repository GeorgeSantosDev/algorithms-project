def validate_data(entry, exit):
    return isinstance(entry, str) or isinstance(exit, str) or entry == None or exit == None or entry > exit or entry < 0 or exit < 0


def study_schedule(permanence_period, target_time):
    if target_time == None:
        return None
    
    counter = 0
    
    for entry, exit in permanence_period:
        if validate_data(entry, exit):
            return None
        
        if entry <= target_time and exit >= target_time:
            counter += 1
    
    return counter
