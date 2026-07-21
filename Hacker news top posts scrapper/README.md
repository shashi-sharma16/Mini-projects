# Hacker News Top 20 Scraper

## Overview

Hacker News Top 20 Scraper is a Python-based web scraping project that retrieves the latest **Top 20 posts** from the Hacker News homepage and stores the extracted data in a CSV file. The project demonstrates how to fetch web content, parse HTML, extract relevant information, and organize it into a structured format.

---

## Features

- Retrieves the latest Top 20 posts from Hacker News
- Extracts the title and URL of each post
- Saves the extracted data to a CSV file
- Handles network-related exceptions gracefully
- Uses a clean and modular Python code structure

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- CSV Module

---

## Project Structure

```text
Hacker-News-Top-Posts/
├── scraper.py
├── hn_top20.csv
├── README.md
└── .gitignore
```
---

## Sample Output

The scraper generates a CSV file containing the title and corresponding URL of the latest Top 20 Hacker News posts.

| Title | URL |
|-------|-----|
| Example Post 1 | https://example.com |
| Example Post 2 | https://example.com |
| Example Post 3 | https://example.com |

A sample `hn_top20.csv` file is included in this repository.

---

## Learning Outcomes

This project helped me understand how to:

- Send HTTP requests using the `requests` library
- Parse HTML using BeautifulSoup
- Extract information using CSS selectors
- Handle network-related exceptions
- Store structured data in CSV format
- Organize Python code into reusable functions

---

## License

This project is intended for learning and educational purposes.