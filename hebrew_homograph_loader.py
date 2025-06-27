#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def find_header_line(filepath, first_field_name):
    """Finds the row index of the actual header in the file, according to the first field name."""
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if line.strip().startswith(first_field_name):
                return i
    raise ValueError(f"Header '{first_field_name}' not found in file.")


def load_data():
    words_filename = 'hebrew_homographs_stress_minimal_pairs.csv'
    skiprows = find_header_line(words_filename, first_field_name='niqqudless')

    words_df = pd.read_csv(words_filename, skiprows=skiprows)

    phrases_df = pd.read_csv("hebrew_homographs_stress_minimal_pairs_phrases_llm1.csv")
    return words_df, phrases_df


def example_run():
    words_df, phrases_df = load_data()
    print(words_df.columns)
    print(words_df['niqqudless'])
    print(words_df['heb1'])
    print(words_df['heb2'])

    print(phrases_df.columns)
    print(phrases_df['stressed'])
    print('--------')

if __name__ == '__main__':
    example_run()
