import json 

text2Sentiment = dict()
for i in range(1, 124):
    entities = json.load(open('output/review' + str(i) + '.txt.out.json'))
    print(entities)
print("INTERMISSION")
print(entities)

for entity in entities['Entities']:
    
    entityName = entity['Mentions'][0]['Text']

    if text2Sentiment.get(entityName) == None:
        sentimentDict = dict({"NEUTRAL": 0, "POSITIVE": 0, "NEGATIVE": 0})
        sentiment = entity['Mentions'][0]['MentionSentiment']['Sentiment']

    if sentiment == "NEUTRAL":
        sentimentDict["NEUTRAL"] += 1
    elif sentiment == "POSITIVE":
        sentimentDict["POSITIVE"] += 1
    elif sentiment == "NEGATIVE":
        sentimentDict["NEGATIVE"] += 1
    
    #print(entity['Mentions'][0]['Text'])
    if entityName == "customer service":
        print()
        print(entity['Mentions'][0]['Text'])
        print(entity['Mentions'][0]['MentionSentiment']['Sentiment'])
        print(sentimentDict)
        print()
    
    text2Sentiment[entityName] = sentimentDict

print(text2Sentiment)   