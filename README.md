# Booking Web Scraper
This Python script scrapes hotel data from Booking.com including information like title, price, rating, and quantity of reviews. It utilizes BeautifulSoup for web scraping and making HTTP requests. The scraped data can be saved to CSV and JSON files for further analysis.

## How to Install and Run the Project
1. Clone the repository:
`https://github.com/malikoyv/Booking-Web-Scraper.git`
2. Install the required packages:
`pip install bs4 requests secure-smtplib`
3. Change your browser setting in the project:
- Go to [the website](https://www.httpbin.org/get) and copy the "User-Agent" line.
- Paste it in the `main.py` file instead of the `headers` variable.
4. Change dates:
Change the dates of check-in and checkout if desired in the `CHECKIN` and `CHECKOUT` variables in `main.py`.
5. Change URI:
Change the link of the booking website if desired in the `URI` variable in `main.py` (because now you scrape Polish hotels :shipit:)

## How to Use the Project
1. Run the `main.py` script.
2. The script will scrape hotel data from Booking.com based on the specified URI, check-in and check-out dates and save the information to CSV and JSON files (`hotel_data.csv` and `hotel_data.json`, respectively) in the project directory.

## Credits
- Developed by [Yehor Malikov](https://github.com/malikoyv)

## License
This project is licensed under the [MIT License](https://github.com/malikoyv/Booking-Web-Scraper/blob/main/LICENSE).

### Additional
- **How to Contribute to the Project:** To contribute to the project, fork the repository, make your changes in a new branch, and submit a pull request to have your modifications reviewed and merged.
- **Documentation** [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

