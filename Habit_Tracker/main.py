from datetime import datetime
from habit_tool import break_habit
import pandas as pd
from tabulate import tabulate

habits = [
    break_habit('Coffee', datetime(2024, 5, 15, 9, 48), cost_per_day=2, minutes_wasted=15),
    break_habit('Gambling', datetime(2022, 7, 15, 9, 48), cost_per_day=10, minutes_wasted=60),
    break_habit('Smoke', datetime(2024, 5, 15, 9, 48), cost_per_day=2, minutes_wasted=15),
]

df = pd.DataFrame(habits)

print(tabulate(df, headers='keys', tablefmt='psql'))