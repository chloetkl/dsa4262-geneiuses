import argparse 
import nbimporter  
from main import generate_predictions 

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run the model on your json.gz file.')
    
    # Define the expected arguments
    parser.add_argument('--json_gz_file', type=str, required=True, help='Path to the input JSON GZ file')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Set default values for selector_file and classifier_file
    selector_file = '../model/selector.joblib'   # Update with your default path
    classifier_file = '../model/rf_classifier.joblib'  # Update with your default path
    
    # Call the generate_predictions function with the parsed parameters
    generate_predictions(args.json_gz_file, selector_file, classifier_file)