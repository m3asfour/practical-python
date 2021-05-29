# fileparse.py
#
# Exercise 3.17

import gzip

def parse_csv(file, select=None, types=None, has_headers=True, 
                delimiter=',', silence_errors=False):
    """Parse a CSV file into a list of records with safe selection of columns

    Args:
        file (file-like/iterable): an iterable or a stream
        select (list): list of column names to include
        types (list): list of types to cast the row values into
        has_headers (bool): a flag to indicate if the csv file has a header
        delimiter (str): the delimiter to parse each line by
        silence_errors (bool): a flag to supress error message in the terminal

    Returns:
        [list]: list of dictionaries containing csv parsed data
    """

    # raise an exception if columns are selected without headers in the csv file
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    #####################################
    # By the end of this block we guarentee that regardless of the passed file type
    # it will be iterable and have a __next__ method
    if isinstance(file, str):           # if str, it's a filepath -> load it
        if file[-3:] == '.gz':          # if zipped file, load it using gzip
            with gzip.open(file, 'rt') as f:
                file = f.readlines()    # each line is read as a str (not parsed)
        else:
            with open(file, 'rt') as f: # if not zipped, load using open() 
                file = f.readlines()    # each line is read as a str (not parsed)
    ## by now we guarentee the file is iterable, but it doesn't have __next__ if it's a list

    if isinstance(file, list):          # if it's a list convert it to a generator
        file = (elem for elem in file)
    #####################################

    # Read the file headers if the csv file has a headers row
    if has_headers:
        headers = next(file)
        # if each line is read as a str: remove quotation marks, remove white space, split using the delimiter
        headers = headers.replace('"','').strip().split(delimiter) if isinstance(headers, str) else headers
    else:
        headers = None

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

    for row_idx, row in enumerate(file):
        if (not row) or ''.join(row).strip() == '':    # Skip rows with no data or the final line containing ' '
            continue

        # if each line is read as a str: remove quotation marks, remove white space, split using the delimiter
        if isinstance(row, str):
            row = row.replace('"','').strip().split(delimiter)  # split the values

        try:
            # cast the selected column data into the corresponding type
            row_indices = indices if indices else range(len(row))
            parsed_row = [val_type(row[col_idx]) for val_type, col_idx in zip(types, row_indices)]
            
            # store in a dictionary if headers exist, otherwise cast into a tuple
            if headers:
                record = dict(zip(headers, parsed_row))
            else:
                record = tuple(parsed_row)

            records.append(record)
        
        except ValueError as error:  # catch record creation value errors
            if not silence_errors:
                # print the reason of the error
                print(f'Row {row_idx+1}: Couldn\'t convert {row}')
                print(f'Row {row_idx+1}: Reason {error}')

    return records
