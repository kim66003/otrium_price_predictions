import requests
import json
import pandas as pd

# Load test data
with open('./assessment/data/test_data.json', 'r') as file:
  data_ = json.load(file)
#   as_json = data_.to_json()

# Make POST request using test data
post_req = requests.post("http://127.0.0.1:8000/api/predict", json=data_)

# Response as dictionary
res_dict = json.loads(post_req.json())

# Convert to dataframe
df = pd.DataFrame.from_dict(res_dict)
df_sale_price = df[['predicted_sale_price']].sort_index()
df_id_date = pd.read_csv('./assessment/data/test_data_prod_date.csv', encoding='utf8', index_col=0).sort_index()
df_sale_price.index = df_sale_price.index.astype('int64')
combine_df_results = df_id_date.join(df_sale_price)

# Save file
combine_df_results.to_csv("./assessment/predictions_data/predictions.csv", index=False)
