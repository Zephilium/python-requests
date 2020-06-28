import requests

url = "https://iti.ac.id"


try:
    response = requests.get(url)
    print(f"Response Code : {response.status_code}")
    print(f"Content : {response.text}")
    print("Sukses")

except Exception as e:
    print(f"Error : {e}")

print("End Program")
