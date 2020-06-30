from logics.logic import convert_data


INDATA_PATH = 'trydata/input'
FILENAME_C_ELEVATION = "country-by-elevation.json"
FILENAME_C_EXPECTANCY = "country-by-life-expectancy.json"
OUTFILE_PATH = 'trydata/output/data.json'

if __name__ == '__main__':
    convert_data(
        is_infile_json_lines=False,
        infile_elv_path=INDATA_PATH + "/" + FILENAME_C_ELEVATION,
        infile_exp_path=INDATA_PATH + "/" + FILENAME_C_EXPECTANCY,
        outfile_path=OUTFILE_PATH)
