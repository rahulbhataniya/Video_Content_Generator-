from nltk import tokenize
from operator import itemgetter
import math
import nltk
#nltk.download('stopwords')

## 2  Declare Variables
doc = '''I am from speak english with vanessa da com.You are so lovely.So i get emails from students telling me when i am so glad i canunderstand everything you say.Putra night charan in english tv show and i can understand anything.Does this mean that your speak in floor.Devika question.I want to make sure the you know exactly the truth.What's the next step when we explain in something like today in the show videos.I want to make sure that you can understand everything.Is.Unnatural.I am not talking.Best.Where is mauli.Children.I am not talking mike.But i am talking to really.Aloe vera flower because i want to make sure that you can understand.Everything.Turn off the talking to.Hamara i know the you are watching but on my side i see so it's difficult to help.Natural conversation.When someone is there so the reason why i want it all you get is because i have a lot of videos on my youtube channel with other english speakers.Jesus videos with people skype does videos with people in my house around my city.And i think it's a really good way.English listening to the next level.What is videos.Mossbauer 
explanation.What videos with my voice to overy understand my voice.One other person.How make sure that in the description and at the end of 
this video i will 
link.The sum of those very also the uk.When the next step.Is 2.Tv show another youtube video with someone who is not me someone who you 
don't completely understand already.I think you are greyed out.Studying with fees.Explanation videos.Then watch in.Conversation video 
that i have.Going to someone else.You can touch your skills and grow them step by step.Because my go is.Hey you for the real world kind 
of makeup karen.Who is race in a child and the goal is to send them.And prepare them for the real world.My god is so the you can understand 
anyone can we communicate in any institute.Not just with me.Three step hair.30 basic video.When go to conversation videos with me and then go 
to the conversations with other people.You have.Different style of speaking.We hope you and this is something that i integrate into the course.
Fancy club.Each month we have a conversation with me and another english speaker sometimes to other speakers.How does natural conversation sound.
It usually pretty fast but you already understand my voice.So it can i help you.Increase.Question for you i want to know when you 
study english.The you make me focus on english learning materials.Like this kind of video old do you make me focus on.English tv shows and 
movies.Big continent.Native speaker.I think it is good to start with more basic.Remove the smart challenging things but i want to know for 
you.What do you memory enjoy.As you study in english.What is now in the comments below and i cant wait to see what you have this day i think 
so much and also to the next time by the next step is to download my free ebook.5 steps to become an accountant in english speaker i want to 
help you master english in speak fluently you are free to subscribe to the eedomus new english lesson.Thanks so much for money with me by.'''

##  3 Remove stopwords

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

## 4. Find total words in the document 

total_words = doc.split()
total_word_length = len(total_words)
print(total_word_length)

##5 5. Find the total number of sentences
total_sentences = tokenize.sent_tokenize(doc)
total_sent_len = len(total_sentences)
print(total_sent_len)

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
print(tf_score)

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

print(idf_score)

##9. Calculate TF * IDF

tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
print(tf_idf_score)

#10. Create a function to get N important words in the document

print('..........................important word................')
def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n]) 
    return result

 #11. Get the top 5 words of significance

print(get_top_n(tf_idf_score, 20))