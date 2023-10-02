
text2Sentiment = dict()
for i in range(1, 10):
    

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

        # mock entities
        entityMocks = dict({"a": 0, "b": 0, "c": 0, "d"})

        # mock aggregation 
        if sentiment == "NEUTRAL":
            sentimentDict["NEUTRAL"] += 1
        elif sentiment == "POSITIVE":
            sentimentDict["POSITIVE"] += 1
        elif sentiment == "NEGATIVE":
            sentimentDict["NEGATIVE"] += 1
        elif sentiment == "MIXED":
            sentimentDict["NEUTRAL"] += 1
        elif sentiment == "MIXED":
            sentimentDict["NEUTRAL"] += 1
        
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

