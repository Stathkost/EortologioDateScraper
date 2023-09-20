# EortologioDateScraper

This Python script allows you to retrieve and format the celebration date for Greek names from the Eortologio website. It simplifies the process of finding name celebration dates and copies them to your clipboard for easy access. Perfect for anyone interested in Greek name celebrations.

## Overview

This Python script allows you to retrieve and format the celebration date for a given Greek name from the [Eortologio website](https://www.eortologio.net/). It then copies the formatted date to your clipboard for convenience.

## How it works

The program works as follows:

1. It takes a **Greek** name as input from the user.
2. It sends a request to the Eortologio website to search for the name's celebration date.
3. It parses the website's HTML content using BeautifulSoup to extract the celebration date.
4. It reformats the date from the Greek date format to a more standard format (M-D).
5. It displays the celebration date on the console.
6. It copies the formatted date to your clipboard for convenience.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- requests
- BeautifulSoup
- pyperclip

You can install these libraries using pip or using the requirements.txt file   
```pip install -r requirements.txt```

## How to use 

Follow these steps to use the script:

Clone this repository to your local machine:   
```git clone https://github.com/Stath_kost/EortologioDateScraper.git```

Change to the project directory: ```cd EortologioDateScraper```

Run the script: ```python celebration_date_scraper.py```

Enter a **Greek** name when prompted.

The celebration date will be displayed on the console, and it will also be copied to your clipboard.
