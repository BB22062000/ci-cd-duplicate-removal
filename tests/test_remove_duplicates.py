import pandas as pd
from src.remove_duplicates import remove_duplicates


def test_remove_duplicates_removes_duplicate_rows(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    test_data = pd.DataFrame({
        "id": [1, 2, 2, 3],
        "name": ["Alice", "Bob", "Bob", "Charlie"],
        "score": [85, 90, 90, 78]
    })

    test_data.to_csv(input_file, index=False)

    cleaned_df = remove_duplicates(input_file, output_file)

    assert len(cleaned_df) == 3
    assert cleaned_df.duplicated().sum() == 0
    assert output_file.exists()


def test_output_file_contains_expected_rows(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    test_data = pd.DataFrame({
        "id": [1, 1, 2],
        "name": ["Alice", "Alice", "Bob"],
        "score": [85, 85, 90]
    })

    test_data.to_csv(input_file, index=False)

    remove_duplicates(input_file, output_file)
    output_df = pd.read_csv(output_file)

    assert len(output_df) == 2
    assert list(output_df["name"]) == ["Alice", "Bob"]
