import json 

entities = json.load(open('a-targeted-sentiment.json'))

# json as a dictionary
print(entities)
print()
print(type(entities))

# create a mapping of text 2 sentiment 
text2Sentiment = dict()

# for entity in entities:
#     text2Sentiment[entity['Entities']['Mentions']['Text']] = entity['Entities']['Mentions']['MentionSentiment']['Sentiment']

for entity in entities['Entities']:
    # print()
    # print(entity['Mentions'][0]['Text'])
    # print(entity['Mentions'][0]['MentionSentiment']['Sentiment'])
    # print()
    text2Sentiment[entity['Mentions'][0]['Text']] = entity['Mentions'][0]['MentionSentiment']['Sentiment']

print(text2Sentiment)