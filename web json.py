# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:54:06 2019

@author: sunny
"""
#%% in order to get item_name and item_note
import pandas as pd
data = {}
data['route'] = []
name_list = ['0左', '0右', '1路', '2路', '3路', '5路', '6路', '7路', '9路', '10路', '11路', '14路', '15路', '18路', '19路', '20路', '21路', '77-1路', '77-2路', '88路', '99路', '99路賞鳥', '西環線']
for num in range(0, len(name_list)):
    file_name = 'route_6_0/公車資訊_謙慈_6_0 - ' + name_list[num] + '.csv'
    sample = pd.read_csv(file_name, encoding='utf-8', engine='python')
    title = []
    for col in sample.columns:         
        title.append(col)
    item_name = title[0]
    item_note = sample[title[0]][0]
    
    #get title
    title = []
    sample = pd.read_csv(file_name, encoding='utf-8', skiprows = [0, 1], engine='python')
    for col in sample.columns:         
        title.append(col)
    #calculate the number of titles
    count = 0
    for i in title:
        count = count+1
    print(len(sample))
    
    # write json
    import json

    route_item = []
    schedule = {}
    schedule_title = []
    for i in range(1, count-1):
        schedule_title.append(title[i])
    schedule['title'] = schedule_title
    schedule['content'] = []
    arrive_time = []
    route_detail_id = 0
    ## content
    for i in range(0, len(sample)):
        arrive_time = []
        for j in range(1, count-1):
            if(sample[title[j]][i]!='─'):
                arrive_time.append(sample[title[j]][i])
            else:
                arrive_time.append('');
        if(pd.isna(sample[title[count-1]][i])):
            sample[title[count-1]][i] = ''
        schedule['content'].append({
            'route_detail_id': route_detail_id,
            'arrive_time': arrive_time,
            'schedule_note': sample[title[count-1]][i]
        })
        route_detail_id = route_detail_id + 1
    
    route_item.append({
        'route_item_id': 0,
        'item_name': item_name,
        'item_note': item_note, 
        'schedule': schedule
    })
    ## repeat for 返程
    file_name = 'route_6_1/公車資訊_謙慈_6_1 - ' + name_list[num] + '.csv'
    sample = pd.read_csv(file_name, encoding='utf-8', engine='python')
    title = []
    for col in sample.columns:         
        title.append(col)
    item_name = title[0]
    item_note = sample[title[0]][0]
    title = []
    sample = pd.read_csv(file_name, encoding='utf-8', skiprows = [0, 1], engine='python')
    for col in sample.columns:         
        title.append(col)
    #calculate the number of titles
    count = 0
    for i in title:
        count = count+1
    
    schedule = {}
    schedule_title = []
    for i in range(1, count-1):
        schedule_title.append(title[i])
    schedule['title'] = schedule_title
    schedule['content'] = []
    arrive_time = []
    route_detail_id = 0
    for i in range(0, len(sample)):
        arrive_time = []
        for j in range(1, count-1):
            if(sample[title[j]][i]!='─'):
                arrive_time.append(sample[title[j]][i])
            else:
                arrive_time.append('');
        if(pd.isna(sample[title[count-1]][i])):
            sample[title[count-1]][i] = ''
        schedule['content'].append({
            'route_detail_id': route_detail_id,
            'arrive_time': arrive_time,
            'schedule_note': sample[title[count-1]][i]
        })
        route_detail_id = route_detail_id + 1
    route_item.append({
        'route_item_id': 1,
        'item_name': item_name,
        'item_note': item_note, 
        'schedule': schedule
    })
    #########
    
    data['route'].append({
        'route_id': num,
        'route_name': name_list[num],
        'route_item': route_item
    })
with open('data.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json.dumps(data, ensure_ascii=False, indent=4))