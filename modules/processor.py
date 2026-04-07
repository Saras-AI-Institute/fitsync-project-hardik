import pandas as pd

# Function to load and clean the CSV data
def load_data():
    # Path to the CSV file
    file_path = 'data/health_data.csv'
    
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)
    
    # Fill missing 'steps' with the median value of the column
    data['steps'].fillna(data['steps'].median(), inplace=True)
    
    # Fill missing 'sleep_hours' with a default value of 7.0
    data['sleep_hours'].fillna(7.0, inplace=True)
    
    # Fill missing 'heart_rate_bpm' with a default value of 68
    data['heart_rate_bpm'].fillna(68, inplace=True)
    
    # Fill missing values in all other numeric columns with their respective median values
    numeric_cols = data.select_dtypes(include='number').columns
    for column in numeric_cols:
        if column not in ['steps', 'sleep_hours', 'heart_rate_bpm']:
            data[column].fillna(data[column].median(), inplace=True)
    
    # Convert the 'date' column to datetime objects for easy date manipulation
    data['date'] = pd.to_datetime(data['date'])
    
    # Return the cleaned DataFrame
    return data
