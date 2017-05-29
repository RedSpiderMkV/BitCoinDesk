
import json
import urllib2
from Currency import Currency

class CoindeskDataManager:
	'''
	CoindeskDataManager - handles requests and responses from the Coindesk API.
	'''
	
	def __init__(self):
		'''
		Initialise new data manager.
		'''
		
		self._apiCurrencyList = 'http://api.coindesk.com/v1/bpi/supported-currencies.json'
		self._apiCurrentPrice = 'http://api.coindesk.com/v1/bpi/currentprice.json'
		self._apiCurrentPriceCode = 'http://api.coindesk.com/v1/bpi/currentprice/{}.json'
		self._apiEODPrice = 'http://api.coindesk.com/v1/bpi/historical/close.json?start={}&end={}&currency={}' # yyyy-mm-dd

	def GetEndOfDayData(self, startDate, endDate, currency):
		'''
		Get end of day data.
		
			@param startDate: start date of data collection, format: yyyy-mm-dd
			@param endDate: end date of data collection, format: yyyy-mm-dd
			@param currency: currency code
			@returns: dictionary of date and data objects
		'''
		
		jsonData = self._getApiJsonResponse(self._apiEODPrice.format(startDate, endDate, currency))
		return jsonData['bpi']

	def GetSupportedCurrencies(self):
		'''
		Get the supported API currencies.
		
			@returns: Collection of Currency objects containing currency code and description
		'''
		
		jsonData = self._getApiJsonResponse(self._apiCurrencyList)
		
		indexSymbol = 'currency'
		indexDescription = 'country'
		
		currencyCollection = []
		
		for data in jsonData:
			currencyData = ''
			try:
				currencyData = Currency(data[indexSymbol], data[indexDescription])
			except Exception:
				currencyData = Currency(data[indexSymbol], '')
				
			currencyCollection.append(currencyData)
			
		return currencyCollection

	def _getApiJsonResponse(self, url):
		'''
		Get the response from the provided url as a json object.
		
			@param url: api endpoint
			@returns: json data from endpoint
		'''
		
		response = urllib2.urlopen(url)
		data = json.load(response)
		return data
