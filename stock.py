# TASK 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = []

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found. Try again.\n")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append((stock_name, quantity, investment))
    total_investment += investment

    print(f"✅ Added {stock_name} | Investment: ${investment}\n")

print("\n📊 Portfolio Summary")
for stock in portfolio:
    print(f"Stock: {stock[0]}, Quantity: {stock[1]}, Investment: ${stock[2]}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock in portfolio:
            file.write(f"{stock[0]}, {stock[1]}, ${stock[2]}\n")
        file.write(f"\nTotal Investment: ${total_investment}")

    print("📁 Data saved to portfolio.txt")