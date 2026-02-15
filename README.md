# Activity 5.2 - Compute Sales

## Description
This project consists of a Python script that calculates total sales from a JSON record file using a price catalogue provided in another JSON file.

## Requirements
- Python 3.x
- Pylint
- Flake8

## Files
- `computeSales.py`: Main script for calculation.
- `priceCatalogue.json`: Original catalogue containing product prices.
- `salesRecord.json`: Original record of sales transactions.
- `SalesResults.txt`: Output file with the latest results.
- `TC1.ProductList.json`: Test Case 1 Product Catalogue.
- `TC1.Sales.json`: Test Case 1 Sales Record.
- `TC2.Sales.json`: Test Case 2 Sales Record.
- `TC3.Sales.json`: Test Case 3 Sales Record.

## Execution
To run the script, use the following command structure:
```bash
python computeSales.py priceCatalogue.json salesRecord.json
```

## Quality Assurance
The code adheres to PEP-8 standards and has been verified with `flake8` and `pylint`.

### Flake8
No errors were found.
```
$ flake8 computeSales.py
(No output)
```

### Pylint
The code achieves a perfect score of 10/10.
```
$ pylint computeSales.py
Your code has been rated at 10.00/10
```

## Test Cases and Results
The system has been tested with 3 distinct test cases to ensure accuracy and error handling.

| Test Case | Product File | Sales File | Expected Behavior | Total Cost |
| :--- | :--- | :--- | :--- | :--- |
| **TC1** | `TC1.ProductList.json` | `TC1.Sales.json` | Standard execution. | **$2,481.86** |
| **TC2** | `TC1.ProductList.json` | `TC2.Sales.json` | Large quantities. | **$166,568.23** |
| **TC3** | `TC1.ProductList.json` | `TC3.Sales.json` | Invalid items (Elotes, Frijoles) handled gracefully. | **$165,235.37** |

### Execution Evidence
#### TC1 Execution
```bash
python computeSales.py TC1.ProductList.json TC1.Sales.json
TOTAL SALES RESULT
Total Cost: $2,481.86
Execution Time: 0.002 seconds
```

#### TC2 Execution
```bash
python computeSales.py TC1.ProductList.json TC2.Sales.json
TOTAL SALES RESULT
Total Cost: $166,568.23
Execution Time: 0.001 seconds
```

#### TC3 Execution
```bash
python computeSales.py TC1.ProductList.json TC3.Sales.json
Error: Product 'Elotes' not found in catalogue.
Error: Product 'Frijoles' not found in catalogue.
TOTAL SALES RESULT
Total Cost: $165,235.37
Execution Time: 0.003 seconds
```
