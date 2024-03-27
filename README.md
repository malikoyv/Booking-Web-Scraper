# Booking Web Scraper
This Python script scrapes hotel data from Booking.com including information like title, price, rating, and quantity of reviews. It utilizes BeautifulSoup for web scraping and making HTTP requests. The scraped data can be saved to CSV and JSON files for further analysis.

## Table of Contents
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
- [How to Use the Project](#how-to-use-the-project)
- [Credits](#credits)
- [License](#license)

## How to Install and Run the Project
1. Clone the repository:
`https://github.com/malikoyv/Booking-Web-Scraper.git`
2. Install the required packages:
`pip install bs4 requests secure-smtplib`
3. Change your browser setting in the project:
- Go to [the website](httpbin.org/get) and copy the "User-Agent" line.
- Paste it in the `main.py` file instead of the `headers` variable.
4. Change dates:
Change the dates of check-in and checkout if desired in the `CHECKIN` and `CHECKOUT` variables in `main.py`.
5. Change URI:
Change the link of the booking website if desired in the `URI` variable in `main.py` (because now you scrape Polish hotels :shipit:)

## How to Use the Project
1. Run the `main.py` script.
2. The script will scrape hotel data from Booking.com based on the specified URI, check-in and check-out dates and save the information to CSV and JSON files (`hotel_data.csv` and `hotel_data.json`, respectively) in the project directory.

## Credits
- Developed by [Your Name](https://github.com/your_username)

## License
This project is licensed under the [MIT License](LICENSE).

### Additional README Sections
- **Badges:** Badges aren't included in this README, but you can add badges to your project to showcase important stats or information.
- **How to Contribute to the Project:** Contribution guidelines can be added if you intend to make this project open-source and welcome contributions from other developers.
- **Include Tests:** Tests can be added to ensure the reliability and functionality of the project. Instructions on how to run these tests can be included in this section.
