import os
import csv
# Folder path to scan 
folder_path = r'C:\Users\kilia\OneDrive\Documents\GitHub\Portfolio\ghcnd_all'  # Change this to your folder path
search_string = ['TMAX','TMIN']        # Update this
output_csv = 'matched_lines.csv'


# Open CSV file for writing
with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    #for filename in os.listdir(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_number, line in enumerate(f, start=1):
                    line_stripped = line.strip().replace('\n', '').replace('\r', '')
                    # Match if line contains ANY of the strings
                    if any(s in line_stripped for s in search_string):
                        writer.writerow([line_stripped])
               
            print(f"Finished processing: {filename}")
