"""Rolling statistics."""

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


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    return ax


def test_run():
    # Read Data
    dates = pd.date_range('2019-05-23', '2020-05-22')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    ax = plot_data(df, title="Rolling Statistics")

    # Compute rolling mean using a 20-day window
    rm_SPY = df['SPY'].rolling(window=20).mean()

    # Add rolling mean to same plot
    rm_SPY.plot(label="Rolling mean", ax=ax)
    plt.show()


if __name__ == "__main__":
    test_run()
