import requests


def api_convert(convert_to, convert_from, convert_amount):
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={convert_from}&amount={convert_amount}"
  payload = {}
  headers = {
          "apikey": "y75xEY6i5OaCsSLZ3zrni8Lz1kzKcyh1"
      }

  response = requests.request("GET", url, headers=headers, data=payload)

  status_code = response.status_code

  if status_code == 200:
    result = response.json()
    return result['result']
  else:
    return "Api Error"
