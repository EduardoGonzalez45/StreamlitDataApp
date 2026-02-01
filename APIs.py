import requests

# For picture of the day API to deliver what is needed.
def apod_generator(url, unique_key, chosen_date):
    final_url = url + unique_key + "&date=" + chosen_date
    response = requests.get(final_url).json()
    return response

# For picture of the day API to deliver 30 days worth of APOD data.
def apod_generator_list(url, unique_key, start_date, end_date):
    final_url = url + unique_key + "&start_date=" + start_date + "&end_date=" + end_date
    response = requests.get(final_url).json()
    return response