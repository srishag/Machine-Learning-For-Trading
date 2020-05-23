"""Build a dataframe in pandas."""
import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="../data/"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if "SPY" not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, "SPY")

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
                              usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})  # rename column to ensure unique column names
        df = df.join(df_temp)
        if symbol == "SPY":  # use SPY as a reference: drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe."""
    return df / df.iloc[0, :]  # divide by the first row


def plot_data(df, title="Normalized Stock Prices"):
    """Plot stock prices."""
    # df.plot()

    # make up for missing title of graph, missing x and y axis labels
    ax = df.plot(title=title, fontsize=12)  # font size used to make the graph more detailed
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()  # must be called to show plots in some environments


def test_run():
    # Define a date range
    dates = pd.date_range('2019-05-23', '2020-05-22')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'AAPL']

    # Get stock data
    df = get_data(symbols, dates)
    df = normalize_data(df)
    print(df)

    plot_data(df)


if __name__ == "__main__":
    test_run()
