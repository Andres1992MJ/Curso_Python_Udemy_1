import requests

def handler(pd: "pipedream"):
    r = requests.get('https://swapi.dev/api/')
    # Export the data for use in future steps
    return r.json()