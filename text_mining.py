# -*- coding: utf-8 -*-
"""
__author__ = "Ahirton Lopes & Rodrigo Pasti"
__copyright__ = "Copyright 2015/2016/2017, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirtonlopes@gmail.com"
__status__ = "Beta"
"""
from nltk.compat import raw_input

"""
Este modulo contem funcoes que fazem o tratamento do texto e o coloca em vários formatos
"""

import re
import nltk
import semantic_dictionaries

import unicodedata
import file_utils
from nltk.corpus import mac_morpho
from nltk.corpus import brown
from nltk.corpus import stopwords as stopwordsNLTK

class TextProcessing():
    
                
    
    def pre_processing_sample(self, sample, stopwords, listSym):   
        #Processa uma amostra de texto
       
        return self.remove_stopwords(self.remove_words_with(self.remove_accents(self.text_lower(self.tokenize([sample]))),listSym),stopwords)[0]
    
      
    """
    Recebe uma lista de documentos e retorna o tratamento destes na forma de lista
    de tokens
    """
    def tokenize(self, documents):
        nDocs = len(documents)
        documentsProcessed = []   
        for iDoc in range(0,nDocs):        
            #adicionar a lista
            totoken = documents[iDoc]
            #print "totoken: " + totoken           
            #documentsProcessed.append(nltk.word_tokenize(totoken.decode('utf-8')))
            
            documentsProcessed.append(nltk.word_tokenize(documents[iDoc]))
            
        return documentsProcessed
    
    def tokenize_one(self, document):
        documentProcessed = nltk.word_tokenize(document)
        return documentProcessed    
        
    """
    Recebe uma lista de documentos na forma de tokens e retorna os respectivos bigrams
    """
    def tokenizeBigram(self, documents):
        nDocs = len(documents)
        documentsProcessed = []   
        for iDoc in range(0,nDocs):        
            #adicionar a lista
            documentsProcessed.append(nltk.bigrams(documents[iDoc]))    
        return documentsProcessed
       # print docsPro[0:10]
    
    """
    Separa um texto em sentenças (frases) - Aqui, por ora em portugues!
    """
    def tokenize_sentence(self, documents):    
        tkr = nltk.data.load('tokenizers/punkt/portuguese.pickle')    
        nDocs = len(documents)
        documentsProcessed = []     
        for iDoc in range(0,nDocs):           
            documentsProcessed.append(tkr.tokenize(documents[iDoc]))
        return documentsProcessed
    
    
    
        
    """
    Faz o stemming de uma lista de documentos (disponivel: Pt e En)
    """
    def stemming(self, documents):#,lang):
        nDocs = len(documents)
        documentsProcessed = []
        #if lang == 'Pt':
        stemmer = nltk.stem.RSLPStemmer()
        #elif lang == 'En':
        #   stemmer = nltk.stem.lancaster.LancasterStemmer()
        for iDoc in range(0,nDocs):
            tokens = documents[iDoc]        
            nTokens = len(tokens)        
            stemWords = []      
            for iToken in range(0,nTokens):
                stemWords.append(stemmer.stem(tokens[iToken]))
            tokens = stemWords
            documentsProcessed.append(tokens)
        return documentsProcessed
        
    
    
        
        
    """
    Faz a conversão de um texto para todas as letras minusculas   
    """   
    def text_lower(self, documents):
        nDocs = len(documents)
        documentsProcessed = []     
        for iDoc in range(0,nDocs):
            tokens = documents[iDoc]        
            nTokens = len(tokens)        
            for iToken in range(0,nTokens):
                tokens[iToken] = tokens[iToken].lower()        
            documentsProcessed.append(tokens)
        return documentsProcessed
    
    def text_lower_one(self, document):
        tokens = document      
        nTokens = len(tokens)        
        for iToken in range(0,nTokens):
            tokens[iToken] = tokens[iToken].lower()        
        return tokens
    
    """
    Remove pontuações de um conjunto de documentos
    """
    def remove_punctuation(self, documents):  
        nDocs = len(documents)
        documentsProcessed = []     
        for iDoc in range(0,nDocs):
            tokens = documents[iDoc]
            tokensNR = []
            nTokens = len(tokens)       
            for iToken in range(0,nTokens):
               # print tokens[iToken].decode('utf-8')           
                #punctuation = "',.?!:;“””"
                punctuation = '"*?!,.:;'
                for sym in punctuation:
                    #tokens[iToken] = tokens[iToken].decode('ascii')
                    tokens[iToken] = tokens[iToken].replace(sym,'')
                #print tokens[iToken]
                if len(tokens[iToken]) > 0:
                    tokensNR.append(tokens[iToken])
            #if len(tokensNR) > 0:
            documentsProcessed.append(tokensNR) 
        return documentsProcessed
  
    
    """
    Remove stop words de uma lista de documentos
    """
    
    def remove_stopwords(self, documents, stopwords):
        nDocs = len(documents)
        documentsProcessed = []    
        #stopwords = stopwordsNLTK.words('english') + semantic_dictionaries.stop_words() + semantic_dictionaries.specific_dictionary()
        for iDoc in range(0,nDocs):
            tokens = documents[iDoc]
            #stop words para cada token do documento corrente
            nTokens = len(tokens)
            importantWords = []
            for iToken in range(0,nTokens):            
                if tokens[iToken] not in stopwords:
                    importantWords.append(tokens[iToken])
                
            documentsProcessed.append(importantWords)
        return documentsProcessed
    
    """
    Remove palavras de um documento que contenham algum dos simbolos contidos em 
    uma lista de entrada
    """
    def remove_words_with(self, documents,listSym):    
        nDocs = len(documents)
        documentsProcessed = []     
        for iDoc in range(0,nDocs):
            tokens = documents[iDoc]
            tokensNR = []
            nTokens = len(tokens)       
            for iToken in range(0,nTokens):
                foundSymbol = False
                for sym in listSym:               
                    if tokens[iToken].find(sym) != -1:
                        foundSymbol = True
                        break                    
                if foundSymbol == False:
                    tokensNR.append(tokens[iToken])                
            #if len(tokensNR) > 0:
            documentsProcessed.append(tokensNR) 
        return documentsProcessed
    
    
    """
    Remove acentos de um conjunto de documentos
    """
    def remove_accents(self, documents):  
        nDocs = len(documents)
        documentsProcessed = []     
        for iDoc in range(0,nDocs):
            tokens = documents[iDoc]
            nTokens = len(tokens)       
            for iToken in range(0,nTokens):
                # print unicode(tokens[iToken])#tokens[iToken].decode('utf-8')
                #uStr = tokens[iToken].decode('utf-8')#unicode(tokens[iToken])
                #print unicode(tokens[iToken])
                #print tokens[iToken]
                #print unicode(tokens[iToken])
                #print tokens[iToken].decode('utf-8')
                #raw_input('----------------------------')
                strNorm = unicodedata.normalize('NFKD', tokens[iToken]) #.decode('utf-8')
                #strNorm = bytes(strNorm,'utf-8').decode('utf-8')
                tokens[iToken] = strNorm.encode('ASCII', 'ignore').decode()            
                #print(tokens[iToken])
                #raw_input('-------------')
            documentsProcessed.append(tokens)
        return documentsProcessed
        
    """
    Faz um tagging (analise morfologica de uma lista de documentos)
    """
    
    def tagging(self, documents, savePath, language):
        nDocs = len(documents)
        documentsProcessed = []
        unigram_tagger = []
        from data_core.file_utils import FileUtils
        file_utils = FileUtils(savePath)
        try:
            unigram_tagger = file_utils.load_object('tagger_' + language,'tagger')          
        except:
            if language == "pt":            
                train_set = mac_morpho.tagged_sents()
            elif language == "en":
                train_set = brown.tagged_sents(tagset='universal')
                #print(train_set[0:1])
                nSents = len(train_set)
                train_set_lower = []
                for iSent in range(0,nSents):
                    nWords = len(train_set[iSent])
                    words = []
                    for iWord in range(0,nWords):
                        words.append((self.text_lower_one([train_set[iSent][iWord][0]])[0],train_set[iSent][iWord][1]))
                    
                    train_set_lower.append(words)
                
                
            #print(train_set_lower[0:1])   
            #test_set =  mac_morpho.tagged_sents()[10001:10010]   
            unigram_tagger = nltk.UnigramTagger(train_set_lower)
            file_utils.save_object(unigram_tagger, 'tagger_' + language,'tagger')
        
        for iDoc in range(0,nDocs):
            #tokens = documents[iDoc]
            documentsProcessed.append(unigram_tagger.tag(documents[iDoc]))
        return documentsProcessed
