# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

# List to store portfolio details
portfolio = []

# Display available stocks
print("=" * 50)
print("          STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter 'done' when you have finished adding stocks.\n")

# Take stock details from user
while True:

    stock_name = input("Enter stock name: ").upper().strip()

    # Stop taking input
    if stock_name == "DONE":
        break

    # Check whether stock exists
    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the available stocks.\n")
        continue

    # Take quantity
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

    except ValueError:
        print("Please enter a valid quantity.\n")
        continue

    # Calculate investment for this stock
    price = stock_prices[stock_name]
    investment = price * quantity

    # Store portfolio details
    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print(f"{stock_name} added successfully! ✅")
    print(f"Investment in {stock_name}: ${investment}\n")


# Check whether portfolio is empty
if len(portfolio) == 0:

    print("\nNo stocks were added to the portfolio.")

else:

    # Calculate total investment
    total_investment = 0

    print("\n" + "=" * 60)
    print("                 YOUR PORTFOLIO")
    print("=" * 60)

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment':<15}")
    print("-" * 60)

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<12}"
            f"${item['price']:<11}"
            f"${item['investment']:<15}"
        )

        total_investment += item["investment"]

    print("-" * 60)
    print(f"Total Investment: ${total_investment}")
    print("=" * 60)

    # Save portfolio to a text file
    save_file = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()

    if save_file == "yes":

        with open("stock_portfolio.txt", "w") as file:

            file.write("STOCK PORTFOLIO TRACKER\n")
            file.write("=" * 40 + "\n\n")

            for item in portfolio:
                file.write(
                    f"Stock: {item['stock']}\n"
                    f"Quantity: {item['quantity']}\n"
                    f"Price: ${item['price']}\n"
                    f"Investment: ${item['investment']}\n"
                    + "-" * 30 + "\n"
                )

            file.write(f"\nTotal Investment: ${total_investment}\n")

        print("\nPortfolio saved successfully! ✅")
        print("File name: stock_portfolio.txt")

    else:
        print("\nPortfolio was not saved.")