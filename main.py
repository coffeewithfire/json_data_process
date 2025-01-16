from api import get_data
from utils import get_difference_data
import json


data_A = get_data()
data_B = get_data()

data_diff = get_difference_data(data_A=data_A, data_B=data_B)


with open("data.json", "w") as file:
    json.dump(data_diff, file)