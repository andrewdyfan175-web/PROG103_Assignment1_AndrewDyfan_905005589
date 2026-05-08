# ============================================================
# Small Business Sales Calculator
# This system supports small businesses in Sierra Leone
# by helping them track sales, calculate profits, and
# manage their financial records efficiently.
# ============================================================

# CONSTANTS
TAX_RATE = 0.15          # 15% tax rate (NRA Sierra Leone standard)
DISCOUNT_THRESHOLD = 5000  # SLL 5,000 qualifies for discount
DISCOUNT_RATE = 0.05     # 5% discount for bulk purchases
APP_NAME = "Small Business Sales Calculator (SBSC)"
VERSION = "1.0"


# --------------------
# FUNCTION DEFINITIONS
# --------------------

def display_header():
    """Displays the application header/banner."""
    print("=" * 60)
    print(f"   {APP_NAME}")
    print(f"   Version {VERSION}")
    print("   Empowering Small Businesses in Sierra Leone")
    print("   SDG 8: Decent Work and Economic Growth")
    print("=" * 60)
    print()


def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- MAIN MENU ---")
    print("1. Add a Sale Record")
    print("2. View All Sales Records")
    print("3. View Sales Summary / Report")
    print("4. Search Sale by Product Name")
    print("5. Exit")
    print("-" * 20)


def get_float_input(prompt):
    """
    Safely gets a positive float input from the user.
    Uses a loop to keep asking until valid input is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  [!] Value cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("  [!] Invalid input. Please enter a numeric value.")


def get_int_input(prompt):
    """
    Safely gets a positive integer input from the user.
    Uses a loop to keep asking until valid input is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  [!] Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


def calculate_discount(subtotal):
    """
    Calculates discount based on subtotal amount.
    Returns discount amount (float).
    Decision structure: if/else
    """
    if subtotal >= DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
        print(f"  [*] Bulk purchase discount applied: {DISCOUNT_RATE * 100:.0f}%")
    else:
        discount = 0.0
    return discount


def calculate_tax(amount):
    """
    Calculates tax on a given amount.
    Returns tax amount (float).
    """
    return amount * TAX_RATE


def calculate_total(unit_price, quantity):
    """
    Calculates subtotal, discount, tax, and final total for a sale.
    Returns a dictionary with all computed values.
    """
    subtotal = unit_price * quantity
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount)
    total = discounted_amount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "discounted_amount": discounted_amount,
        "tax": tax,
        "total": total
    }


def add_sale(sales_list):
    """
    Prompts user to enter a sale record and appends it to the sales list.
    Demonstrates: input, data types, functions, decision structures.
    """
    print("\n--- ADD NEW SALE RECORD ---")

    product_name = input("  Enter Product Name       : ").strip()
    if product_name == "":
        print("  [!] Product name cannot be empty.")
        return

    category = input("  Enter Product Category   : ").strip()
    unit_price = get_float_input("  Enter Unit Price (SLL)   : ")
    quantity = get_int_input("  Enter Quantity Sold      : ")

    # Calculate all values
    result = calculate_total(unit_price, quantity)

    # Build sale record as a dictionary
    sale_record = {
        "id": len(sales_list) + 1,
        "product": product_name,
        "category": category,
        "unit_price": unit_price,
        "quantity": quantity,
        "subtotal": result["subtotal"],
        "discount": result["discount"],
        "tax": result["tax"],
        "total": result["total"]
    }

    sales_list.append(sale_record)

    # Display receipt for this sale
    print("\n  --- SALE RECEIPT ---")
    print(f"  Sale ID        : #{sale_record['id']}")
    print(f"  Product        : {product_name}")
    print(f"  Category       : {category}")
    print(f"  Unit Price     : SLL {unit_price:,.2f}")
    print(f"  Quantity       : {quantity}")
    print(f"  Subtotal       : SLL {result['subtotal']:,.2f}")
    print(f"  Discount(5%)       : SLL {result['discount']:,.2f}")
    print(f"  Tax (15%)      : SLL {result['tax']:,.2f}")
    print(f"  TOTAL PAYABLE  : SLL {result['total']:,.2f}")
    print("  " + "-" * 30)
    print("  [✔] Sale record saved successfully!")


def view_all_sales(sales_list):
    """
    Displays all recorded sales in a formatted table.
    Uses a loop to iterate through the sales list.
    """
    print("\n--- ALL SALES RECORDS ---")

    if len(sales_list) == 0:
        print("  [!] No sales records found. Please add a sale first.")
        return

    # Table header
    print(f"\n  {'ID':<5} {'Product':<20} {'Category':<15} {'Qty':<6} {'Unit Price':>14} {'Total':>16}")
    print("  " + "-" * 78)

    # Loop through all records
    for sale in sales_list:
        print(f"  {sale['id']:<5} {sale['product']:<20} {sale['category']:<15} "
              f"{sale['quantity']:<6} SLL {sale['unit_price']:>10,.2f} SLL {sale['total']:>12,.2f}")

    print("  " + "-" * 78)
    print(f"  Total Records: {len(sales_list)}")


