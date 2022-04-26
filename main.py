import requests
import json
import pandas as pd

def scrape_with_api():
    # get circuit data from ergast API
    response = requests.get("http://ergast.com/api/f1/circuits.json?limit=100").json()

    # parse json and print
    data = json.dumps(response, indent=4, sort_keys=True)
    print(data)

    # get down to correct level of dictionary
    response_clean = response["MRData"]["CircuitTable"]["Circuits"]

    # convert to dataframe
    df = pd.json_normalize(response_clean)

    df.to_csv('f1_circuits.csv')


if __name__ == '__main__':
    scrape_with_api()


