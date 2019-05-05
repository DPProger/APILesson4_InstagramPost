import os
import requests
from download_image import download_image


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    path = os.getcwd() + '/' + 'images' + '/'
    os.makedirs(path, mode=0o777, exist_ok=True)
    url = "https://api.spacexdata.com/v3/rockets/"

    response = requests.get(url)
    response.raise_for_status()
    array_rockets = response.json()

    for pos_array_rockets, array_rockets in enumerate(array_rockets):
        for pos_link, link in enumerate(array_rockets['flickr_images']):
            file_name = '{}spacex{}{}.jpeg'.format(path, pos_array_rockets, pos_link)
            download_image(link, file_name)