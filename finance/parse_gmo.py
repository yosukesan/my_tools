
def gmo(file_name):
	import pandas as pd
	import numpy as np

	data = pd.read_csv(file_name, usecols=["約定日時", "銘柄名", "売買区分", "約定単価", "約定数量", "手数料", "手数料消費税", "受渡金額（円貨）"])
	tics = set(data["銘柄名"])

	for tic in tics:

		tic_data = data[data["銘柄名"] == tic]
		tic_buy = tic_data[tic_data["売買区分"] == "買"]
		tic_sell = tic_data[tic_data["売買区分"] == "売"]

		amount_buy = sum(tic_buy["約定数量"])
		amount_sell = sum(tic_sell["約定数量"])
		ave_buy = np.mean(tic_buy["約定単価"])
		#ave_sell = average(tic_sell["約定単価"])
		left_over = amount_buy - amount_sell
		
		print("\n=======================================")
		print("銘柄名=", tic)
		print("---------------------------------------")
		print(tic_data)
		print("---------------------------------------")
		print("次年度へ繰越数量=", left_over, \
				"取得時平均約定単価=", ave_buy, \
				"手数料合計=", sum(tic_data["手数料"]), \
				"手数料消費税合計=", sum(tic_data["手数料消費税"]), \
				"受渡金額=", sum(tic_data["受渡金額（円貨）"]))

if __name__ == "__main__":
	gmo("./data/2017.csv")
	#gmo("./data/2018.csv")
