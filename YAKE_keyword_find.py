import yake
def find_key_word(ngram,deb_threshold,data,num_keyword):
    kw_extractor = yake.KeywordExtractor()
    text = data
    language = "en"
    max_ngram_size = ngram
    deduplication_threshold = deb_threshold
    numOfKeywords = num_keyword
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    res=[]
    for kw in keywords:
        res.append(kw[0])
        print(kw)
    return res
    
if __name__=='__main__':
    text="""spaCy is an open-source software library.for advanced natural language processing, written in the programming languages Python and Cython. The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
    find_key_word(3,0.9,text,10)