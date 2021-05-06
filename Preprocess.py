#!/usr/bin/env python
# coding: utf-8

import re

def loadInputFile_devData(path: str):
    with open(path, 'r', encoding='utf8') as f:
        file_text = f.read().encode('utf-8').decode('utf-8-sig')
    datas = [d.split('\n') for d in file_text.split('\n\n--------------------\n\n')[:-1]]
    datas = [datas[i][j] for i in range(len(datas)) for j in range(2) if j % 2 == 1]
    return datas

def loadInputFile_trainData(file_path):
    trainingset = list()         # store trainingset [content,content,...]
    position = list()            # store position [article_id, start_pos, end_pos, entity_text, entity_type, ...]
    mentions = dict()            # store mentions[mention] = Type
    with open(file_path, 'r', encoding='utf8') as f:
        file_text = f.read().encode('utf-8').decode('utf-8-sig')
    datas = file_text.split('\n\n--------------------\n\n')[:-1]
    for data in datas:
        data = data.split('\n')
        content = data[0]
        trainingset.append(content)
        annotations = data[1:]
        for annot in annotations[1:]:
            annot = annot.split('\t')  # annot= article_id, start_pos, end_pos, entity_text, entity_type
            position.extend(annot)
            mentions[annot[3]] = annot[4]
    return trainingset, position, mentions


def CRF_format(file):
    training_text, position, _mentions = loadInputFile_trainData(file)
    segment_text_list = [list(t) for t in training_text]
    BIO_list = [['O' for _ in segment_text] for segment_text in segment_text_list]
    for i in range(0, len(position), 5):
        BIO_list[int(position[0 + i])][int(position[1 + i])] = 'B-' + position[4 + i]
        for j in range(int(position[1 + i]) + 1, int(position[2 + i])):
            BIO_list[int(position[0 + i])][j] = 'I-' + position[4 + i]
    return segment_text_list, BIO_list


#(200,5000)     #split with ， 。 ? and combine sentence
def split_sentence(text,label,sequence_length): 
    return_txt = []
    return_label = []
    for article_ID, article in enumerate(text):
        start_ind= 0
        i = 0
        while i < len(article):
            txt_sequence = []
            label_sequence =[]
            while i < len(article) and len(txt_sequence) < sequence_length : 
                if article[i] == "，" or article[i]  == "。" or article[i]  == '?':
                    txt_sequence+=article[start_ind:i+1]
                    label_sequence+=label[article_ID][start_ind:i+1]
                    start_ind = i+1                
                i+=1
            return_txt.append(txt_sequence)
            return_label.append(label_sequence)
    return return_txt,return_label


def split_sentence_tst(text,sequence_length):     #split with ， 。 ? and combine sentence (158,XX,>80)
    return_txt = []
    for article_ID, article in enumerate(text):
        start_ind= 0
        i = 0
        return_tmp = []
        while i < len(article):
            txt_sequence = []
            while i < len(article) and len(txt_sequence) < sequence_length :   #and len(txt_sequence) < sequence_length
                if article[i] == "，" or article[i]  == "。" or article[i]  == '?':
                    txt_sequence+=article[start_ind:i+1]
                    start_ind = i+1                
                i+=1      
            return_tmp.append(txt_sequence)
        return_txt.append(return_tmp)
    return return_txt
                
        
def delete_some_sentence(x_train, y_train):
    for ind,item in enumerate(x_train):
        for j in range(len(item)):
            if y_train[ind][j] != "O":
                break
        else:
            del x_train[ind]
            del y_train[ind]
    return x_train, y_train
