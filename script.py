import pandas as pd
import numpy as np 

data = pd.read_csv("games.csv")
stat = pd.read_csv("stat.csv")



def inpput(flag = 1):
    if flag == 0:
       None

    else:
        on = input("please enter column name : ")
        copyy = data.copy()
        copyy[on].drop_duplicates(inplace = True)
        temp = copyy[on].unique()
        tempdf = pd.DataFrame()
        tempdf[on] = temp
        tempdf.to_csv(f'{on}_stat.csv' , index=False)
        read = pd.read_csv(f'{on}_stat.csv')
        return on


on = inpput()


def cal_on(para):
    
    
    
    ftemp = data[data[on] == para]
    count = ftemp['Name'].count()
    maxx = ftemp.loc[ : , 'Global_Sales'].max()
    temp = ftemp[ftemp["Global_Sales"] == maxx]
    bestgamesales = temp['Global_Sales'].head(1).values
    topgamessales = temp["Name"].head(1).values
    totalsales = ftemp['Global_Sales'].sum()
    

    return count , bestgamesales , topgamessales , totalsales 
    

    
def ret_on():
    count = []
    best_game_sales =  [] 
    best_game_name =   []
    totalsales = []

    temp = pd.read_csv(f'{on}_stat.csv')
    
    for i  , row in temp.iterrows():
        returnn = cal_on(row[f'{on}'])
        count.append(returnn[0])
        best_game_sales.append(returnn[1])
        best_game_name.append(returnn[2])       
        totalsales.append(returnn[3])

    return count  , best_game_sales , best_game_name , totalsales




def retttt():

    temp = pd.read_csv(f'{on}_stat.csv')
    rett = ret_on()
    temp['count'] = rett[0]
    temp['best_game_name'] = rett[2]
    temp['best_game_sales'] = rett[1]
    temp['total_sales'] = rett[3]
    temp.sort_values(by='total_sales' , ascending=False , inplace=True)
    print(temp)
    temp.to_csv(f'{on}_stat.csv' , index=False)
    




def search():
    on  = input("please enter base : ").capitalize()
    choice = input("enter what you want to search for : ")
    cond = choice.isdigit()
    print(cond)
    if cond == True:
        temp = data[data[on] == int(choice)]
        
    else:
        temp = data[data[on] == choice]

    count = temp["Name"].count()
    print("********************************************************************************")
    print(f'the search is on {on} ({choice}) and the count of results is {count}')
    print("********************************************************************************")
    print(temp)


retttt()