# Get the logs that are above a certain time maxSpan
# ["30 100 sign-out", "30 10 sign-in", "40 20 sign-out", "40 0 sign-in"]



def get_logs(logs, maxSpan):

    user_times = {}

    for log in logs:

        parts = log.split()
        id, duration, action = parts[0], int(parts[1]), parts[2]
        if id in user_times:
            actions = user_times.get(id)
            if action == "sign-in":
                if action in actions: 
                    curr = actions["sign-in"]
                    if duration < curr:
                        actions["sign-in"] = duration
                else:
                    actions["sign-in"] = duration
            else:
                print("here")
                if action in actions:
                    curr = actions["sign-out"]
                    if duration > curr:
                        actions["sign-out"] = duration
                else:
                    actions["sign-out"] = duration
        else:
            actions = {}
            actions[action] = duration
            user_times[id] = actions

    print(user_times)  
    result = []

    for k, v in user_times.items():
        if "sign-out" in v:
            delta = v["sign-out"] - v["sign-in"]

            if delta <= maxSpan:
                result.append(k)
    result.sort()
    return result

logs = ["30 20 sign-out", "30 10 sign-in", "40 20 sign-out", "40 0 sign-in", "30 0 sign-in", "30 100 sign-out", "50 20 sign-in"]
print(get_logs(logs, 90))
            


                









