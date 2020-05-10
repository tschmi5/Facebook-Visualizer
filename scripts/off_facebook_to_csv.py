
import json
import csv

off_facebook_file = '../data/facebook/ads_and_businesses/your_off-facebook_activity'

f = open(off_facebook_file + '.json')
raw_json = json.load(f)
places = (raw_json['off_facebook_activity'])
f.close()


with open(off_facebook_file + '.csv','w') as file:
  writer = csv.writer(file)
  writer.writerow(['name','id','type','date'])
  for place in places:
    for event in place['events']:
      writer.writerow([place['name'],event['id'],event['type'],event['timestamp']])
