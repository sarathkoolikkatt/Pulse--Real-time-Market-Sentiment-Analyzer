import pandas as pd

dfs = []

# Twitter data (optional)
if pd.io.common.file_exists("data/raw_data.csv"):
    dfs.append(pd.read_csv("data/raw_data.csv"))

# Reddit data
if pd.io.common.file_exists("data/reddit_raw_data.csv"):
    dfs.append(pd.read_csv("data/reddit_raw_data.csv"))

merged_df = pd.concat(dfs, ignore_index=True)

merged_df.to_csv("data/merged_raw_data.csv", index=False)

print(" Data merged successfully")
print(f"Total rows after merge: {len(merged_df)}")
