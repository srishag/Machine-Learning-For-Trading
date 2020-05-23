"""Build a dataframe in pandas."""
import pandas as pd


def test_run():
    start_date = "2020-03-13"
    end_date = "2020-03-17"
    dates = pd.date_range(start_date, end_date)  # list of DatetimeIndex object

    df1 = pd.DataFrame(index=dates)  # create an empty dataframe

    # Read in more stocks
    symbols = ["SPY", "GOOG", "IBM", "AAPL"]
    for symbol in symbols:
        df_temp = pd.read_csv("../data/{}.csv".format(symbol), index_col="Date", parse_dates=True,
                              usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})  # rename column to ensure unique column names
        df1 = df1.join(df_temp, how="inner")

    print(df1)


if __name__ == "__main__":
    test_run()
