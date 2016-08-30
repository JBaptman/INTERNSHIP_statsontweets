from util import *

#Variable used to store the tweets
data = []


#At the end of this little script, every tweet in the file opened will be in the variable data, as strings
#NB : The CSV file used contains multiple tweets and the text is in the second column of each row

filename = "../data/All tweets (cleaned).csv"
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            tmp = del_all(row[1])
            data.append(tmp)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))




#Uncomment the instructions you want to execute below
print("#######################################################")
nb_words(data)
#nb_wordset(data)
#lexical_diversity(data)
#nb_nouns(data)
#nb_verbs(data)
#nb_namedEntities(data)
