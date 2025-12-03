import requests

def upload(url, api_key, path):
    with open(path, 'rb') as f:
        files = {'file': f}

        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.post(f"https://{url}/uploadfile", files=files, headers=headers)

        try:
            response.raise_for_status()

            data = response.json()
            return data['data']['downloadPage']
        except requests.HTTPError:
            print("Status:", response.status_code)
            print("Response text:", response.text)
            return False