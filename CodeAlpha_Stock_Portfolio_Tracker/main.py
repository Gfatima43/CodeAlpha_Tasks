"""A simple CLI project that calculates investments from predefined stock prices
and exports the final results to a CSV file. The project uses the argparse library for command-line argument parsing and pandas for data manipulation and CSV export.
"""

from __future__ import annotations
from argparse import ArgumentParser
import csv
from pathlib import Path
from typing import Dict, List, TypedDict, Union

DEFAULT_STOCK_PRICES: Dict[str, float] = {
    "AAPL": 150.0,
    "GOOGL": 280.0,
    "AMZN": 340.0,
    "MSFT": 300.0,
    "TSLA": 700.0,
}

CSV_FILE = Path(__file__).resolve().parent / "investment_results.csv"

class InvestmentItem(TypedDict):
    stock: str
    quantity: int
    price_per_share: float
    total_investment: float
    
def normalize_symbol(symbol: str) -> str:
    """Return a clean uppercase stock symbol."""
    return symbol.strip().upper()

def calculate_investment(price_per_share: float, quantity: int) -> float:
    """Calculate the total investment for a given stock."""
    return price_per_share * quantity

def format_money(value: float) -> str:
    """"Format a number as US dollars. """
    return f"${value:,.2f}" 
   
def read_stock_symbol(stocks: Dict[str, float]) -> str:
    """Prompt until the user enters a valid stock symbol."""
    while True:
        symbol = normalize_symbol(input("Enter the stock symbol: "))
        if symbol in stocks:
            return symbol
        print(f"❌ Stock not available. Please choose from the available stocks: {', '.join(stocks.keys())}")

def read_quantity() -> int:
    """Prompt until the user enters a valid quantity."""
    while True:
        raw_quantity = input("Enter quantity: ").strip()
        try:
            quantity = int(raw_quantity)
        except ValueError:
            print("❌ Invalid input. Please enter a positive whole number.")
            continue
        if quantity > 0:
            return quantity
        print("❌ Quantity must be greater than zero.")
        
def should_continue() -> bool:
    """Ask whether another stock should be added."""
    while True:
        answer = input("Do you want to add another stock? (yes/no): ").strip().lower()
        if answer in ('yes', 'y'):
            return True
        if answer in ('no', 'n'):
            return False
        print("❌ Invalid input. Please enter 'y' for yes or 'n' for no.")
        
def add_investment_item(investments: List[InvestmentItem], stocks: Dict[str, float], symbol: str, quantity: int) -> None:
    """Add one calculated investment item to the list."""
    price_per_share = stocks[symbol]
    total_investment = calculate_investment(price_per_share, quantity)
    investments.append(
        {
            "stock": symbol,
            "quantity": quantity,
            "price_per_share": price_per_share,
            "total_investment": total_investment,
        }
    )
    print(f"✅ Added {quantity} shares of {symbol} at {format_money(price_per_share)} each. \nTotal investment: {format_money(total_investment)}.")
    
def display_summary(investments: List[InvestmentItem]) -> None:
    """Display the final list of investments in a formatted table and grand total."""
    if not investments:
        print("No investments to display.")
        return
    print("\nInvestment Summary:")
    print("=" * 58)
    print(f"{'Stock':<10} {'Quantity':>10} {'Price / Share':>15} {'Total Investment':>20}")
    print("-" * 58)
    
    grand_total = 0.0
    for item in investments:
        grand_total += item["total_investment"]
        print(
            f"{item['stock']:<10}"
            f" {item['quantity']:>10}"
            f" {format_money(item['price_per_share']):>15}"
            f" {format_money(item['total_investment']):>20}"
        )
    print("-" * 58)
    print(f"{'Grand Total':<37} {format_money(grand_total):>20}")

def display_welcome(stocks: Dict[str, float]) -> None:
    """Display a welcome message and the available stock symbols."""
    print("=" * 50)
    print("Welcome to the Investment Calculator!")
    print("=" * 50)
    print("Available stocks:")
    for symbol, price in stocks.items():
        print(f"  {symbol:<10} {format_money(price)}")

def export_to_csv(investments: List[InvestmentItem], filename: Union[str, Path] = CSV_FILE) -> bool:
    """Export the list of investments to a CSV file."""
    output_path = Path(filename).expanduser()
    if not output_path.is_absolute():
        output_path = Path(__file__).resolve().parent / output_path
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open(mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["Stock", "Quantity", "Price Per Share", "Total Investment"]
            writer = csv.DictWriter(
                file, fieldnames=fieldnames
            )
            writer.writeheader()
            for item in investments:
                writer.writerow(
                    {
                        "Stock": item["stock"],
                        "Quantity": item["quantity"],
                        "Price Per Share": f"{item['price_per_share']:.2f}",
                        "Total Investment": f"{item['total_investment']:.2f}",
                    }
                )
            grand_total = sum(item["total_investment"] for item in investments)
            writer.writerow(
                {
                    "Stock": "Grand Total",
                    "Total Investment": f"{grand_total:.2f}",
                }
            )
        print(f"✅ Investments exported to {output_path.name}")
        return True
    except PermissionError:
        print(f"❌ Could not write to {output_path}. Please check the file permissions and try again.")
    except OSError as e:
        print(f"❌ Could not write to {output_path}: {e}")
    except Exception as e:
        print(f"❌ Error exporting investments to CSV: {e}")
    return False
    
def main() -> None:
    """Run the stock investment calculator CLI."""
    parser = ArgumentParser(description="Stock Investment Calculator")
    parser.add_argument(
        "--stocks",
        type=str,
        help="Path to a CSV file containing stock symbols and prices. If not provided, default prices will be used.",
    )
    args = parser.parse_args()

    stocks = DEFAULT_STOCK_PRICES.copy()
    
    if args.stocks:
        try:
            with open(args.stocks, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                stocks = {row['Symbol'].strip().upper(): float(row['Price']) for row in reader}
            print(f"✅ Loaded stock prices from {args.stocks}")
        except Exception as e:
            print(f"❌ Error loading stock prices from {args.stocks}: {e}")
            print("Using default stock prices instead.")

    display_welcome(stocks)

    investments: List[InvestmentItem] = []
    
    while True:
        symbol = read_stock_symbol(stocks)
        quantity = read_quantity()
        add_investment_item(investments, stocks, symbol, quantity)
        
        if not should_continue():
            break
        
    if not investments:
        print("❌ No investments added. Exiting.")
        return

    display_summary(investments)
    export_to_csv(investments)
    
if __name__ == "__main__":
    main()