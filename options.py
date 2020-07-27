import sys

def call(strike, premium, current, lot, buy=True):
	breakeven = strike + premium
	if buy:
		max_loss = (0 - premium*lot)
		cash_return = (current - breakeven) * lot
		if cash_return <= max_loss:
			cash_return = max_loss
		return cash_return
	else:
		if current <= strike:
			return premium*lot
		else:
			cash_return = (breakeven - current) * lot
			return cash_return

def put(strike, premium, current, lot, buy=True):
	breakeven = strike - premium
	if buy:
		max_loss = (0 - premium*lot)
		cash_return = (breakeven - current) * lot
		if cash_return <= max_loss:
			cash_return = max_loss
		return cash_return
	else:
		if current >= strike:
			return premium*lot
		else:
			cash_return = (current - breakeven) * lot
			return cash_return

if __name__ == '__main__':
	args = sys.argv[1:]
	trade = args[0]
	args = [int(i) for i in args[1:]]
	if trade == 'call':
		profit = call(args[0], args[1], args[2], args[3], buy=args[4])
	elif trade == 'put':
		profit = put(args[0], args[1], args[2], args[3], buy=args[4])
	print(profit)