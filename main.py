import pandas as pd
import snowflake
from snowflake.connector.pandas_tools import write_pandas
from restApi import api_request

users = api_request()
df = pd.DataFrame(users)

conn = snowflake.connector.connect(
    user='***',
    password='***',
    account='***',
    warehouse='***',
    database='***',
    schema='***'
)

write_pandas(conn, df, 'USERS', auto_create_table=True, overwrite=True)
print("데이터 저장 완료!")