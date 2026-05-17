import os
import pandas as pd
from src.remove_duplicates import remove_duplicates

def test_duplicate_removal():
    output_file = "data/test_processed_dataset.csv"
    df = remove_duplicates("data/dataset.csv", output_file)
    assert df.duplicated().sum() == 0

def test_output_file_created():
    output_file = "data/test_processed_dataset.csv"
    remove_duplicates("data/dataset.csv", output_file)
    assert os.path.exists(output_file)

def test_final_row_count():
    output_file = "data/test_processed_dataset.csv"
    df = remove_duplicates("data/dataset.csv", output_file)
    assert len(df) == 918
