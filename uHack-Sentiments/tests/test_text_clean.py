import pandas as pd
from src.text_ops import(
    calculate_wcount,
    lowercase_string,
    lowercase_column,
)
import pytest


@pytest.fixture()
def dummy_df():
    string_col = ['Hey how are you',
                  'Love is life',
                  ]
    df_dict = {'string': string_col, 'word_count': [4, 3]}
    df = pd.DataFrame(df_dict)
    return df


@pytest.fixture
def lowercased_df():
    string_col = ['hey how are you',
                  'love is life',
                  ]
    df_dict = {'string': string_col}
    df = pd.DataFrame(df_dict)
    return df


def test_calculate_wcount(dummy_df):
    expected_df = dummy_df
    string_col = ['Hey how are you',
                  'Love is life',
                  ]
    df_dict = {'string': string_col, }
    new_df = pd.DataFrame(df_dict)
    new_df['word_count'] = calculate_wcount(new_df, 'string')
    assert new_df.equals(expected_df)


def test_lowercase_string():
    assert lowercase_string('abc') == 'abc'
    assert lowercase_string('ABC') == 'abc'
    assert lowercase_string('Abc123') == 'abc123'


def test_lowercase_column(dummy_df, lowercased_df):
    actual_df = lowercase_column(dummy_df.drop(['word_count'], axis=1), col='string')
    assert actual_df.equals(lowercased_df)
