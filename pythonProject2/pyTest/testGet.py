import requests

if __name__ == '__main__':
    #r = requests.get("https://github.com/SimplifyJobs/New-Grad-Positions?tab=readme-ov-file")
    #print(r.status_code)
    data = {
        "text":"hello"
    }
    r = requests.post(url = "https://dict.youdao.com/keyword/key",data=data)
    print(r.json())

def test_youdou():
    data = {
        "text": "hello"
    }
    r = requests.post(url="https://dict.youdao.com/keyword/key", data=data)
    result = r.json()
    print(result["message"])
    assert result["message"]=="SUCCESS"