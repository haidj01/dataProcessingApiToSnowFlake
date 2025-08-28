import requests
import json

def api_request():
    try:
        response = requests.get('https://fake-json-api.mock.beeceptor.com/users')
        response.raise_for_status()  # HTTP 에러 체크
        users = response.json()
        print(f"사용자 {len(users)}명 조회됨")
        return users
    except requests.exceptions.RequestException as e:
        print(f"API 호출 실패: {e}")
        return None