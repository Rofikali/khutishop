import requests

url = "http://127.0.0.1:8000/api/porducts/"
params = {"limit": 3}
all_results = []

r = requests.get(url, params=params, auth=("admin", "admin"))
data = r.json()['results'][0]['name']
print(data)
# all_results


# while url:
#     r = requests.get(url, params=params)
#     data = r.json()
#     print(data)
#     # all_results.extend(data.get("results", []))

# # Get the next page URL
# url = data.get("next")
# params = {}  # Clear params since 'next' already contains them

# Print or process all results
# for item in all_results:
#     print(item)
