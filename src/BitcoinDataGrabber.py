
import json
import urllib2

apiCurrencyList = 'http://api.coindesk.com/v1/bpi/supported-currencies.json'
apiCurrentPrice = 'http://api.coindesk.com/v1/bpi/currentprice.json'
apiCurrentPriceCode = 'http://api.coindesk.com/v1/bpi/currentprice/{}.json'
apiEODPrice = 'http://api.coindesk.com/v1/bpi/historical/close.json?start={}&end={}&currency={}' # yyyy-mm-dd

def GetApiJsonResponse(url):
	response = urllib2.urlopen(url)
	data = json.load(response)
	return data

def GetApiRawResponse(url):
	response = urllib2.urlopen(url)
	data = response.read()
	return data

def printSupportedCurrencies():
	jsonData = GetApiJsonResponse(apiCurrencyList)
	indexSymbol = 'currency'
	indexCurrency = 'country'
	for data in jsonData:
		dataStr = ''
		try:
			dataStr = '{}\t{}'.format(data[indexSymbol], data[indexCurrency])
		except Exception, e:
			dataStr = '{}\t{}'.format(data[indexSymbol], '')
			
		print dataStr
	
def printEODData(startDate, endDate, currency):
	jsonData = GetApiJsonResponse(apiEODPrice.format(startDate, endDate, currency))
	eodData = jsonData['bpi']
	
	for data in eodData:
		print data, eodData[data]
			
if __name__ == '__main__':
	#printSupportedCurrencies(jsonData)
	printEODData('2017-05-01', '2017-05-26', 'GBP')
