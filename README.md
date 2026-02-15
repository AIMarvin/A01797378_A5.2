# Activity 5.2 - Compute Sales

## Description
This project consists of a Python script that calculates total sales from a JSON record file using a price catalogue provided in another JSON file.

## Requirements
- Python 3.x
- Pylint
- Flake8

## Files
- `computeSales.py`: Main script for calculation.
- `priceCatalogue.json`: Catalogue containing product prices.
- `salesRecord.json`: Record of sales transactions.
- `SalesResults.txt`: Output file with the latest results.

## Execution
To run the script, use the following command:
```bash
python computeSales.py priceCatalogue.json salesRecord.json
```

## Results
The program outputs the total cost and the execution time to both the console and a file named `SalesResults.txt`.

Example output:
```text
TOTAL SALES RESULT
Total Cost: $130.00
Execution Time: 0.001539 seconds
```

## Quality
- **Pylint Score**: 10.00/10
- **Flake8**: 0 errors
- **PEP-8 Compliant**
