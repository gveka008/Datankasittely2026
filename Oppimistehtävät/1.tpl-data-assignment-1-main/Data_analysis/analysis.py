import pandas as pd

def analyze_data(users):
    print("Analyzing user data...")
    df = pd.DataFrame(users)
    print(f"Data shape (shape): {df.shape}")
    print("Two first rows of the data:")
    print(df.head(2))
    print("Two last rows of the data:")
    print(df.tail(2))