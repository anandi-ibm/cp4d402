from ibm_watson_studio_lib import access_project_or_space
wslib = access_project_or_space()

import pandas as pd

df_data_1 = pd.read_csv(wslib.mount.get_data_path('datalake_names.csv'))
df_data_1.head()
