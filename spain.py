import json 

text2Sentiment = dict()
for i in range(1, 124):
    entities = json.load(open('output/review' + str(i) + '.txt.out.json'))

    pointlessCtr = 0
    # print("length of entities is: " + str(len(entities['Entities'])))
    for entity in entities['Entities']:
        pointlessCtr += 1

        entityName = entity['Mentions'][0]['Text']

        if text2Sentiment.get(entityName) == None:
            sentimentDict = dict({"NEUTRAL": 0, "POSITIVE": 0, "NEGATIVE": 0})
            sentiment = entity['Mentions'][0]['MentionSentiment']['Sentiment']

        if sentiment == "NEUTRAL":
            # print("sentiment is NEUTRAL")
            sentimentDict["NEUTRAL"] += 1
        elif sentiment == "POSITIVE":
            # print("sentiment is POSITIVE")
            sentimentDict["POSITIVE"] += 1
        elif sentiment == "NEGATIVE":
            # print("sentiment is NEGATIVE")
            sentimentDict["NEGATIVE"] += 1
        
        if entityName == "customer service":
            print()
            print(entity['Mentions'][0]['Text'])
            print(entity['Mentions'][0]['MentionSentiment']['Sentiment'])
            print(sentimentDict)
            print()
       
        text2Sentiment[entityName] = sentimentDict