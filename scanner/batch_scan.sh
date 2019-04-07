
# @author Yosuke OTSUKI
# @date	2017/03/23
# @license AGPL ver 1
# @description	scanimage command in sane is required
#
# apt-get install sane
#

scanimage \
	--resolution 150 -x 215 -y 297 \
	--format=png \
	--batch-double \
	--batch=scanned-p%d.png 

convert scanned-p*.png scanned.pdf

rm *.png
