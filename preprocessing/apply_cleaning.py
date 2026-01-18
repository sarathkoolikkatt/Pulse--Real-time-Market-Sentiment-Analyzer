import pandas as pd
from clean_text import clean_text

# Load raw data
input_file = "data/merged_raw_data.csv"
output_file = "data/cleaned_data.csv"

df = pd.read_csv(input_file)

# Apply cleaning
df["clean_text"] = df["text"].apply(clean_text)

# Remove empty rows after cleaning
df = df[df["clean_text"].str.strip() != ""]

# Save cleaned data
df.to_csv(output_file, index=False)

print("Cleaned data saved to data/cleaned_data.csv")
