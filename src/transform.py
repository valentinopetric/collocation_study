import pandas as pd
import json
import os

def load_json(path):
    
    with open(path, 'r') as file:
        data = json.load(file)

    return data
    

def transform_diff_avg(df:pd.DataFrame):
    
    df_diff = df.pct_change() * 100
    
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../json','experiments.json'), 'r') as f:
        data = json.load(f)
    
    events = data["experiments"]
    
    diff_averages_df = pd.DataFrame(index=df.columns, columns=events.keys())
    
    for experiment, times in events.items():
        df_exp_full = pd.DataFrame()
        for start_time, end_time in times:
            df_exp_full = pd.concat([df_exp_full,df_diff[start_time:end_time]],axis=0)
        
        diff_averages_df[experiment] = df_exp_full.mean()
       
              
    return diff_averages_df
    
    