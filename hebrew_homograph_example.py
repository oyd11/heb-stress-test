#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hebrew_homograph_loader

words_df, phrases_df = hebrew_homograph_loader.load_data()

stressed_set = set(phrases_df['stressed'])

for word in sorted(stressed_set):
    word_df = phrases_df[phrases_df['stressed'] == word]
    phrases = word_df['phrase']

    print('-===-')
    print(f'{word=} {len(word_df)=}')
    print('------')
    print(phrases.values)
