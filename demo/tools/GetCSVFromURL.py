import requests

def getCSV(path, name):
    r = requests.get(path, allow_redirects=True)
    destination = '/demo/tools/downloaded/' + name
    open(destination, 'wb').write(r.content)
    return destination


# Test, if it works, you will find the file in the "downloaded" directory.
# For this example, i am using a small .csv file i found on the internet.

#getCSV('https://www.stats.govt.nz/assets/Uploads/Business-price-indexes/Business-price-indexes-September-2020-quarter/Download-data/business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv', 'downloadedCSV.csv')