def get_difference_data(data_A: dict, data_B: dict) -> dict:

    result = {}

    for user, data in data_B.items():
        metadata = data["metadata"]
        achievements = {
            achievement: flag
            for achievement, flag in data["achievements"].items()
            if achievement not in data_A[user]["achievements"]
        }
        result[user] = {"metadata": metadata, "achievements": achievements}

    return result



if __name__ == "__main__":
    
    from api import get_data
    
    data_A = get_data()
    data_B = get_data()

    data_diff = get_difference_data(data_A=data_A, data_B=data_B)

    for user, data in data_diff.items():
        for achieve in data["achievements"]:
            if achieve in data_A[user]["achievements"]:
                print(f"User {user} failed.")
        else:
            print(f"User {user} passed.")
