# Stock-Portfolio-Tracker
 Stock Portfolio Tracker

Goal:

The objective of this console application is to build a simple stock tracker that calculates the total current investment value based on manual user inputs and hardcoded price data.

Key Features:

Hardcoded Prices: Stock prices are defined in an internal Python dictionary (PRICE_DATA), simulating a static price feed for: AAPL, TSLA, MSFT, GOOG, AMZN, V, and NVDA.

User Input: The program collects stock tickers and the quantity of shares from the user.

Value Calculation: Calculates the total value of the portfolio based on the quantity multiplied by the predefined price for each stock.

Report Generation: Prints a detailed, itemized summary of the portfolio and the total value to the console.

File Handling: Automatically saves the complete valuation report to a text file named portfolio_summary.txt upon completion.

How to Run:

Ensure you have Python 3 installed.

Save the code as stock_tracker.py.

Open your terminal or command prompt.

Run the script using the following command:

python stock_tracker.py


Usage:

The program will prompt you to enter a stock ticker (e.g., AAPL) and the quantity (e.g., 10). Enter 'done' when you have finished adding all your holdings.

Concepts Demonstrated

Dictionaries (for storing price data)

Input/Output (for collecting user data and displaying results)

Basic Arithmetic (for calculating total value)

File Handling (for generating and saving the final .txt report)
