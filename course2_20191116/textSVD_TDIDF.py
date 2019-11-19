# -*- coding: utf-8 -*-


import numpy as np
import pylab
import re
from scipy import linalg
from matplotlib import pyplot

# 文档
documents = [
    "Roronoa Zoro, nicknamed \"Pirate Hunter\" Zoro, is a fictional character in the One Piece franchise created by Eiichiro Oda.",
    "In the story, Zoro is the first to join Monkey D. Luffy after he is saved from being executed at the Marine Base. ",
    "Zoro is an expert swordsman who uses three swords for his Three Sword Style, but is also capable of the one and two-sword styles. ",
    "Zoro seems to be more comfortable and powerful using three swords, but he also uses one sword or two swords against weaker enemies.",
    "In One Piece, Luffy sails from the East Blue to the Grand Line in search of the legendary treasure One Piece to succeed Gol D. Roger as the King of the Pirates. ",
    "Luffy is the captain of the Straw Hat Pirates and along his journey, he recruits new crew members with unique abilities and personalities. ",
    "Luffy often thinks with his stomach and gorges himself to comical levels. ",
    "However, Luffy is not as naive as many people believe him to be, showing more understanding in situations than people often expect. ",
    "Knowing the dangers ahead, Luffy is willing to risk his life to reach his goal to become the King of the Pirates, and protect his crew.",
    "Adopted and raised by Navy seaman turned tangerine farmer Bellemere, Nami and her older sister Nojiko, have to witness their mother being murdered by the infamous Arlong.",
    "Nami, still a child but already an accomplished cartographer who dreams of drawing a complete map of the world, joins the pirates, hoping to eventually buy freedom for her village. ",
    "Growing up as a pirate-hating pirate, drawing maps for Arlong and stealing treasure from other pirates, Nami becomes an excellent burglar, pickpocket and navigator with an exceptional ability to forecast weather.",
    "After Arlong betrays her, and he and his gang are defeated by the Straw Hat Pirates, Nami joins the latter in pursuit of her dream."
]

documents = []
with open('textSVD.txt', 'r') as file:
    for line in file:
        documents.append(line.strip())


print(len(documents))
# 停用词
stopwords = ['a', 'an', 'after', 'also', 'and', 'as', 'be', 'being', 'but', 'by', 'd', 'for', 'from', 'he', 'her',
             'his', 'in', 'is', 'more', 'of', 'often', 'the', 'to', 'who', 'with', 'people']
# 要去除的标点符号的正则表达式
punctuation_regex = '[,.;"]+'
# map,key是单词,value是单词出现的文档编号
dictionary = {}

## 词列表
dict = []


text = ''
for d in documents:
    text += ' '+d

def word_rate(dict,text):
    if

# 依次处理每篇文档
for d in documents:
    words = d.split();
    for w in words:
        # 去标点
        w = re.sub(punctuation_regex, '', w.lower())
        if w in stopwords:
            continue
        elif w in dictionary:
            dictionary[w].append(currentDocId)
        else:
            dictionary[w] = [currentDocId]
    currentDocId += 1





def word_rate(word, doc):
    for w in dictionary:
        word = dictionary[w]





