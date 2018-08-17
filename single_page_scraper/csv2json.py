
#
# # Writing JSON data
#
#
# # Reading data back
# with open('./result.json', 'r',encoding="utf-8") as f:
#     data = f.read()
#
# data.replace('"}','"},\n')
#
# with open('./result2.json', 'w') as f2:
#     json.dump(data, f2)
# script for convert csv to json array
# in fact, we don't need it any more
import csv
import json
# utf-8 or ISO-8859-13; try to set encoding when error
csvfile = open('../result_true.csv', 'r',encoding='ISO-8859-13')
jsonfile = open('../result_true_2.json', 'w',encoding='ISO-8859-13')

fieldnames = ("id","claim","rating","image_url","permalink","publish_date","reddit_url")
reader = csv.DictReader(csvfile, fieldnames)

out = json.dumps([ row for row in reader],ensure_ascii=False)
jsonfile.write(out)