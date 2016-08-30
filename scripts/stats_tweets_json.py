from util import *

#Variables used to store the tweets
data = []
data_ios = []
data_android = []
data_else = []


#At the end of this little script, every tweet in the file opened will be in the variable data, as strings
#Also, the tweets from iOS devices will be in data_ios, the tweets from Android devices will be in data_android, and the others (web, other devices, etc.) will be in data_else
#NB : The JSON file contains multiple JSON objects, but not contained in an array


#We open the JSON file that contains the tweets 
with open('../data/data_en.json',encoding='utf-8') as f:
    for line in f:
        
        if(line != '\n'):
            obj = json.loads(line)

            #For every JSON object, we take the text and remove the "automatic tweets" from Youtube + punctuation, hashtag, URLs, and mentions
            if (('text' in list(obj.keys())) and ('source' in list(obj.keys()))):
                tmp = obj["text"]
                
                if find_YTTweets(tmp):
                    tmp2 = del_all(tmp)
                    data.append(tmp2)
                    
                    if 'Twitter for iPhone' in obj["source"]:
                        data_ios.append(tmp2)
                        
                    elif 'Twitter for Android' in obj["source"]:
                        data_android.append(tmp2)
                        
                    else:
                        data_else.append(tmp2)




#Uncomment the instructions you want to execute below
print("#######################################################")
nb_chars(data_ios)
#nb_words(data_ios)
#nb_wordset(data)
#lexical_diversity(data)
#nb_nouns(data)
nb_verbs(data)
#nb_namedEntities(data_ios)
most_common_words(data_ios,20)

