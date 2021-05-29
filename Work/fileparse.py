# fileparse.py
#
# Exercise 3.8

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """Parse a CSV file into a list of records with safe selection of columns

    Args:
        filename (str): filepath of the csv file
        select (list): list of column names to include
        types (list): list of types to cast the row values into
        has_headers (bool): a flag to indicate if the csv file has a header
        delimiter (str): the delimiter to parse each line by

    Returns:
        [list]: list of dictionaries containing csv parsed data
    """

    # raise an exception if columns are selected without headers in the csv file
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers if the csv file has a headers row
        headers = next(rows) if has_headers else None
        indices = None   # indices of selected columns 
        records = []

        # select the specified headers only and the indices of the corresponding value
        if select and headers: # there must be headers to select from
            # select columns that exist in headers (any colname could be passed)
            exist_select = [colname for colname in select if colname in headers]
            indices = [headers.index(col) for col in exist_select]
            headers = exist_select

            # print a message if some columns not found in headers
            if len(exist_select) != len(select):
                print(f'Columns not found: {[colname for colname in select if colname not in exist_select]}')

        # default the types to str if not passeed
        if not types:
            types = [str for h in headers]

        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # cast the selected column data into the corresponding type
            row_indices = indices if indices else range(len(row))
            parsed_row = [val_type(row[col_idx]) for val_type, col_idx in zip(types, row_indices)]
            
            # store in a dictionary if headers exist, otherwise cast into a tuple
            if headers:
                record = dict(zip(headers, parsed_row))
            else:
                record = tuple(parsed_row)

            records.append(record)

    return records