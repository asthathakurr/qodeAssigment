import pyarrow as pa
import pyarrow.parquet as pq

class Storage:
    def save_parquet(self, df, path="data/tweets.parquet"):
        table = pa.Table.from_pandas(df)
        pq.write_table(table, path)
