import pandas as pd

class Processor:
    def clean(self, df):
        df['content'] = df['content'].astype(str).str.lower()
        df['content'] = df['content'].str.replace(r"[^a-zA-Z0-9# ]", "", regex=True)
        df.drop_duplicates(subset=['content'], inplace=True)
        return df.reset_index(drop=True)
