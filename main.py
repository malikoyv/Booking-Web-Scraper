from bs4 import BeautifulSoup
import requests

# def parseListing(listing_url):
    

def main():
    # Replace checkin/checkout dates if you wish
    checkin = "2024-03-30"
    checkout = "2024-03-31"

    # Connecting to the website
    URL = f'https://www.booking.com/searchresults.html?ss=Poland&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaLYBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuALtgIGwBsACAdICJDQ3MzNiMDBkLTdkZDEtNGUwMS1iZmY0LWE4Mzk3ZDBkMmZmMtgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=170&dest_type=country&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=d95a69b613ab01d9&ac_meta=GhA1MjUyNjliYmVlNjkwMTY0IAAoATICZW46BnBvbGFuZEAASgBQAA%3D%3D&checkin={checkin}&checkout={checkout}&group_adults=1&no_rooms=1&group_children=0'

    # Change "User-Agent" upon your browser settings
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    response = requests.get(URL, headers=headers)

    product_links = []
    hotels = []
    x = 0

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_list = soup.find_all('div', class_= 'c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4')

        for item in product_list:
            for link in item.find_all('a', class_='a78ca197d0'):
                product_links.append(link['href'])
                if len(product_links) == 6:
                    break
            if len(product_links) == 6:
                break
    else:
        print(response.status_code)

    for link in product_links:
        request = requests.get(link, headers=headers)

        soup = BeautifulSoup(request.content, 'html.parser')
        title_el = soup.find('h2', class_='d2fee87262 pp-header__title')
        title = title_el.getText(strip=True) if title_el else 'Title not found'
        price_el = soup.find('span', class_= 'prco-valign-middle-helper')
        price = price_el.getText(strip=True).replace('\xa0', ' ') if price_el else 'Price not found'
        try:
            rating_el = soup.find('div', class_='ac4a7896c7')
            rating = rating_el.getText(strip=True).replace('Scored ', '') if rating_el else 'Rating not found'
        except:
            rating = '-'
        quantity_el = soup.find('span', class_='a3b8729ab1 f45d8e4c32 d935416c47')
        quantity = quantity_el.getText(strip=True).replace('·', '') if quantity_el else 'Quantity of reviews not found'

        hotel = {
            'URI': link,
            'title': title,
            'price': price,
            'rating': rating,
            'quantity': quantity
        }
        hotels.append(hotel)

    for i in hotels:
        print(i)

main()