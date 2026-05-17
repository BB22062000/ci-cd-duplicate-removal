import pandas as pd

def remove_duplicates(input_file="data/dataset.csv", output_file="data/processed_dataset.csv"):
    df = pd.read_csv(input_file)
    cleaned_df = df.drop_duplicates()
    cleaned_df.to_csv(output_file, index=False)
    print(f"Duplicate removal complete. Rows after cleaning: {len(cleaned_df)}")
    return cleaned_df

if __name__ == "__main__":
    remove_duplicates()
