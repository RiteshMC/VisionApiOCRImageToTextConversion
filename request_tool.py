import json

import requests


def get_processed_data_with_url(api_key, image_url):
    url = "https://vision.googleapis.com/v1/images:annotate?key={}".format(api_key)
    payload = json.dumps({
        "requests": [
            {
                "image": {
                    "source": {
                        "imageUri": image_url
                    }
                },
                "features": [
                    {
                        "type": "DOCUMENT_TEXT_DETECTION"
                    }
                ]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)


def get_processed_data_with_base64img(api_key, base64data):
    url = "https://vision.googleapis.com/v1/images:annotate?key={}".format(api_key)
    payload = json.dumps({
        "requests": [
            {
                "image": {
                    "content": base64data
                },
                "features": [
                    {
                        "maxResults": 50,
                        "type": "DOCUMENT_TEXT_DETECTION"
                    }
                ]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)
