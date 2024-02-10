import pandas as pd

import re


@pd.api.extensions.register_dataframe_accessor("select")
class SelectAccessor:
    def __init__(self, pandas_obj):
        # self._validate(pandas_obj)
        self._obj = pandas_obj

    def starts_with(self, s: str):
        return self._obj[[col for col in self._obj.columns if col.startswith(s)]]

    def ends_with(self, s: str):
        return self._obj[[col for col in self._obj.columns if col.endswith(s)]]

    def contains(self, s: str):
        return self._obj[[col for col in self._obj.columns if s in col]]

    def matches(self, pattern: str):
        return self._obj[[col for col in self._obj.columns if re.search(pattern, col)]]
