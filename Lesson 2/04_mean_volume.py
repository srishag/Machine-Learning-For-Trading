import pandas as pd


def get_mean_volume(symbol):
    """Return the mean volume value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("../data/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()  # compute and return mean


def test_run():
    """Function called by Test Run."""
    print("Mean Volume")
    for symbol in ['AAPL', 'IBM']:
        print(symbol, get_mean_volume(symbol))


if __name__ == "__main__":
    test_run()
