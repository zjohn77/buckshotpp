
# coding: utf-8

# In[1]:

from numpy.random import choice
from pandas import read_csv, DataFrame
from sklearn.cluster import KMeans
import os
import sys
sys.path.insert(0, 'C:/Users/jjung/Documents/GitHub//bkmark_organizer/test_parser_stemmer/prototype/TxtClus/')
from nlp.termWeighting import doc_term_matrix
from EstimateK.seqFit import sensitiv


# In[2]:

class Clusterings(object):
    '''Define class for .'''
    def __init__(self, param_dict):
        self.__param_dict = param_dict        
    
    def get_file(self):
        '''read csv input into a pandas data frame'''
        return read_csv(self.__param_dict['file_loc'], encoding = 'latin1')

    def term_weight_matr(self, snippetsArr):
        '''compute a document-term matrix based on a collection of text documents'''
        return doc_term_matrix(snippetsArr, self.__param_dict)


# In[4]:

if __name__ == "__main__":
    news_file = sys.path[0] + 'Input/newsSample.csv'    
    # Run 1:
    vecSpaceModel1 = Clusterings({'run': 1,
                                  'file_loc': news_file,
                                  'samp_size': 50,
                                  'tf_dampen': True,
                                  'common_word_pct': 1,
                                  'rare_word_pct': 1,
                                  'dim_redu': False})
    headlines = vecSpaceModel1.get_file().TITLE
    term_weight_obj = vecSpaceModel1.term_weight_matr(headlines)
    X1 = term_weight_obj['docTerm_X'].toarray()
    sensitiv(X1)    


# In[9]:

df = DataFrame({'predictedCluster': KMeans(17).fit(X1).labels_, 
                'document': term_weight_obj['samp']}).sort_values(by='predictedCluster')

print(df)

