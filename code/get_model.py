# Import libraries
import argparse 
import nbimporter  

import gzip
import shutil
import os
import json 
import pandas as pd
import numpy as np

# ML
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

from joblib import dump, load

from main import generate_model


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate the model from your json and labels file.')
    
    # Define the required and optional arguments
    parser.add_argument('--training_data_json', type=str, default='../data/dataset0.json.gz', help='Path to the input JSON GZ file')
    parser.add_argument('--labels', type=str, default='../data/data.info.labelled', help='Path to the input labels file')
    parser.add_argument('--selector', type=str, default='../model/selector.joblib.gz', help='Path to the selector file')
    parser.add_argument('--output_joblib_path', type=str, required=True, help='Path to save the output')
    parser.add_argument('--compress', type=bool, default=True, help='Compress model file')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the generate_predictions function with the parsed parameters
    generate_model(args.training_data_json, args.labels, args.selector, args.output_joblib_path, args.compress)
