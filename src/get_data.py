## read params
## process
## return dataframe

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    data_path = config['data_source']['s3_source']
    df = pd.read_csv(data_path)
    return df


if __name__ == '__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument("--config", default="parameters.yaml")
    parsed_args = arg.parse_args()
    get_data(config_path=parsed_args.config)
