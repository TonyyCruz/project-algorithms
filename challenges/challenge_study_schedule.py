def study_schedule(permanence_period, target_time):
    active_users = 0
    try:
        for initial, final in permanence_period:
            if initial <= target_time and final >= target_time:
                active_users += 1
        return active_users
    except (TypeError, ValueError):
        return None
