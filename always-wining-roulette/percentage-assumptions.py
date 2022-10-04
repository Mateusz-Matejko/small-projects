template = {
    "black_counter": 8,
    "final_bet_money": 2048,
    "final_bet_turn": 12,
    "green_counter": 0,
    "lowest_player_wallet": -1719,
    "red_counter": 4,
    "total_spent": 4095,
    "try_number": 402319,
    "won_amount": 329
  }

# this is minimal amount of moves will guarantee the minimal expected win (100)


def chance_for_7_wins_in_a_row():
    return 0.4864864864864865 ** 7
print(f"{chance_for_7_wins_in_a_row():.2%}")



