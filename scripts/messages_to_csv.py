import json
import os
import csv

messages_location = '../data/facebook/messages/inbox'

for root,dirs,files in os.walk(messages_location):
  for name in dirs:
    person_path = os.path.join(root,name,'message_1.json')
    f = open(person_path)
    raw_json = json.load(f)
    places = (raw_json['off_facebook_activity'])
    f.close()





# with open(off_facebook_file + '.csv','w') as file:
#   writer = csv.writer(file)
#   writer.writerow(['name','id','type','date'])
#   for place in places:
#     for event in place['events']:
#       writer.writerow([place['name'],event['id'],event['type'],event['timestamp']])
