import os
from typing import Dict, List, Tuple

# --- Configuration: Hardcoded Stock Prices ---
# This dictionary simulates a real-time price feed for simplicity.
PRICE_DATA: Dict[str, float] = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "MSFT": 420.00,
    "GOOG": 155.20,
    "AMZN": 185.90,
    "V": 270.30,
    "NVDA": 920.00,
}

def get_portfolio_input(prices: Dict[str, float]) -> Dict[str, int]:
    """
    Collects stock ticker and quantity input from the user.

    Args:
        prices: The dictionary of available stock prices.

    Returns:
        A dictionary mapping stock tickers to quantities (e.g., {"AAPL": 10}).
    """
    portfolio: Dict[str, int] = {}
    print("\n--- Portfolio Input ---")
    print(f"Available stocks: {', '.join(prices.keys())}")
    print("Enter 'done' when finished.")

    while True:
        try:
            # 1. Get stock ticker
            ticker = input("Enter stock ticker (or 'done'): ").strip().upper()
            if ticker == 'DONE':
                break

            if ticker not in prices:
                print(f"Error: Ticker '{ticker}' not found in price list. Please try again.")
                continue

            # 2. Get quantity
            quantity_input = input(f"Enter quantity for {ticker}: ").strip()
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Error: Quantity must be a positive whole number.")
                continue

            # 3. Add to portfolio
            portfolio[ticker] = portfolio.get(ticker, 0) + quantity
            print(f"Added {quantity} shares of {ticker}.")

        except ValueError:
            print("Error: Invalid quantity entered. Please enter a whole number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return portfolio

def calculate_portfolio_value(portfolio: Dict[str, int], prices: Dict[str, float]) -> Tuple[float, List[str]]:
    """
    Calculates the total value of the portfolio and generates a detailed summary.

    Args:
        portfolio: User's stock holdings (ticker: quantity).
        prices: Hardcoded price data (ticker: price).

    Returns:
        A tuple containing:
        - The total calculated investment value (float).
        - A list of formatted strings for the detailed summary.
    """
    total_value: float = 0.0
    summary_lines: List[str] = ["\n--- Investment Summary ---"]

    if not portfolio:
        return 0.0, summary_lines

    # Sort stocks alphabetically for a clean report
    sorted_tickers = sorted(portfolio.keys())

    for ticker in sorted_tickers:
        quantity = portfolio[ticker]
        price = prices.get(ticker, 0.0)  # Use 0.0 if somehow price is missing
        stock_value = quantity * price
        total_value += stock_value

        summary_line = (
            f"Stock: {ticker:<5} | Quantity: {quantity:<4} | Price: ${price:10,.2f} | "
            f"Value: ${stock_value:12,.2f}"
        )
        summary_lines.append(summary_line)

    return total_value, summary_lines

def save_portfolio(total_value: float, summary_lines: List[str], filename: str = "portfolio_summary.txt"):
    """
    Writes the portfolio summary and total value to a specified text file.
    """
    try:
        with open(filename, 'w') as f:
            f.write("Stock Portfolio Valuation Report\n")
            f.write("Generated using hardcoded price data.\n")
            f.write("----------------------------------------\n")

            # Write individual stock lines
            for line in summary_lines:
                f.write(line + "\n")

            # Write total value
            total_line = f"\nTOTAL INVESTMENT VALUE: ${total_value:,.2f}"
            f.write(total_line + "\n")

        print(f"\nSuccess! Portfolio summary saved to '{filename}' in the current directory.")
        print(total_line)

    except Exception as e:
        print(f"\nError writing file: {e}")

# --- Main Execution Block ---
if __name__ == "__main__":
    # 1. Get user input
    user_portfolio = get_portfolio_input(PRICE_DATA)

    # 2. Calculate and generate summary
    if user_portfolio:
        final_value, detail_lines = calculate_portfolio_value(user_portfolio, PRICE_DATA)

        # Print detailed breakdown
        for line in detail_lines:
            print(line)

        # 3. Save to file
        save_portfolio(final_value, detail_lines)
    else:
        print("\nNo stocks were entered. Portfolio value is $0.00.")
