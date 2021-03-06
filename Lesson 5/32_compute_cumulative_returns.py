"""Compute cumulative returns."""

import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="../data/"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def compute_cumulative_returns(df):
    """Compute and return the cumulative return values."""
    cumulative_returns = df.copy()  # copy given dataframe to match size and column names
    cumulative_returns = (df/df.iloc[0, :].values) - 1
    return cumulative_returns


def test_run():
    # Read data
    dates = pd.date_range('2019-07-01', '2019-07-31')  # one month only
    symbols = ['SPY', 'GOOG']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute cumulative returns
    cumulative_returns = compute_cumulative_returns(df)
    plot_data(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")


if __name__ == "__main__":
    test_run()