def view_summary(sales_list):
    """
    Generates a full sales summary/report.
    Uses loops and decision structures to compute statistics.
    """
    print("\n--- SALES SUMMARY REPORT ---")

    if len(sales_list) == 0:
        print("  [!] No sales records available for summary.")
        return

    # Initialize accumulators
    total_revenue = 0.0
    total_discount = 0.0
    total_tax = 0.0
    total_quantity = 0
    highest_sale = sales_list[0]
    lowest_sale = sales_list[0]

    # Loop through all sales
    for sale in sales_list:
        total_revenue += sale["total"]
        total_discount += sale["discount"]
        total_tax += sale["tax"]
        total_quantity += sale["quantity"]

        # Find highest and lowest sale using decision structures
        if sale["total"] > highest_sale["total"]:
            highest_sale = sale
        if sale["total"] < lowest_sale["total"]:
            lowest_sale = sale

    average_sale = total_revenue / len(sales_list)

    print(f"\n  Number of Sales        : {len(sales_list)}")
    print(f"  Total Items Sold       : {total_quantity}")
    print(f"  Total Discounts Given  : SLL {total_discount:,.2f}")
    print(f"  Total Tax Collected    : SLL {total_tax:,.2f}")
    print(f"  Total Revenue          : SLL {total_revenue:,.2f}")
    print(f"  Average Sale Value     : SLL {average_sale:,.2f}")
    print(f"\n  Highest Sale           : {highest_sale['product']} — SLL {highest_sale['total']:,.2f}")
    print(f"  Lowest Sale            : {lowest_sale['product']} — SLL {lowest_sale['total']:,.2f}")

    # Performance indicator using decision structure
    print("\n  --- BUSINESS PERFORMANCE INDICATOR ---")
    if total_revenue >= 5000000:
        print("  [★★★] Excellent! Revenue exceeds SLL 5,000,000.")
    elif total_revenue >= 2000000:
        print("  [★★ ] Good performance. Keep it up!")
    elif total_revenue >= 500000:
        print("  [★  ] Fair. Try to increase sales volume.")
    else:
        print("  [   ] Low revenue. Consider promotions or discounts.")


def search_sale(sales_list):
    """
    Searches for a sale record by product name (case-insensitive).
    Uses a loop and decision structure.
    """
    print("\n--- SEARCH SALE BY PRODUCT NAME ---")

    if len(sales_list) == 0:
        print("  [!] No records to search.")
        return

    keyword = input("  Enter product name to search: ").strip().lower()
    found = False

    # Loop through records to find matches
    for sale in sales_list:
        if keyword in sale["product"].lower():
            print(f"\n  --- Match Found ---")
            print(f"  Sale ID      : #{sale['id']}")
            print(f"  Product      : {sale['product']}")
            print(f"  Category     : {sale['category']}")
            print(f"  Unit Price   : SLL {sale['unit_price']:,.2f}")
            print(f"  Quantity     : {sale['quantity']}")
            print(f"  Subtotal     : SLL {sale['subtotal']:,.2f}")
            print(f"  Discount     : SLL {sale['discount']:,.2f}")
            print(f"  Tax          : SLL {sale['tax']:,.2f}")
            print(f"  Total        : SLL {sale['total']:,.2f}")
            found = True

    if not found:
        print(f"  [!] No sale found matching '{keyword}'.")


# MAIN PROGRAM

def main():
    """
    Main function — entry point of the program.
    Controls the main loop and menu navigation.
    """
    sales_list = []   # List to store all sale records (data structure)

    display_header()
    print("  Welcome! This system helps small businesses in Sierra Leone")
    print("  track their daily sales, calculate taxes, and view reports.")

    # Main program loop
    running = True
    while running:
        display_menu()
        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            add_sale(sales_list)
        elif choice == "2":
            view_all_sales(sales_list)
        elif choice == "3":
            view_summary(sales_list)
        elif choice == "4":
            search_sale(sales_list)
        elif choice == "5":
            print("\n  Thank you for using SBSC. Goodbye!")
            print("  Supporting SDG 8 — Economic Growth in Sierra Leone 🇸🇱")
            print("=" * 60)
            running = False
        else:
            print("  [!] Invalid choice. Please enter a number between 1 and 5.")


# Entry point
if __name__ == "__main__":
    main()