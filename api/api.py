import requests
import logging
import pandas as pd


URL = "https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog"
STATUS_OK = 200
OUTPUT_FILE = "api.xlsx"

def main():
    response = requests.get(URL)
    status_code = response.status_code

    logging.basicConfig(level=logging.INFO)
    logging.info("status_code: %s" % status_code)

    if status_code == STATUS_OK:
        api_data = response.json()
        df = pd.DataFrame.from_dict(api_data)
        df.to_excel(OUTPUT_FILE)
        logging.info("File created successfully")
    else:
        logging.error("Invalid response received")

    return

if __name__ == '__main__':
    main()
