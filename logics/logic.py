# import numpy as np
import pandas as pd


def convert_data(is_infile_json_lines, infile_elv_path, infile_exp_path, outfile_path):
    print(is_infile_json_lines)
    print(infile_elv_path)
    print(infile_exp_path)
    print(outfile_path)
    # dat_elv = pd.read_json(infile_elv_path, encoding='utf_8', lines=is_infile_json_lines)
    # dat_exp = pd.read_json(infile_exp_path, encoding='utf_8', lines=is_infile_json_lines)

    # converted = pd.merge(dat_elv, dat_exp, on='country').dropna(how='any').copy()
    # converted['dev_expectancy'] = converted['expectancy'] - converted['expectancy'].mean()
    # converted['dev_elevation'] = converted['elevation'] - converted['elevation'].mean()
    # converted.to_json(outfile_path, orient='records')
