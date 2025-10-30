# Ballard---Scraping
A Python automation project using Selenium to scrape attorney and staff profiles from the Ballard Spahr website. It dynamically loads all results per alphabetical filter, extracts structured data such as name, role, email, contact number, and location, and exports the dataset into a JSON file.

This project uses Selenium automation to scrape professional profile data from the Ballard Spahr website. It iterates through all alphabetical filters (A–Z), loads all results dynamically by clicking “Load More,” and extracts detailed information about each person including:

- Full Name  
- Position / Role  
- Email  
- Contact Number  
- Office Location  

All extracted data is saved in a structured JSON format for further processing.

---

## 🚀 Features

✅ Fully automated browsing  
✅ Handles cookie popup automatically  
✅ Dynamic "Load More" button clicking  
✅ Structured data output in JSON format  
✅ Complete scan A–Z

---

## 🧰 Tech Stack

| Component | Used For |
|----------|----------|
| Python 3 | Main Script |
| Selenium WebDriver | Browser Automation |
| Chrome + Chromedriver | Page Rendering & Execution |
| JSON | Data Storage |

---

## 📦 Installation

## 1️⃣ Clone the repository  
```
git clone https://github.com/<your-username>/ballardspahr-scraper.git
cd ballardspahr-scraper
```
## 2️⃣ Install the dependencies
```
pip install selenium
```
## 3️⃣ Download compatible ChromeDriver
```
➡ https://chromedriver.chromium.org/downloads
Make sure the version matches your Chrome browser version.
```
▶️ Usage
Run the script:
```
python scraper.py
The output will be stored as: data.json
```
📁 Output JSON Example
```
json
[
    {
        "Name": "John Doe",
        "Role": "Partner",
        "Mail": "doe@ballardspahr.com",
        "Phone": "123.456.7890",
        "Location": "Philadelphia"
    }
]
```
## ⚠ Legal Notes
This script is strictly for learning and research.
Before running web scrapers on production sites:

Always check and respect the website’s Terms of Service

Follow robots.txt guidelines

Avoid aggressive scraping frequencies

## 📝 License
Distributed for educational use only.
You may modify and adapt the code as needed.


## Improvements

If you'd like, I can also:

✅ Add pagination progress logging  
✅ Save as CSV / Excel  
✅ Add try/except for missing fields  
✅ Make it multithreaded for speed  
✅ Convert everything into a full GitHub repository structure













