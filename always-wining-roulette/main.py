import json
from random import choice

# Starting variables that simulation was made for
start_money = 1  # the money player start with
expected_win = 100 # the money player is at least expecting to win

# the following program was written for color Red, but was also tested for color black.
chose_to_win = "red" # the color player will always be betting for


# defining casino game board
green = [0]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
whole_roulette = green + black + red


def main():
    list_of_results = roulette_simulation(amount_of_tries=1)
    write_results(results=list_of_results)


def roulette_simulation(amount_of_tries):
    # list that keeps all the result details for further analysis
    final_results = []
    for _ in range(amount_of_tries):
        current_bet = start_money
        total_spent = 0
        turn = 0
        red_counter = 0
        green_counter = 0
        black_counter = 0
        next_bet = 0
        player_wallet = 0
        while True:
            if next_bet != 0:
                current_bet = next_bet
            turn += 1
            total_spent += current_bet
            result = choice(whole_roulette)
            next_bet = current_bet * 2
            if result in red and current_bet + player_wallet > expected_win:
                player_wallet += current_bet
                red_counter += 1
                simulation_details = {}
                ...
                simulation_details["red_counter"] = red_counter
                simulation_details["black_counter"] = black_counter
                simulation_details["green_counter"] = green_counter
                simulation_details["final_bet_money"] = current_bet
                simulation_details["final_bet_turn"] = turn
                simulation_details["total_spent"] = total_spent
                simulation_details["won_amount"] = player_wallet
                final_results.append(simulation_details)
                break
            elif result in red:
                red_counter += 1
                player_wallet += current_bet
                continue
            elif result in black:
                black_counter += 1
                player_wallet -= current_bet
                continue
            elif result in green:
                green_counter += 1
                player_wallet -= current_bet
                continue
    return final_results


def write_results(results):
    with open("results-holder.json", "a") as f:
        json.dump(results, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()