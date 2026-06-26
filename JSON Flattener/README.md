# JSON Flattener

A simple Python utility that converts nested JSON objects into a flattened JSON format using customizable key separators.

## Features

* Flattens nested dictionaries and lists
* Supports custom key separators (e.g., `.`, `-`, `_`)
* Saves the flattened output to a JSON file
* Includes sample input and output JSON files

## Technologies Used

* Python
* `json` module
* `os` module

## Project Structure

```text
JSON-Flattener/
│── json_flattener.py
│── nested_data.json       # Sample input file
│── flattened_data.json    # Sample output file
└── README.md
```

## Example

**Input (`nested_data.json`)**

```json
{
  "user": {
    "name": "Alice",
    "age": 25
  }
}
```

**Output (`flattened_data.json`)**

```json
{
  "user.name": "Alice",
  "user.age": 25
}
```

## Error Handling

* Checks if the input file exists.
* Handles invalid JSON and unexpected errors gracefully.
