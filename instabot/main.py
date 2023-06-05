import requests

url = "https://youtube-video-download-info.p.rapidapi.com/dl"

def video_yuklab_bering (link):

    querystring = {"id":link}

    headers = {
        "X-RapidAPI-Key": "82d214d06amsh1a8779fec34649ep1ab62fjsn9de378a7509e",
        "X-RapidAPI-Host": "youtube-video-download-info.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()