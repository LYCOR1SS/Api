
import requests

def video_yuklab_ber(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
    "X-RapidAPI-Key": "01832907ddmshc1d27e9e8bcaccap1de55fjsn1b119adcbf25",
    "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
        }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()['media']





