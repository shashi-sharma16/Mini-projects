# Cover Image Downloader using wget

## Overview

Cover Image Downloader using wget is a Python-based web scraping project that downloads the cover images of the first 10 books from the Books to Scrape website. The project demonstrates how to extract image URLs, download images using wget, and save them locally with clean filenames.

## Features

- Scrapes the first 10 book listings
- Extracts book cover image URLs
- Downloads images using wget
- Saves images with sanitized filenames
- Organizes downloaded images in a dedicated folder
- Automatically creates the images directory if it does not exist

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- wget
- urllib.parse
- os
- re

## Project Structure

```
Cover-Image-Downloader-using-wget/
├── images/
├── image_wget.py
├── README.md
└── .gitignore
```

## Sample Output

The image_wget.py downloads the cover images of the first 10 books and stores them in the `images/` folder.

A sample `images/` folder is included in this repository.

## Learning Outcomes

This project helped me understand how to:

- Extract image URLs from HTML pages
- Download images using wget
- Work with URL handling using urllib
- Create and manage directories in Python
- Generate clean filenames using regular expressions
- Organize a web scraping project effectively

## License

This project is intended for learning and educational purposes.