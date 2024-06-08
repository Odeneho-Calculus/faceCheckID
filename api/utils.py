#API TOKEN : oIitEgME/Xby42/E69De8AWr6A+Tobjb//7fYnyld/CBMCJ4HOn+12/7irSYDOUF4ZUD42NyjRc=



import time
import requests
from bs4 import BeautifulSoup

APITOKEN = 'oIitEgME/Xby42/E69De8AWr6A+Tobjb//7fYnyld/CBMCJ4HOn+12/7irSYDOUF4ZUD42NyjRc='  # Replace with your actual API token
TESTING_MODE = True

def search_by_face(image_file):
    if TESTING_MODE:
        print('****** TESTING MODE search, results are inaccurate, and queue wait is long, but credits are NOT deducted ******')

    site = 'https://facecheck.id'
    headers = {'accept': 'application/json', 'Authorization': APITOKEN}
    files = {'images': open(image_file, 'rb'), 'id_search': None}
    response = requests.post(site + '/api/upload_pic', headers=headers, files=files).json()

    if response['error']:
        return f"{response['error']} ({response['code']})", None

    id_search = response['id_search']
    print(response['message'] + ' id_search=' + id_search)
    json_data = {'id_search': id_search, 'with_progress': True, 'status_only': False, 'demo': TESTING_MODE}

    while True:
        response = requests.post(site + '/api/search', headers=headers, json=json_data).json()
        if response['error']:
            return f"{response['error']} ({response['code']})", None
        if response['output']:
            return None, response['output']['items']
        print(f'{response["message"]} progress: {response["progress"]}%')
        time.sleep(1)

def extract_image_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    image_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
    return image_urls
