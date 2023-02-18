import PyPDF2
import os, os.path, re
from os import walk
import pandas as pd
import numpy as np    
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
from statistics import mode

#directory
directory = "pdfs"
Frequency_directory = "Frequency_input_data.txt"
Research_directory = "Research_input_data.txt"
Literature_review_directory = "Literature_review.pdf"

def pdf_review():
    lst = os.listdir(directory) 
    number_files = len(lst)
    array_leng = int(number_files)
    arX = ["x"]*array_leng
    filenames = next(walk(directory), (None, None, []))[2] 
    SearchString = "markov"

    for idx, item in enumerate(arX):
        try:
            objName = directory+filenames[idx]
            object = PyPDF2.PdfFileReader(objName, strict=False)
            NumPages = object.getNumPages()
            for i in range(0, NumPages):
                PageObj = object.getPage(i)
                Text = PageObj.extractText() 
                TextSTR = str(Text)
                ResSearch = re.search(SearchString, str(Text))
                if len(str(ResSearch)) > 10:
                    file = open(Research_directory,'a')
                    file.writelines("File #"+str(idx)+"✅"+" Page: "+str(i)+"\n"+"ResSearch: "+str(ResSearch)+"\n\n"+str(Text)+"\n\n")
                    file.close()    
                print(ResSearch)
                split_it = TextSTR.split()
                stopwords = ["used","Fig.","r","u","6","70","2019","!","0.7","70","(Yes)","No","E","J.,","<1,","[CrossRef]","936","2", "vol.", "pp.", "n", "10:00", "C,", "1.T","fi","Without","given","From","ep","10","t","0.46","19,","E[Li]","R.","1>","M.,","Yes","di","etc","0:039", "0.00","b","C","108","ðÞ","S","s","t",'The',"al.","^","If","an","In","J.","A.","Atlason,",",","email","09:45","m","0","15","o","by","M",".","3", "GA", "1","0","23,","that","we","was","M.","[","each","on", "sta±ng", "&", "be", "are", "09:15", "A", "is","set","h","show","can","e","true","=","at","more","as","i", "09:30","et","under","said","all", "will","with", "from",'the', "and", "in", "of", "to", "for","(", "or", "a"]
                for word in list(split_it):  # iterating on a copy since removing will mess things up
                    if word in stopwords:
                            split_it.remove(word)
                temp = [wrd for sub in split_it for wrd in sub.split()]
                res = mode(temp)
                #print("Word with maximum frequency : " + str(res))
                file = open(Frequency_directory,'a')
                file.writelines("File #"+str(idx)+"✅ == "+str(res)+"\n")
                file.close() 
            file = open(Frequency_directory,'a')
            file.writelines("\n")
            file.close() 
        except Exception as E:
            print(E)
        print("File #"+str(idx+1)+"✅")
    return "succes"

def Literature_review():
    number_files = 1
    array_leng = int(number_files)
    arX = ["x"]*array_leng
    SearchString = "Scheduling"
    for idx, item in enumerate(arX):
        try:
            objName = Literature_review_directory
            object = PyPDF2.PdfFileReader(objName, strict=False)
            NumPages = object.getNumPages()
            for i in range(0, NumPages):
                PageObj = object.getPage(i)
                Text = PageObj.extractText() 
                TextSTR = str(Text)
                ResSearch = re.search(SearchString, str(Text))
                if len(str(ResSearch)) > 10:
                    file = open(Research_directory,'a')
                    file.writelines("File #"+str(idx)+"✅"+" Page: "+str(i)+"\n"+"ResSearch: "+str(ResSearch)+"\n\n"+str(Text)+"\n\n")
                    file.close()    
                split_it = TextSTR.split()
                stopwords = ["optimale","vores","dette","ours","our","fra","ikke","https://www.scopus.com/record/display.uri?eid=2-s2.0-","Vi","I","are","or","det","som","de","we","on","vi","ved","a","kan","et","på","den","-","in","der","med","and","af","og","af","the","at","er","en","i","of","til","for","to"]
                for word in list(split_it):  # iterating on a copy since removing will mess things up
                    if word in stopwords:
                            split_it.remove(word)
                temp = [wrd for sub in split_it for wrd in sub.split()]
                res = mode(temp)
                #print("Word with maximum frequency : " + str(res))
                file = open(Frequency_directory,'a')
                file.writelines("File #"+str(idx)+"✅ == "+str(res)+"\n")
                file.close() 
            file = open(Frequency_directory,'a')
            file.writelines("\n")
            file.close() 
        except Exception as E:
            print(E)
        print("File #"+str(idx)+"✅")
    return "succes"

#Literature_review()
pdf_review()