
class Price:
	def __init__(self, currency, price, date):
		'''
		Instantiate a new Price object.
			
			@param currency: currency code
			@param price: price
			@param date: recorded date
		'''
		
		self.Currency = currency
		self.Price = price
		self.Date = date
