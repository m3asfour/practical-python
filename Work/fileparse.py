# fileparse.py
#
# Exercise 3.5

import csv

def parse_csv(filename, select=None, types=None):
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

        # default the types to str if not passeed
        if not types:
            types = [str for h in headers]

        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # cast the selected column data into the corresponding type
            record = dict(zip(headers, [val_type(row[col_idx]) for val_type, col_idx in zip(types, indices)]))
            records.append(record)

    return records