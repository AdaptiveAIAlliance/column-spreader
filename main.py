import pandas as pd
import csv


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


def write_unique_values_into_csv(unique_values, output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Unique Values"])  # Write header row

        for value in unique_values:
            writer.writerow([value])


def get_value_start_with(csv_file, start_with):
    chunk_size = 10_000  # Number of rows to process at a time
    output_values = set()

    # Iterate over the CSV file in chunks
    for chunk in pd.read_csv(csv_file, chunksize=chunk_size, usecols=[0]):
        filtered_values = chunk.iloc[:, 0].astype(
            str).str.startswith(start_with)
        output_values.update(
            chunk.loc[filtered_values, chunk.columns[0]].unique())

    return output_values


def get_numbers_with_repetition(csv_file, digit, number_of_repetition):
    chunk_size = 10_000  # Number of rows to process at a time
    output_values = set()

    # Iterate over the CSV file in chunks
    for chunk in pd.read_csv(csv_file, chunksize=chunk_size, usecols=[0]):
        filtered_values = chunk.iloc[:, 0].astype(str).apply(
            lambda x: str(x)[3:].count(str(digit)) == number_of_repetition)
        output_values.update(
            chunk.loc[filtered_values, chunk.columns[0]].unique())

    return output_values


# csv_file_path = "path/to/your/file.csv"
csv_file_path = "./sample.csv"
output_file_path = "./output_file.csv"
numbers_with_three_six_path = "./numbers_with_three_six.csv"

# unique_values = get_value_start_with(csv_file_path, '912')
# write_unique_values(unique_values, output_file_path)

numbers_with_three_six = get_numbers_with_repetition(csv_file_path, 6, 3)
write_unique_values(numbers_with_three_six, numbers_with_three_six_path)


# print("Unique values from the first column have been written to", output_file_path)
