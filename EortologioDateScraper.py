import requests
from bs4 import BeautifulSoup
import pyperclip

def eortologio(name):
    url = f"https://www.eortologio.net/pote_giortazei/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        target_element = soup.find("table", class_="table no-margin table-striped table-bordered calendar")

        if target_element:
            date_element = target_element.find("b").find("a")
            
            if date_element:
                date_text = date_element.text.strip()
            else:
                print("Date element not found on the page.")
                return None
        else:
            print("Element not found on the page.")
            return None
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

    return date_text

def reformat_date(date_text):
    # Convert the Greek month names to their corresponding numerical values
    greek_months = {
        "Ιανουαρίου": "01",
        "Φεβρουαρίου": "02",
        "Μαρτίου": "03",
        "Απριλίου": "04",
        "Μαΐου": "05",
        "Ιουνίου": "06",
        "Ιουλίου": "07",
        "Αυγούστου": "08",
        "Σεπτεμβρίου": "09",
        "Οκτωβρίου": "10",
        "Νοεμβρίου": "11",
        "Δεκεμβρίου": "12"
    }
    
    # Split the date text into day and month parts
    day, month = date_text.split(" ")

    # Reformat the date in M-D format
    formatted_date = f"{greek_months[month]}-{day}"
    
    return formatted_date

name = input("Give me a name: ")
date_text = eortologio(name)

if date_text:
    formatted_date = reformat_date(date_text)
    print(f"{name} is celebrating on {formatted_date}.")
    
    # Copy the formatted date to the clipboard
    pyperclip.copy(formatted_date)
    print("Formatted date copied to clipboard.")
