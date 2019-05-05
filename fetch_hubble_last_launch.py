import os
import requests
from download_image import download_image


def fetch_hubble_last_launch():
    path = os.getcwd() + '/' + 'images' + '/'
    os.makedirs(path, mode=0o777, exist_ok=True)
    name_collection = 'spacecraft'
    url_collection = "http://hubblesite.org/api/v3/images?page=all&collection_name={}".format(name_collection)

    response = requests.get(url_collection)
    response.raise_for_status()
    array_collection = response.json()

    for obj_hubble in array_collection:
        id_image = obj_hubble.get('id')
        url_image = "http://hubblesite.org/api/v3/image/{}".format(id_image)
        response = requests.get(url_image)
        response.raise_for_status()
        array_image = response.json()['image_files']
        best_image = len(array_image)-1
        link_best_image = array_image[best_image]['file_url']
        ext = os.path.splitext(link_best_image)[1]
        link_download = '{}'.format(link_best_image)
        file_name = '{}hubble_{}_{}.{}'.format(path, name_collection, id_image, ext)
        download_image(link_download, file_name)