import pandas as pd

class DataPreprocessor:
    @staticmethod
    def clean_data(data):
        df = pd.DataFrame(data)
        df.fillna("Unknown", inplace=True)
        return df

    @staticmethod
    def normalize_data(df):
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
        return df
