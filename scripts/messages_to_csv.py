import json
import os
import csv

messages_location = '../data/facebook/messages/inbox'

with open(messages_location + '/../messages_flat.csv','w') as file:
  writer = csv.writer(file)
  writer.writerow(['title','sender_name','timestamp_ms','content','type'])
  for root,dirs,files in os.walk(messages_location):
    for name in dirs:
      person_path = os.path.join(root,name,'message_1.json')
      try:
        f = open(person_path)
        raw_json = json.load(f)
      
        messages = (raw_json['messages'])
        title = raw_json['title']
        for message in messages:
          try:
            writer.writerow([title,message['sender_name'],message['timestamp_ms'],message['content'],message['type']])
          except KeyError:
            pass
        f.close()
      except FileNotFoundError:
        f.close()
        pass




