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
        def __init__(self,text_file):
            self.doc=text_file
        ##  3 Remove stopwords


        ## 4. Find total words in the document 
        def TF__IDF(self):
            self.total_words = self.doc.split()
            self.total_word_length = len(self.total_words)
            #print(total_word_length)

            ##5 5. Find the total number of sentences
            self.total_sentences = tokenize.sent_tokenize(self.doc)
            self.total_sent_len = len(self.total_sentences)
            #print(total_sent_len)

            ##6. Calculate TF for each word

            self.tf_score = {}
            for each_word in self.total_words:
                each_word = each_word.replace('.','')
                if each_word.lower() not in stop_words:
                    if each_word in self.tf_score:
                        self.tf_score[each_word] += 1
                    else:
                        self.tf_score[each_word] = 1

            # Dividing by total_word_length for each dictionary element
            self.tf_score.update((x, y/int(self.total_word_length)) for x, y in self.tf_score.items())
            ##8 8. Calculate IDF for each word

            self.idf_score = {}
            for each_word in self.total_words:
                each_word = each_word.replace('.','')
                if each_word.lower() not in stop_words:
                    if each_word in self.idf_score:
                        self.idf_score[each_word] = self.check_sent(each_word, self.total_sentences)
                    else:
                        self.idf_score[each_word] = 1

            # Performing a log and divide
            self.idf_score.update((x, math.log(int(self.total_sent_len)/y)) for x, y in self.idf_score.items())

            #print(idf_score)

            ##9. Calculate TF * IDF

            self.tf_idf_score = {key: self.tf_score[key] * self.idf_score.get(key, 0) for key in self.tf_score.keys()}

        ##7. Function to check if the word is present in a sentence list

        def check_sent(self,word, sentences): 
            self.final = [all([w in x for w in word]) for x in sentences] 
            self.sent_len = [sentences[i] for i in range(0, len(self.final)) if self.final[i]]
            return int(len(self.sent_len))
        

        

        
        #print(tf_idf_score)

        #10. Create a function to get N important words in the document

        def get_top_n(self,n):
            self.TF__IDF()
            self.sorted_result = dict(sorted(self.tf_idf_score.items(), key = itemgetter(1), reverse = True)[:n]) 
            ##################################################################
            # sorted_result onctaone bot word and correspondin frequency      #
            ###################################################################
            self.keywords=[key for key in self.sorted_result.keys()]
            return self.keywords

 #11. Get the top 5 words of significance
if __name__ == '__main__':
    #get_top_n(tf_idf_score, 20)
    text='''I am from speak english with vanessa da com.You are so lovely.
    So i get emails from students telling me when i am so glad i canunderstand everything you say.
    Putra night charan in english tv show and i can understand anything.Does this mean that your speak 
    in floor.Devika question.I want to make sure the you know exactly the truth.What's the next step when we 
    explain in something like today in the show videos.I want to make sure that you can understand everything.
    Is.Unnatural.I am not talking.Best.Where is mauli.Children.I am not talking mike.But i am talking to really.
    Aloe vera flower because i want to make sure that So i get emails from students telling me when i am so glad i canunderstand everything you say.
    Putra night charan in english tv show and i can understand anything.Does this mean that your speak 
    in floor.Devika question.I want to make sure the you know exactly the truth.What's the next step when we 
     you can understand.Everything.Turn off the talking to.Hamara  '''
    obj=key_word_find(text)
    final_keyword=obj.get_top_n(20)
    print(final_keyword)

##print(get_top_n(tf_idf_score, 20))