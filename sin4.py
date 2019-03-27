#simple quant shit
import random
import time

def main():
	# Growing list of share prices, including current
	priceHistory = [50]

	# Current bank balance and amount of shares held
	balance = 450
	shareHeld = 0

	for a in range(20):

		sharePrice = priceHistory[-1] + random.randint(-15, 16)

		# Ensure stock can't be negatively priced
		if sharePrice < 0: sharePrice = 0
		
		priceHistory.append(sharePrice)

		# With this modular setup, we can define many different 'buyer functions'
		# that can have their own logic for choosing when and how much to buy/sell
		(quantity, price) = naiveBuyer(balance, shareHeld, priceHistory)

		total = quantity * price

		# Sanity checks
		if (balance - total < 0):
			print ('Error: AI tried to buy more than we can afford. Skipping forward...')
			continue

		if (price < 0):
			print ('Error: AI return negative price value. Skipping forward...')
			continue

		balance -= total
		shareHeld += quantity

		print ('current share price: ' + str(sharePrice))

		if total > 0:
			print ('\nBOUGHT ' + str(quantity) + ' for ' + str(price) + ' each')
			print ('current balance: ' + str(balance) + '\n')
		elif total < 0:
			print ('\nSOLD ' + str(-quantity) + ' for ' + str(price) + ' each')
			print ('current balance: ' + str(balance) + '\n')

		time.sleep(0.5)

	print ('\nfinal balance: ' + str(balance))


# Keeps track of the price of the last share purchased
buyPrice = 0

# Takes in the current share price and returns a tuple
# with the amount of shares to buy and at what price.
# Will buy if positive, sell if negative, and wait if 0.
def naiveBuyer(balance, shareHeld, priceHistory):

	global buyPrice

	oldSharePrice = priceHistory[-2]
	currentSharePrice = priceHistory[-1]

	if (currentSharePrice - oldSharePrice) > (0.1 * oldSharePrice) and (balance - currentSharePrice) >= 0 and shareHeld == 0:
		# Buy a single share at market value
		buyPrice = currentSharePrice
		return (1, currentSharePrice)
	
	if currentSharePrice > (1.1 * buyPrice) and shareHeld > 0:
		# Sell a single share at market value
		return (-1, currentSharePrice)
	
	# Do nothing
	return (0, 0)


if __name__ == "__main__":
	main()