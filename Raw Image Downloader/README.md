# Raw Image Downloader

## Overview

Raw Image Downloader is a Python-based web scraping project that downloads the cover images of the first 10 books from the Books to Scrape website. The project demonstrates how to retrieve image URLs, download files using streamed requests, and save them locally with clean filenames.

## Features

* Scrapes the first 10 book listings
* Extracts book cover image URLs
* Downloads images using streamed requests
* Saves images with sanitized filenames
* Organizes downloaded images in a dedicated folder

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* urllib.parse
* os
* re

## Project Structure

```text
Raw-Image-Downloader/
├── images/
├── scraper.py
├── README.md
└── .gitignore
```

## Sample Output

The scraper downloads the cover images of the first 10 books and stores them in the `images/` folder.

A sample `images/` folder is included in this repository.

## Learning Outcomes

This project helped me understand how to:

* Download files using streamed HTTP requests
* Extract image URLs from HTML
* Save files with custom filenames
* Work with file and directory operations in Python
* Organize a web scraping project effectively

## License

This project is intended for learning and educational purposes.
