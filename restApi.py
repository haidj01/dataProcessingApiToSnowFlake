import requests
import json

def api_request(url: str, params: dict = None):
    try:
        response = requests.get(url=url, params= params)
        response.raise_for_status()  # HTTP 에러 체크
        resp = response.json()
        return resp
    except requests.exceptions.RequestException as e:
        print(f"API 호출 실패: {e}")
        return None