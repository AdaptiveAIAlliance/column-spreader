import pandas as pd

def get_unique_values(csv_file):
    chunk_size = 10_000  # Number of rows to process at a time
    unique_values = set()

    # Iterate over the CSV file in chunks
    for chunk in pd.read_csv(csv_file, chunksize=chunk_size, usecols=[0]):
        unique_values.update(chunk.iloc[:, 0].unique())

    return unique_values

def write_unique_values(unique_values, output_file):
    with open(output_file, "w") as file:
        for value in unique_values:
            file.write(str(value) + "\n")

# csv_file_path = "path/to/your/file.csv"
csv_file_path = "./sample.csv"
output_file_path = "./output_file.txt"

unique_values = get_unique_values(csv_file_path)
write_unique_values(unique_values, output_file_path)

print("Unique values from the first column have been written to", output_file_path)
