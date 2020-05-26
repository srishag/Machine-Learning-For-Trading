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

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def test_run():
    # Read data
    dates = pd.date_range('2020-02-01', '2020-05-31')
    symbols = ['SPY', 'GOOG']
    df = get_data(symbols, dates)
    df.fillna(method="ffill", inplace=True)  # fill forward
    df.fillna(method="bfill", inplace=True)  # fill backward
    plot_data(df)


if __name__ == "__main__":
    test_run()
