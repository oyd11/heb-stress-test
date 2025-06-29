#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hebrew_homograph_loader

gloss_df, phrases_df = hebrew_homograph_loader.load_data()

print(f'columns: {list(phrases_df.columns)}')
# ['id', 'niqqudless', 'stressed', 'phrase', 'ind']



stressed_set = set(phrases_df['stressed'])

for word in sorted(stressed_set):
    word_df = phrases_df[phrases_df['stressed'] == word]
    phrases = word_df['phrase']

    print('-===-')
    print(f'{word=} {len(word_df)=}')
    print('------')
    for phrase, ind in zip(phrases.values, word_df['ind']):
        print(f'{ind} ::: {phrase}')

# experiement setup:


import numpy as np

def invert_permutation_numpy(permutation):
    return np.argsort(permutation)

permulation_len = len(phrases_df)
new_p = np.random.permutation(permulation_len)
# saving permutation for experiment
p = np.array(
      [235, 164, 167,  78, 174,  97, 143,   0,  98, 125, 168, 150, 185,
       209, 140, 153,  21, 171,  71, 238,  48,  20,   1, 214, 124,  46,
       126, 137,  64,  13, 186,  56, 202, 206,  54,  19,  23, 213, 217,
        52, 147,  66, 221, 132,  45,  50, 239, 190, 228,  83, 222, 114,
        29, 165,   7,  85, 199, 113, 189,  95,   6,  40,  32, 183, 177,
        80,   4,  96, 205, 111, 105, 203, 207,  33, 188,  11, 127, 175,
        75, 215, 116, 148,  35, 144,  12, 146, 160,  76, 218,  58, 176,
        36,  22,  38,  10,  61, 211,  60,   9, 131, 216, 110,   8, 115,
        86, 135,  25, 149, 157, 101, 191,  51,  69, 138, 192, 225,  57,
       156,   3, 154, 118, 122, 158,  14,  17,  93, 121, 129, 155,  72,
       161, 200,  44, 231, 159,  65, 184, 119, 133, 201, 169, 106, 178,
       195, 180, 233, 234,  49, 193, 109,  18,  73, 196, 103, 142, 134,
       166,  74,  34, 181, 100,  63, 170,  30, 236, 232,  43, 145,  81,
        90,  55,  16,  27, 128,  47, 107,  31, 230,  91, 141, 151,  94,
        62,  24, 208, 102,  87, 136, 139,  67,  42,  53,  15, 237,  82,
       219, 163, 108,  37, 227, 197, 182, 204,  41, 162, 220, 152, 179,
       130,   2,   5, 117, 212, 104,  70,  59, 120, 173, 194, 223, 210,
       198,  28,  39, 123, 226,  68, 224, 187,  88,  26,  89,  77,  92,
       229, 172,  79,  99, 112,  84])

q = invert_permutation_numpy(p)

phrases_experiemnt_df = phrases_df.iloc[p]
back = phrases_experiemnt_df.iloc[q]