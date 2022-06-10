# read the data from the data source
# save it in data\\raw for further processing

import os
from get_data import read_params, get_data
import argparse


def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_columns = [column.replace(" ", "_") for column in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]

    df.to_csv(raw_data_path, sep=",", index=False, header=new_columns)


if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument("--config", default="params.yaml")
    parsed_args = arg.parse_args()
    load_and_save(config_path=parsed_args.config)
