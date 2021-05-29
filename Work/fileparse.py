# fileparse.py
#
# Exercise 3.4

import csv

def parse_csv(filename, select=None):
    """Parse a CSV file into a list of records with safe selection of columns

    Args:
        filename (str): filepath of the csv file

    Returns:
        [list]: list of dictionaries containing csv parsed data
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []

        # select the specified headers only and the indices of the corresponding value
        if select:
            # select columns that exist in headers (any colname could be passed)
            exist_select = [colname for colname in select if colname in headers]
            indices = [headers.index(col) for col in exist_select]
            headers = exist_select

            # print a message if some columns not found in headers
            if len(exist_select) != len(select):
                print(f'Columns not found: {[colname for colname in select if colname not in exist_select]}')

        else:
            indices = range(len(headers))   # all values in the row if no headers were selected

        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, [row[col_idx] for col_idx in indices]))
            records.append(record)

    return records