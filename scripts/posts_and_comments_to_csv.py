import json
import os
import csv

likes_and_comments_location = '../data/facebook/likes_and_reactions/posts_and_comments'

with open(likes_and_comments_location + '.csv','w') as file:
  writer = csv.writer(file)
  writer.writerow(['actor','recipient','timestamp','reaction'])    
  try:
    f = open(likes_and_comments_location + '.json')
    raw_json = json.load(f)
  
    reactions = (raw_json['reactions'])
    for reaction in reactions:
      try:
        timestamp = reaction['timestamp']
        data = reaction['data'][0]
        actor = data['reaction']['actor']
        action = data['reaction']['reaction']
        title = reaction['title']

        if len(title.split('likes')) > 1:
          recipient = title.split('likes')
          recipient = recipient[1].split('\'s')[0]
          writer.writerow([actor,recipient,action,timestamp])
        elif len(title.split('liked')) > 1:
          recipient = title.split('liked')
          recipient = recipient[1].split('\'s')[0]
          writer.writerow([actor,recipient,action,timestamp])
        elif len(title.split('reacted to')) > 1:
          recipient = title.split('reacted to')[1]
          recipient = recipient.split('\'s')[0]
          writer.writerow([actor,recipient,action,timestamp])
        else:
          print(title)
      except KeyError as e:
        print('KeyError')
    f.close()
  except FileNotFoundError:
    f.close()
    pass




