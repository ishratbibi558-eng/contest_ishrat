import pandas as pd
import requests

# Function to load CSV data
def load_csv_data(file_path):
    data = pd.read_csv(file_path)
    print("CSV Data Loaded:")
    print(data.head())
    return data

# Function to load JSON data
def load_json_data(url):
    response = requests.get(url)
    data = response.json()
    print("JSON Data Loaded:")
    print(data)
    return data

# Function to load Excel data
def load_excel_data(file_path):
    data = pd.read_excel(file_path)
    print("Excel Data Loaded:")
    print(data.head())
    return data

# Function to load data from an API
def load_api_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    print("API Data Loaded:")
    print(data)
    return data

# Example usage
if __name__ == '__main__':
    # Load CSV Data
    load_csv_data('path/to/your/file.csv')

    # Load JSON Data
    load_json_data('https://api.example.com/data.json')

    # Load Excel Data
    load_excel_data('path/to/your/file.xlsx')

    # Load API Data
    load_api_data('https://api.example.com/data')