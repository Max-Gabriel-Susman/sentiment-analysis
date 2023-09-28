import json 

text2Sentiment = dict()
for i in range(1, 124):
    entities = json.load(open('output/review' + str(i) + '.txt.out.json'))

    # json as a dictionary
    # print(entities)
    # print()
    # print(type(entities))

    # create a mapping of text 2 sentiment 

    # for entity in entities:
    #     text2Sentiment[entity['Entities']['Mentions']['Text']] = entity['Entities']['Mentions']['MentionSentiment']['Sentiment']

    pointlessCtr = 0
    for entity in entities['Entities']:
        pointlessCtr += 1
        # print()
        # print(entity['Mentions'][0]['Text'])
        # print(entity['Mentions'][0]['MentionSentiment']['Sentiment'])
        # print()

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
    #print("yaaas")
    # print()
    # print(text2Sentiment)
    # print()



class Entity:
    def __init__(self, name): 
        pass 