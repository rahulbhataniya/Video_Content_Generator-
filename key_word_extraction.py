from nltk import tokenize
from operator import itemgetter
import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))

#nltk.download('stopwords')

## 2  Declare Variables
class key_word_find():
        wh_question_word=list()
        answord_word=list()
        ans=list()
        def __init__(self,text_file):
            self.doc=[word.lower() for word in text_file.replace('.',' ').split(' ')]
            self.wh_question_word=['Q','what','when','where','which','who','why','how','explanation','problem','question','solve','find']
            self.answord_word=['solution','answer','ans','following']

        ##  3 Remove stopwords


        ## 4. Find total words in the document 

        #print(tf_idf_score)

        #10. Create a function to get N important words in the document

        def get_exercise_n(self):
            wh_word=set()
            for word in self.doc:
                if word in self.wh_question_word:
                    wh_word.add(word)
            self.ans=list(wh_word)
            return self.ans


 #11. Get the top 5 words of significance
if __name__ == '__main__':
    #get_top_n(tf_idf_score, 20)
    text='''I am from speak english with vanessa vanessa vanessa vanessa vanessa da com.You are so lovely.
    So i get emails from students telling me when i am so glad i canunderstand everything you say.
    Putra night charan in why english tv show and i can understand anything.Does this mean that your speak 
    in floor.Devika question.I whant to make sure the you know exactly the truth.What's the next step when we 
    explain in something like today in the show videos.I want to make sure that you can understand everything.
    Is.Unnatural.I am not talking.Best.Where is mauli.Children.I am not talking mike.But i am talking to really.
    Aloe vera flower because i want to make sure that So i get emails from students telling me when i am so glad i canunderstand everything you say.
    Putra night charan in when english tv show and i can understand anything.Does this mean that your speak 
    in floor.Devika question.I want to make sure the you know exactly the truth.What's the next step when we 
     you can understand.Everything.Turn off the talking to.Hamara  '''
    obj=key_word_find(text)
    final_keyword=obj.get_exercise_n()
    print(final_keyword)

##print(get_top_n(tf_idf_score, 20))