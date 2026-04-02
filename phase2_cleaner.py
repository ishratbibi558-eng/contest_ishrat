import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def remove_duplicates(self):
        before = len(self.dataframe)
        self.dataframe.drop_duplicates(inplace=True)
        after = len(self.dataframe)
        print(f"Removed {before - after} duplicate rows.")

    def handle_missing_values(self):
        missing_info = self.dataframe.isnull().sum()
        print(f"Missing values before cleaning:\n{missing_info[missing_info > 0]}")
        self.dataframe.fillna(self.dataframe.mean(), inplace=True)
        missing_info_after = self.dataframe.isnull().sum()
        print(f"Missing values after cleaning:\n{missing_info_after[missing_info_after > 0]}")

    def detect_outliers(self):
        q1 = self.dataframe.quantile(0.25)
        q3 = self.dataframe.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outlier_condition = (self.dataframe < lower_bound) | (self.dataframe > upper_bound)
        outliers = self.dataframe[outlier_condition.any(axis=1)]
        print(f"Detected {len(outliers)} outlier rows:\n{outliers}")

    def show_example_operations(self):
        print("\n--- Example of Cleaning Operations ---")
        # Example data
        print(self.dataframe.head())

# Example usage
if __name__ == '__main__':
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 2, np.nan, 4, 5, 6, 100],
        'B': [5, 6, 7, 8, np.nan, 10, 5, 0],
    }
    df = pd.DataFrame(data)
    cleaner = DataCleaner(df)

    print("\n--- Initial Data ---")
    cleaner.show_example_operations()
    cleaner.remove_duplicates()
    cleaner.handle_missing_values()
    cleaner.detect_outliers()
    cleaner.show_example_operations()  
