
from CoindeskApi.CoindeskApi import CoindeskDataManager
from CoindeskApi.Currency import Currency

def printSupportedCurrencies():
	dataManager = CoindeskDataManager()
	currencies = dataManager.GetSupportedCurrencies()
	
	for currencyData in currencies:
		print currencyData.Code, currencyData.Description
	
def printEODData(startDate, endDate, currency):
	dataManager = CoindeskDataManager()
	eodData = dataManager.GetEndOfDayData(startDate, endDate, currency)
	
	for data in eodData:
		print data, eodData[data]
			
if __name__ == '__main__':
	printSupportedCurrencies()
	#printEODData('2017-05-01', '2017-05-26', 'GBP')
