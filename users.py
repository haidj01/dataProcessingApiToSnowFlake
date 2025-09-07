import pandas as pd
from snowflake_operation import dataframe_to_snowflake
from restApi import api_request
url = 'https://fake-json-api.mock.beeceptor.com/users'
users = api_request(url)
if users:
    df = pd.DataFrame(users)
    dataframe_to_snowflake(df, 'USERS',"PUBLIC")
else:
    raise ValueError("No users found!")