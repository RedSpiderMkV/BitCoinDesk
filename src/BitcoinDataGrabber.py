#!/usr/bin/python

import sys
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
		printFormattedPriceData(data)
			
def printCurrentData(dataManager, currency):
	currentPrice = dataManager.GetCurrentData(currency)
	printFormattedPriceData(currentPrice)

def printFormattedPriceData(priceData):
	printData = '{}\t{}\t{}'.format(priceData.Currency, priceData.Price, priceData.Date)
	print printData

def main():
	if len(sys.argv) not in [2, 4]:
		print '\n====BitCoinDataGrabber v0.1a====\n'
		print 'Invalid command\n'
		print 'Historic Data Usage: BitcoinDataGrabber.py <currency> <start> <end>'
		print 'eg: BitcoinDataGrabber.py 2013-01-15 2013-01-31 GBP\n'
		print 'Current Data Usage: BitcoinDataGrabber.py <currency>'
		print 'eg: BitcoinDataGrabber.py GBP\n'
		
		return
		
	currency = sys.argv[1]
	dataManager = CoindeskDataManager()
	
	#printSupportedCurrencies(dataManager)
	
	if len(sys.argv) == 4:	
		startDate = sys.argv[2]
		endDate = sys.argv[3]
		
		printEODData(dataManager, startDate, endDate, currency)
	elif len(sys.argv) == 2:
		printCurrentData(dataManager, currency)
		
if __name__ == '__main__':
	main()
	

