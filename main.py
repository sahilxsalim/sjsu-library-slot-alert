import requests
from utils import increment_date
import send_email

def fetch_slots(date):
    headers = {
        'authority': 'booking.sjlibrary.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://booking.sjlibrary.org',
        'referer': 'https://booking.sjlibrary.org/reserve/king',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'lid': '1164',
        'gid': '0',
        'eid': '-1',
        'seat': '0',
        'seatId': '0',
        'zone': '0',
        'start': date,
        'end': increment_date(date, 1),
        'pageIndex': '0',
        'pageSize': '18',
    }

    response = requests.post(
        'https://booking.sjlibrary.org/spaces/availability/grid', headers=headers, data=data)

    response_data = response.json()
    slots = response_data.get('slots')
    if slots:
        send_email.send_email('Slots available')
    else:
        print('No slots available')

if __name__ == '__main__':
    fetch_slots('2023-11-13')
