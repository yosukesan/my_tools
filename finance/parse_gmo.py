
class Result:

	def __init__(self):
		self._fee = 0.0
		self._tax = 0.0
		self._sum = 0.0

	def update(self, fee, tax, sum):
		self._fee += fee
		self._tax += tax
		self._sum += sum

	def fee(self):
		return self._fee
	
	def tax(self):
		return self._tax

	def sum(self):
		return self._sum

class ETF:

	def __init__(self):
		self._rate = {
			"楽天ＥＴＦ‐日経ダブルインバース指数連動型": 0.35,
			"楽天ＥＴＦ‐日経レバレッジ指数連動型": 0.35,
			"日経２２５連動型上場投資信託": 0.35,
			#{"ＮＥＸＴ　ＦＵＮＤＳ　日経平均ダブルインバース・インデックス": 0.35},
			#{"特殊電極": 0.35},
			#{"ＷＴＩ原油価格連動型上場投信": 0.35},
			#{"ダイワ上場投信−日経平均ダブルインバース・インデックス": 0.35},
			#{"ＮＥＸＴ　ＦＵＮＤＳ日経平均インバース・インデックス連動型": 0.35},
			#{"ＮＥＸＴ　ＦＵＮＤＳ日経平均レバレッジ・インデックス連動型": 0.35},
			#{"純プラチナ上場信託（現物国内保管型）": 0.35},
			"ＮＥＸＴＦＵＮＤＳ東証ＲＥＩＴ指数連動型上場投資信託": 0.32,
			"上場インデックスファンドＭＳＣＩ日本株高配当低ボラティリティ": 0.27,
			"上場インデックスファンド新興国債券": 0.486,
			"上場インデックスファンド海外債券（ＦＴＳＥ　ＷＧＢＩ）毎月分": 0.27,
			"上場インデックスファンド米国債券（為替ヘッジなし）": 0.1728}

	def rate(self, tic):
		return self._rate[tic]

def gmo(file_name):
	import pandas as pd
	import numpy as np
	import datetime
	import itertools

	etf = ETF()

	pd.set_option("display.max_columns", 1000)
	pd.set_option("display.width", 1000)
	pd.set_option("display.max_rows", 1000)
	data = pd.read_csv(file_name, usecols=["約定日時", "銘柄名", "売買区分", "約定単価", "約定数量", "手数料", "手数料消費税", "受渡金額（円貨）"])
	tics = set(data["銘柄名"])

	result = Result()

	for tic in tics:

		tic_data = data[data["銘柄名"] == tic]
		tic_buy = tic_data[tic_data["売買区分"] == "買"]
		tic_sell = tic_data[tic_data["売買区分"] == "売"]

		#historical = tic_data["約定日時"]
		#for d in zip(historical[1:], historical[:-1]):
		#	forward = datetime.datetime.strptime(d[0], '%Y/%m/%d %H:%M:%S') 
		#	after = datetime.datetime.strptime(d[1], '%Y/%m/%d %H:%M:%S') 
		#	days = (forward - after).days

		#	if days != 0:
		#		etf.rate(tic) / days
		#	else:
		#		print(0)

		amount_buy = sum(tic_buy["約定数量"])
		amount_sell = sum(tic_sell["約定数量"])
		ave_buy = np.mean(tic_buy["約定単価"])
		#ave_sell = average(tic_sell["約定単価"])
		left_over = amount_buy - amount_sell

		tic_fee	= sum(tic_data["手数料"])
		tic_tax = sum(tic_data["手数料消費税"])
		tic_sum = sum(tic_data["受渡金額（円貨）"])

		result.update(tic_fee, tic_tax, tic_sum)
	
		print("\n============================================================")
		print("銘柄名=", tic)
		print("-----------------------------------------------------------")
		print(tic_data)
		print("-----------------------------------------------------------")
		print("次年度へ繰越数量=",		left_over, \
				"取得時平均約定単価=",	ave_buy, \
				"手数料合計=",			tic_fee, \
				"手数料消費税合計=",	tic_tax, \
				"信託報酬=",			0,\
				"受渡金額=",			tic_sum)
		print("\n\n")

	print("\n============================================================")
	print("年度末合計")
	print("手数料=", result.fee(), "手数料消費税=", result.tax(), "損益総計=",result.sum())
	print("============================================================")

if __name__ == "__main__":
	#gmo("./data/2017.csv")
	gmo("./data/2018.csv")
