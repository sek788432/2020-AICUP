#!/usr/bin/env python
# coding: utf-8

import re
import pandas as pd

def add_to_dataframe(start_pos,end_pos,new_txt,new_label,article,article_id):
    check = False
    for i in new_label:   
        if i != "O":
            check = True
    if check == False :
        return False,None,None   # all O data return false
    return_list = []
    B_ind_type = {}              #{ 0:time, 5:name, ...}
    for i in range(len(new_label)):
        #find next i
        if new_label[i][0] == "B":     
            entity_type = new_label[i][2:]
            B_ind_type[i] = entity_type
            
    for key,value in B_ind_type.items():
        ind = key+1
        entity_txt = new_txt[key]
        while ind < len(new_label) and new_label[ind][0] == "I":
            entity_txt+=new_txt[ind]
            ind+=1
        return_list.append([article_id,key+start_pos,key+start_pos+len(entity_txt),entity_txt,value])
    return True,return_list,len(return_list)


def make_contest_output(x_contest, model, path):  
    df = []          
    for article_num in range(len(x_contest)):
        predict = model.predict(x_contest[article_num])
        start_pos = 0
        #i is the index of every senetence
        for i in range(len(x_contest[article_num])):     
            end_pos = start_pos + len(x_contest[article_num][i])
            not_all_o,data,length = add_to_dataframe(start_pos,
                                                     end_pos,
                                                     x_contest[article_num][i],
                                                     predict[i],
                                                     x_contest[article_num],
                                                     article_num)
      
            #data = [article_id, index, index + len(entity_text), entity_text, entity_type]
            if not_all_o:
                for i in range(length):
                    df.append(data[i])   
            start_pos = end_pos
        print("Finish Predict article ", article_num)
    df = pd.DataFrame(df, columns=['article_id', 'start_position', 'end_position', 'entity_text', 'entity_type'])
    df.to_csv(f'{path}.tsv', sep='\t', index=False, encoding='utf8')