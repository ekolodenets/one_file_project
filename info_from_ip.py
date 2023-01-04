import requests
from pyfiglet import Figlet
import folium

def get_info_from_ip(ip='127.0.0.1'):

    try:
        response = requests.get(url=f'https://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Organisation]': response.get('org'),
            '[Region]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Latitude]': response.get('lat'),
            '[Longitude]': response.get('lon')
        }

        for k, v in data.items():
            print(f'{k}: {v}')
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

    # create html file with location on the map
    map_location = folium.Map(location=[response.get('lat'), response.get('lon')])
    map_location.save(f'{response.get("query")}_{response.get("city")}.html')

def main():
    preview = Figlet(font='slant')
    print(preview.renderText('IP INFO'))
    ip = input('Please enter a target IP: ')

    get_info_from_ip(ip=ip)

if __name__ == '__main__':
    main()