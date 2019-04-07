# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
import os

data = pd.DataFrame()

with open('../Code/msr-paraphrase-corpus/quora_duplicate_questions.tsv','r', encoding="utf-8") as tsvin:
    data = data.from_csv(tsvin, sep='\t', header=0)

data.columns=['#1 ID', '#2 ID', '#1 String', '#2 String', 'Quality']
data['split'] = np.random.randn(data.shape[0], 1)
msk = np.random.rand(len(data)) <= 0.7

train = data[msk]
test = data[~msk]

train_file = open('train.txt', 'a')
test_file = open('test.txt', 'a')

data[msk].to_csv('../train.csv', mode='w', columns=['Quality', '#1 ID', '#2 ID', '#1 String','#2 String'], index=False)
data[~msk].to_csv('../test.csv', mode='w', columns=['Quality', '#1 ID', '#2 ID', '#1 String','#2 String'], index=False)

with open('../train.txt', "w", encoding="utf-8") as my_output_file:
    with open('../train.csv', "r", encoding="utf-8") as my_input_file:
        [ my_output_file.write("\t".join(row)+'\n') for row in csv.reader(my_input_file)]
    os.remove('../train.csv')
    my_output_file.close()
    
with open('../test.txt', "w", encoding="utf-8") as my_output_file:
    with open('../test.csv', "r", encoding="utf-8") as my_input_file:
        [ my_output_file.write("\t".join(row)+'\n') for row in csv.reader(my_input_file)]
    os.remove('../test.csv')
    my_output_file.close()
