
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

csvfile = open('../result_final_only_image.csv', 'r',encoding='utf-8')
jsonfile = open('../result_final_only_image', 'w',encoding='utf-8')

fieldnames = ("id","claim","rating","image_url","permalink","publish_date")
reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps([ row for row in reader],ensure_ascii=False)
jsonfile.write(out)