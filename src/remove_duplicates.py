from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "raw_dataset.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed_dataset.csv"


def remove_duplicates(input_path=INPUT_FILE, output_path=OUTPUT_FILE):
    """
    Read a CSV file, remove duplicate rows, and save the cleaned dataset.
    """
    df = pd.read_csv(input_path)
    cleaned_df = df.drop_duplicates()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(output_path, index=False)

    return cleaned_df


if __name__ == "__main__":
    cleaned = remove_duplicates()
    print(f"Duplicate removal complete. Rows after cleaning: {len(cleaned)}")
