import pandas as pd
import snowflake
from snowflake.connector.pandas_tools import write_pandas
from restApi import api_request
url = 'https://fake-json-api.mock.beeceptor.com/users'
users = api_request(url)
if users:
    df = pd.DataFrame(users)
    print(df)
    # conn = snowflake.connector.connect(
    #     user='***',
    #     password='***',
    #     account='***',
    #     warehouse='***',
    #     database='***',
    #     schema='***'
    # )
    # write_pandas(conn, df, 'USERS', auto_create_table=True, overwrite=True)
    print("데이터 저장 완료!")
else:
    raise ValueError("No users found!")