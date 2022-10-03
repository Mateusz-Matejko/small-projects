from app import db, Roulette
import pandas as pd

result = {}

list_of_arguments = [try_number, black_counter, red_counter, green_counter,
                     final_bet_money, lowest_player_wallet, total_spent, won_amount]

for list_of_arguments in :
    argument = argument
    slq_query = db.session.query(Roulette(**result)).all()
    df = pd.DataFrame(slq_query)
    res = df.describe()
    result[argument] = {"min": res.describe().min(),
                        "max": res.describe().max(),
                        "std": res.describe().std()}

print(result)





