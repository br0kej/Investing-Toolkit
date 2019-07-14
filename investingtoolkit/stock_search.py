import requests
from investingtoolkit import utils

def search_equity(apikey):
    """Uses the Alpha Vantage API to search for
    a Stock Symbol based the user's keyword input"""

    # User input keyword to perform search
    search = input('Stock Search Keyword: ')
    # Send Request to Alpha Vantage Search API
    search_response = requests.get(
        'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + search + '&apikey=' + apikey + '&datatype=json')
    request_validation = utils.check_response_status(search_response)

    if request_validation is True:
        # Conversion of response to a JSON object.
        json = search_response.json()
        # Loop through results, assign index key and print results
        if not json['bestMatches']:
            print("[-] No Results Found for search :" + search)
        else:
            print('[+] Printing results for search: ' + search + '\n')
            for idx, item in enumerate(json['bestMatches']):
                if item['3. type'] == "Equity" and float(item['9. matchScore']) > 0.4:
                    print('Name: {}  Symbol: {}  Type: {}'.format(
                        item['2. name'],
                        item['1. symbol'],
                        item['3. type']
                    ))
    else:
        print('[-] Request failed. Unable to find results for ' + search)