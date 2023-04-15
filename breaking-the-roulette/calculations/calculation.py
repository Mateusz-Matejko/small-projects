import json
import pprint
import pandas
from app import db, Roulette
import csv_creation as pd


result = {}


# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("sqlite:///Casino.db", {})
df = pandas.read_sql_query(sql=db.select(
                                [Roulette.try_number,
                                 Roulette.black_counter,
                                 Roulette.green_counter,
                                 Roulette.red_counter,
                                 Roulette.lowest_player_wallet,
                                 Roulette.total_spent,
                                 Roulette.final_bet_money,
                                 Roulette.final_bet_turn,
                                 Roulette.won_amount]),
    con=engine
)

list_of_arguments = ["try_number", "black_counter", "green_counter", "red_counter", "lowest_player_wallet",
                     "total_spent", "final_bet_money", "won_amount"]

for argument in list_of_arguments:
    result[argument] = {"min": round(float(df[argument].min()), 2),
                        "max": round(float(df[argument].max()), 2),
                        "std": round(float(df[argument].std()), 2),
                        "mean": round(float(df[argument].mean()), 2)}


def write_result_to_file(dictionary):
    with open("average_results.json", "w") as f:
        json.dump(dictionary, f, indent=2, sort_keys=True)


print(type(result))

write_result_to_file(dictionary=result)



