import pandas as pd


def get_max_close(symbol):
    """Return the maximum closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("../data/{}.csv".format(symbol))  # read in data
    return df['Close'].max()  # compute and return max


def test_run():
    """Function called by Test Run."""
    print("Max Close")
    for symbol in ['AAPL', 'IBM']:
        print(symbol, get_max_close(symbol))


if __name__ == "__main__":
    test_run()
