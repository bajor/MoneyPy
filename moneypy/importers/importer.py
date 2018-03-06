import pandas as pd
import regex as re

def find_fields(*args, **kwargs):
    file = pd.read_csv(*args)
    fields = []

    if not kwargs: kwargs = dict(date = 'date', amount = 'amount', desc = 'description')

    for v in kwargs.items():
        f = file[[col for col in file.columns.values if re.search(v[1], col, re.IGNORECASE)]]
        if len(f) >= 0: fields.append(f.columns[0])

    return file.filter(items=fields)