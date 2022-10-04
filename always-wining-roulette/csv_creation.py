import json
import csv_creation as pd


def main():
    result = read_result()
    df = pd.DataFrame(result)
    df.to_csv("average_result.csv")


def read_result():
    with open("average_result.json", "r") as f:
        result = json.load(f)
        return result


if __name__ == '__main__':
    main()