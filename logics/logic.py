# import numpy as np
import pandas as pd


def convert_data(infile_elv_path, infile_exp_path, outfile_path):
    dat_elv = pd.read_json(infile_elv_path, encoding='utf_8')
    dat_exp = pd.read_json(infile_exp_path, encoding='utf_8')

    converted = pd.merge(dat_elv, dat_exp, on='country').dropna(how='any').copy()
    converted['dev_expectancy'] = converted['expectancy'] - converted['expectancy'].mean()
    converted['dev_elevation'] = converted['elevation'] - converted['elevation'].mean()
    converted.to_json(outfile_path, orient='records')
