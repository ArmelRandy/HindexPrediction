import ast
import pandas as pd

def cleaning(word):
    indice = word.find("----")
    id = int(word[0:indice])
    dico = ast.literal_eval(word[indice+4:])
    indexlength = int(dico["IndexLength"])
    invertedindex = dico["InvertedIndex"]
    return id, indexlength, invertedindex
def clean_1(word):
    indice = word.find("----")
    id = int(word[0:indice])
    return id
def clean_2(word):
    indice = word.find("----")
    id = int(word[0:indice])
    dico = ast.literal_eval(word[indice+4:])
    indexlength = int(dico["IndexLength"])
    return indexlength
def clean_3(word):
    indice = word.find("----")
    id = int(word[0:indice])
    dico = ast.literal_eval(word[indice+4:])
    invertedindex = dico["InvertedIndex"]
    return str(invertedindex)

if __name__ == "__main__" :
    abs = pd.read_csv('abstracts.txt', sep = "\n", header = None)
    abs["paper_ID"] = abs[0].apply(lambda x : clean_1(x))
    abs["IndexLength"] = abs[0].apply(lambda x : clean_2(x))
    abs["InvertedIndex"] = abs[0].apply(lambda x : clean_3(x))
    abs.drop(columns = [0], inplace = True)
    abs.to_csv("filename.csv", index = False)