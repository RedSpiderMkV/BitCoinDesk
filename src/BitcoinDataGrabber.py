
from CoindeskApi.CoindeskApi import CoindeskDataManager
from CoindeskApi.Currency import Currency
from CoindeskApi.Price import Price

def printSupportedCurrencies(dataManager):
	currencies = dataManager.GetSupportedCurrencies()
	
	for currencyData in currencies:
		print currencyData.Code, currencyData.Description
	
def printEODData(dataManager, startDate, endDate, currency):
	eodData = dataManager.GetEndOfDayData(startDate, endDate, currency)
	
	for data in eodData:
		printFormattedPriceData(priceData)
			
def printCurrentData(dataManager, currency):
	currentPrice = dataManager.GetCurrentData(currency)
	printFormattedPriceData(priceData)

def printFormattedPriceData(priceData):
	printData = '{}\t{}\t{}'.format(priceData.Currency, priceData.Price, priceData.Date)
	print printData

if __name__ == '__main__':
	dataManager = CoindeskDataManager()
	#printSupportedCurrencies(dataManager)
	#printEODData(dataManager, '2017-05-01', '2017-05-26', 'GBP')
	printCurrentData(dataManager, 'GBP')
