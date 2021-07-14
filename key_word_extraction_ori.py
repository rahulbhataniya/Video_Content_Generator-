from nltk import tokenize
from operator import itemgetter
import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

#nltk.download('stopwords')

## 2  Declare Variables
doc = '''I am from speak english with vanessa da com.You are so lovely.So i get emails from students telling me when i am so glad i canunderstand everything you say.Putra night charan in english tv show and i can understand anything.Does this mean that your speak in floor.Devika question.I want to make sure the you know exactly the truth.What's the next step when we explain in something like today in the show videos.I want to make sure that you can understand everything.Is.Unnatural.I am not talking.Best.Where is mauli.Children.I am not talking mike.But i am talking to really.Aloe vera flower because i want to make sure that you can understand.Everything.Turn off the talking to.Hamara i know the you are watching but on my side i see so it's difficult to help.Natural conversation.When someone is there so the reason why i want it all you get is because i have a lot of videos on my youtube channel with other english speakers.Jesus videos with people skype does videos with people in my house around my city.And i think it's a really good way.English listening to the next level.What is videos.Mossbauer 
        explanation.What videos with my voice to overy understand my voice.One other person.How make sure that in the description and at the end of 
        this video i will 
        '''

##  3 Remove stopwords


## 4. Find total words in the document 

total_words = doc.split()
total_word_length = len(total_words)
#print(total_word_length)

##5 5. Find the total number of sentences
total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)
#print(total_sent_len)

##6. Calculate TF for each word

tf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1

# Dividing by total_word_length for each dictionary element
tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
#print(tf_score)

##7. Function to check if the word is present in a sentence list

def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

##8 8. Calculate IDF for each word

idf_score = {}
for each_word in total_words:
    each_word = each_word.replace('.','')
    if each_word not in stop_words:
        if each_word in idf_score:
            idf_score[each_word] = check_sent(each_word, total_sentences)
        else:
            idf_score[each_word] = 1

# Performing a log and divide
idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

#print(idf_score)

##9. Calculate TF * IDF

tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
#print(tf_idf_score)

#10. Create a function to get N important words in the document

print('..........................important word................')
def get_top_n(dict_elem, n):
    sorted_result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    ##################################################################
    # sorted_result onctaone bot word and correspondin frequency      #
    ###################################################################
    keywords=[key for key in sorted_result.keys()]
    return keywords

 #11. Get the top 5 words of significance
if __name__ == '__main__':
    get_top_n(tf_idf_score, 20)
print(get_top_n(tf_idf_score, 20))