"""Plot two histograms."""

import os
import pandas as pd
import matplotlib.pyplot as plt


# function to get path of the symbol
def symbol_to_path(symbol, base_dir="../data/"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


# reads csv
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


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()  # copy given dataframe to match size and column names
    # compute daily returns starting from row 1 as no data present for day before day 0
    # another way to do this is: (df[1:]/df[:-1].values) - 1
    daily_returns[1:] = (df/df.shift(1)) - 1
    daily_returns.iloc[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2019-05-23', '2020-05-22')
    symbols = ['SPY', 'GOOG']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Compute and plot both histograms on the same chart
    daily_returns['SPY'].hist(bins=20, label="SPY")  # default number of bins is 10
    daily_returns['GOOG'].hist(bins=20, label="GOOG")
    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":
    test_run()
