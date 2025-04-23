import pandas as pd

input = r"C:\Users\kilia\OneDrive\Documents\GitHub\Portfolio\matched_lines.csv"

import pandas as pd
import re
import os

def parse_line(line):
    # Station ID (11 chars), Date (6 chars), Variable (4 chars)
    station = line[0:11]
    yyyymm = line[11:17]
    variable = line[17:21]

    # The rest of the line is daily values + flags
    data_part = line[21:].strip()

    # Match groups of "number + optional space + flag"
    # Ex: 289  X or 283X or 267  X
    matches = re.findall(r"(-?\d{1,4})\s*([A-Z]?)", data_part)

    # Just get the value (can also return flags separately if needed)
    values = [int(m[0]) if m[0] != '' else None for m in matches]

    # Return full parsed row
    return [station, yyyymm, variable] + values[:31]  # Just 31 days max

columns = ["station", "yyyymm", "variable"] + [f"day_{i+1}" for i in range(31)]

os.makedirs("chunks", exist_ok=True)
chunk_size = 15000
buffer = []
chunk_num = 0

with open(input, "r") as f:
    for i, line in enumerate(f):
        try:
            parsed = parse_line(line.strip())
            buffer.append(parsed)
        except Exception as e:
            print(f"Error parsing line {i}: {e}")

        if (i + 1) % chunk_size == 0:
            df = pd.DataFrame(buffer, columns=columns)
            df.to_parquet(f"chunks/part_{chunk_num}.parquet")
            buffer = []
            chunk_num += 1

# Save any leftover lines
if buffer:
    df = pd.DataFrame(buffer, columns=columns)
    df.to_parquet(f"chunks/part_{chunk_num}.parquet")
    
