import argparse 
import nbimporter  

import gzip
import shutil
import os
import json 
import pandas as pd
import numpy as np

# ML
from sklearn.feature_selection import SelectFromModel

from joblib import dump, load


from main import generate_predictions 

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run the model on your json.gz file.')
    
    # Define the required and optional arguments
    parser.add_argument('--json_gz_file', type=str, required=True, help='Path to the input JSON GZ file')
    parser.add_argument('--selector', type=str, default='../model/selector.joblib.gz', help='Path to selector file')
    parser.add_argument('--classifier', type=str, default='../model/rf_classifier.joblib.gz', help='Path to classifier file')
    parser.add_argument('--output_path', type=str, default='default', help='Optional path to save the output')
    parser.add_argument('--include_features', type=str, default=False, help='Optional path to save the output')
    
    # Parse the arguments
    args = parser.parse_args()
    
    
    # Call the generate_predictions function with the parsed parameters
    generate_predictions(args.json_gz_file, args.selector, args.classifier, args.output_path, args.include_features)