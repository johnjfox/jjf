import pandas as pd
from pandas.testing import assert_frame_equal

from src import jjf


def make_test_df():
    return pd.DataFrame(
        {
            "foo_int1_end": [1, 2, 3],
            "int2_end": [100, 200, 300],
            "foo_float1": [4.0, 5.0, 6.0],
            "float2": [40.0, 50.0, 60.0],
            "str1_end": ["a", "b", "c"],
            "str2": ["XXX", "YYY", "ZZZ"],
        }
    )


def test_ends_with():
    df = make_test_df()
    assert df.select.ends_with("end").equals(
        df[["foo_int1_end", "int2_end", "str1_end"]]
    )


def test_contains():
    df = make_test_df()
    assert df.select.contains("float").equals(df[["foo_float1", "float2"]])


def test_contains_fail():
    df = make_test_df()
    assert df.select.contains("foobar").empty


def test_matches_start():
    df = make_test_df()
    assert df.select.matches("^str").equals(df[["str1_end", "str2"]])


def test_matches_end():
    df = make_test_df()
    assert df.select.matches("end$").equals(
        df[["foo_int1_end", "int2_end", "str1_end"]]
    )
