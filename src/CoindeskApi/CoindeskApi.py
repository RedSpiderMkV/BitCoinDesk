
import json
import urllib2
from datetime import datetime
from Currency import Currency
from Price import Price

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
		
		url = self._apiEODPrice.format(startDate, endDate, currency)
		
		jsonData = self._getApiJsonResponse(url)
		eodData = jsonData['bpi']
		
		dataCollection = []
		for eodDate in eodData:
			dataCollection.append(Price(currency, eodDate, eodData[eodDate]))
		
		return dataCollection

	def GetCurrentData(self, currency):
		'''
		Get the current data from the API.
		
			@param currency: currency code of interest
			@returns: current bitcoin price data as a Price object.
		'''
		
		url = self._apiCurrentPriceCode.format(currency)
		
		jsonData = self._getApiJsonResponse(url)
		price = jsonData['bpi'][currency]['rate_float']
		date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
		
		currentData = Price(currency, price, date)
		return currentData

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
