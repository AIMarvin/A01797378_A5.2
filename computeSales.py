# pylint: disable=invalid-name
"""
This module calculates total sales from a JSON file using a price catalogue.
It reads two JSON files (catalogue and sales record), computes the total cost,
and writes the result to a file and console, including execution time.
"""

import sys
import json
import time


def load_json_file(filename):
    """Parses a JSON file and returns its content."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error loading {filename}: {error}")
        return None


def create_price_catalogue(catalogue_data):
    """Converts price catalogue list to a dictionary for faster lookup."""
    price_dict = {}
    for item in catalogue_data:
        title = item.get("title")
        price = item.get("price")
        if title and isinstance(price, (int, float)):
            price_dict[title] = price
    return price_dict


def compute_total_sales(price_catalogue, sales_record):
    """Calculates total sales cost based on the sales record."""
    total_cost = 0.0
    for sale in sales_record:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product not in price_catalogue:
            print(f"Error: Product '{product}' not found in catalogue.")
            continue

        try:
            quantity = float(quantity)
            total_cost += price_catalogue[product] * quantity
        except (ValueError, TypeError):
            print(f"Error: Invalid quantity '{quantity}' "
                  f"for product '{product}'.")
            continue

    return total_cost


def main():
    """Main function to execute the sales calculation."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json "
              "salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    catalogue_data = load_json_file(catalogue_file)
    sales_data = load_json_file(sales_file)

    if catalogue_data is None or sales_data is None:
        sys.exit(1)

    price_dict = create_price_catalogue(catalogue_data)
    total_sales = compute_total_sales(price_dict, sales_data)

    elapsed_time = time.time() - start_time
    output_lines = [
        "TOTAL SALES RESULT",
        f"Total Cost: ${total_sales:,.2f}",
        f"Execution Time: {elapsed_time:.6f} seconds"
    ]

    # Print to console
    for line in output_lines:
        print(line)

    # Write to file
    with open("SalesResults.txt", "w", encoding='utf-8') as result_file:
        result_file.write("\n".join(output_lines))


if __name__ == "__main__":
    main()
