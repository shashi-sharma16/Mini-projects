# CSV to JSON Converter

A simple Python project that converts data from a CSV file into JSON format using Python's built-in `csv` and `json` modules.

## Features

* Reads data from a CSV file
* Converts CSV records into JSON format
* Saves the converted data to a JSON file
* Displays a preview of the converted records
* Handles missing input files

## Technologies Used

* Python
* csv module
* json module
* os module

## Example

**Input:** `data.csv`

```csv
id,name,email
1,John,john@example.com
2,Alice,alice@example.com
```

**Output:** `converted_data.json`

```json
[
  {
    "id": "1",
    "name": "John",
    "email": "john@example.com"
  }
]
```
