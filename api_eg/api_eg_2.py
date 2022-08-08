#https://developer.nrel.gov
#https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=gVl6k04aFcnQ0PU5oiTf2a6ZUKYNANwc8Ogr5bcb
import requests
res=requests.get("https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=gVl6k04aFcnQ0PU5oiTf2a6ZUKYNANwc8Ogr5bcb")
print(res.status_code)
print(res.text)
print(res.json())
print(list(res.json()))