# Stock Portfolio Tracker

A command-line Python program that calculates a stock portfolio using predefined
stock prices and exports the final result to `investment_results.csv`.

## Available Stocks

| Stock | Price |
| --- | ---: |
| AAPL | $150.00 |
| GOOGL | $280.00 |
| AMZN | $340.00 |
| MSFT | $300.00 |
| TSLA | $700.00 |

## Run

```bash
python main.py
```

Enter a stock symbol, quantity, and whether you want to add another stock. When
you finish, the app prints a portfolio summary and writes `investment_results.csv`.
The CSV is saved beside `main.py`, even when you launch the program from another
working directory.
