import pandas as pd
import dask.dataframe as dd
import numpy as np


input = r"C:\Users\kilia\OneDrive\Documents\GitHub\Portfolio\chunks"

df = dd.read_parquet(input)

# Melt day columns into a single column of daily values
day_cols = [f"day_{i+1}" for i in range(31)]
df_long = df.melt(id_vars=["station", "yyyymm", "variable"], 
                  value_vars=day_cols, 
                  var_name="day", 
                  value_name="value")

# Step 3: Clean

df_long["value"] = df_long["value"].astype(str)

# Keep only values that look like a number, optionally with a minus or decimal
valid = df_long["value"].str.match(r"^-?\d+(\.\d+)?$")

# Filter to only keep valid rows
df_long = df_long[valid]

df_long["value"] = df_long["value"].astype("float")
df_long["value"] = df_long["value"].mask(df_long["value"] == -9999, np.nan)
df_long = df_long.dropna(subset=["value"])
df_long["year"] = df_long["yyyymm"].str[:4]

# Step 4: Aggregate
avg_by_year = df_long.groupby(["year", "variable"])["value"].mean().reset_index()
avg_by_year["variable"] = avg_by_year["variable"].astype("category")

# Step 5: Pivot
result = avg_by_year.pivot_table(index="year", columns="variable", values="value")
result = result.rename(columns={"TMAX": "avg_TMAX", "TMIN": "avg_TMIN"}).reset_index()

# Step 6: Convert to °C
result["avg_TMAX"] = result["avg_TMAX"] / 10
result["avg_TMIN"] = result["avg_TMIN"] / 10

# Final result
result = result.compute()
print(result.head())
