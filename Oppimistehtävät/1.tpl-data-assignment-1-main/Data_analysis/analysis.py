import pandas as pd

def analyze_data(users):
    print("Analyzing user data...")
    #Convert data to df for analysis
    df = pd.DataFrame(users)
    #Display basic info about data
    print(f"Data shape (shape): {df.shape}")
    print("Two first rows of the data:")
    #First rows of data
    print(df.head(2))
    print("Two last rows of the data:")
    #Last rows of data
    print(df.tail(2))