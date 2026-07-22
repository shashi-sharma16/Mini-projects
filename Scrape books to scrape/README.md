# Scrape Books to Scrape

## Overview

Scrape Books to Scrape is a Python-based web scraping project that extracts book titles and prices from the **Books to Scrape** website and stores the collected data in a JSON file. The project demonstrates how to fetch web pages, parse HTML, extract structured information, handle pagination, and save the scraped data in a reusable format.

## Features

* Scrapes book titles and prices from Books to Scrape
* Automatically follows pagination to collect multiple pages of data
* Collects a specified number of books (default: 70)
* Saves the extracted data to a JSON file
* Handles network-related exceptions gracefully
* Uses a clean and modular Python code structure

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* JSON Module
* urllib.parse

## Project Structure

```
Scrape-Books-to-Scrape/
├── scrape.py
├── books_data.json
├── README.md
└── .gitignore
```

## Sample Output

The scraper generates a JSON file containing the title and price of each scraped book.

```json
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77"
  },
  {
    "title": "Tipping the Velvet",
    "price": "£53.74"
  },
  {
    "title": "Soumission",
    "price": "£50.10"
  }
]
```

A sample **books_data.json** file is included in this repository.

## Learning Outcomes

This project helped me understand how to:

* Send HTTP requests using the `requests` library
* Parse HTML using BeautifulSoup
* Extract information using CSS selectors
* Handle pagination while scraping multiple pages
* Handle network-related exceptions
* Store structured data in JSON format
* Organize Python code into reusable functions

## License

This project is intended for learning and educational purposes.
