import pandas as pd
import snowflake
from snowflake.connector.pandas_tools import write_pandas

def dataframe_to_snowflake(df: pd.DataFrame, table: str, schema: str = None):
    with snowflake.connector.connect(
        user='***',
        password='***',
        account='***',
        warehouse='***',
        database='***',
        schema=schema
    ) as conn:
        write_pandas(conn, df, table, auto_create_table=True, overwrite=True)
        print("데이터 저장 완료!")