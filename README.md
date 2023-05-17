# CSV Unique Values Extractor

This Python script reads a CSV file and extracts the unique values from the first column. It utilizes the `pandas` library for efficient processing of large CSV files.

## Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)

## Usage

1. Make sure you have Python installed on your system.

2. Install the required `pandas` library by running the following command:
pip install pandas

3. Place your CSV file in the desired location and update the `csv_file_path` variable in the script with the path to your CSV file.

4. Specify the output file path by updating the `output_file_path` variable in the script. The unique values from the first column will be written to this file.

5. Run the script using the following command:
python main.py

6. The script will process the CSV file, extract the unique values from the first column, and write them to the specified output file.

7. Once the script finishes execution, you can find the output file with the unique values.

## Customize

- If you need to modify the script to extract unique values from a different column, update the `usecols` parameter in the `pd.read_csv` function. For example, to extract unique values from the second column, change `usecols=[0]` to `usecols=[1]`.

- Adjust the `chunk_size` variable to control the number of rows processed at a time. Larger values may require more memory but can improve processing speed.

## Notes

- Processing large CSV files may require significant system resources and time. Ensure that your system has enough memory and processing power to handle the size of your file.

- This script assumes that the CSV file has a header row and uses a comma (`,`) as the delimiter. If your CSV file has a different format, you may need to modify the script accordingly.

- For more information on the `pandas` library and its capabilities, refer to the [pandas documentation](https://pandas.pydata.org/docs/).
