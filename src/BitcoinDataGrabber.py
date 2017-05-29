
import json
import urllib2

apiCurrencyList = 'http://api.coindesk.com/v1/bpi/supported-currencies.json'
apiCurrentPrice = 'http://api.coindesk.com/v1/bpi/currentprice.json'

def GetApiJsonResponse(url):
	response = urllib2.urlopen(url)
	
	data = json.load(response)
	return data

jsonData = GetApiJsonResponse(apiCurrencyList)

def printSupportedCurrencies():
	indexSymbol = 'currency'
	indexCurrency = 'country'
	for data in jsonData:
		try:
			dataStr = '{}\t{}'.format(data[indexSymbol], data[indexCurrency])
			print dataStr
		except Exception, e:
			print data
			
if __name__ == '__main__':
	printSupportedCurrencies()
