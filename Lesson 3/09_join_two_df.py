"""Build a dataframe in pandas."""
import pandas as pd


def test_run():
    start_date = "2020-03-13"
    end_date = "2020-03-17"
    dates = pd.date_range(start_date, end_date)  # list of DatetimeIndex object

    df1 = pd.DataFrame(index=dates)  # create an empty dataframe

    # read SPY data into temporary dataframe
    # index_col: corrected for the index col to be "Date" instead of integers (refer to CSV file)
    # parse_dates: convert dates into DateTime index objects
    # usecols: use only two columns we are interested in
    # na_values: NaN is string -> need to tell read_csv should be indicated as "Not a Number"
    dfSPY = pd.read_csv("../data/SPY.csv", index_col="Date", parse_dates=True,
                        usecols=["Date", "Adj Close"], na_values=["nan"])

    # inner join: form intersection based on df1 index with dfSPY index, while preserving order of df1 index
    # alternatively:
    # df1 = df1.join(dfSPY) does a left join by default
    # ie a.join(b) = all rules of a + rules of b whose index values are in a (rest are NaNs), then use
    # df1 = df1.dropna() to drop rows with NaN values
    df1 = df1.join(dfSPY, how="inner")

    print(df1)


if __name__ == "__main__":
    test_run()
