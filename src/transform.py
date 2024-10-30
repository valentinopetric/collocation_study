import pandas as pd
import json
import os
import requests

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
    

def get_device_data(device_id,indoor=True,start_date = '2024-10-16 05:00:00',end_date = '2024-10-21 00:00:00'):
    
    if indoor:
        r = requests.get(f"https://airwings-europe.wings-ict-solutions.eu/api/realvaluesindoor?", headers={"x-api-key": "804t9Tges45YyXUJ6GF4gfds45aretEW43w"}, params={"raw": "true",
                    "start": start_date,
                    "stop": end_date,
                    "device_id": device_id
                })
    else:
        r = requests.get(f"https://airwings-europe.wings-ict-solutions.eu/api/realvalues?", headers={"x-api-key": "804t9Tges45YyXUJ6GF4gfds45aretEW43w"}, params={"raw": "true",
                    "start": start_date,
                    "stop": end_date,
                    "device_id": device_id
                })
        
    if len(r.text) < 10:
        return 
    
    file_text = json.loads(r.text)
    df = pd.DataFrame(file_text)
    
    return df

def get_all_devices_data(device_ids,indoor=True,start_date = '2024-10-16 05:00:00',end_date = '2024-10-21 00:00:00'):
    
    df_full = pd.DataFrame()

    for device in device_ids:
        df_device = get_device_data(device,indoor=indoor,start_date=start_date,end_date=end_date)
        df_full = pd.concat([df_full,df_device],axis=0)
    
    return df_full
    

def transform_columns_air_w(df,indoor=True):
    
    if indoor:
        new_column_names = {
            'timestamp': 'datetime',
            'timezone': 'timezone',
            'CO2': 'co2',
            'TVOC': 'tvoc',
            'CO': 'co',
            'PM1': 'pm_1.0',
            'PM25': 'pm_2.5',
            'PM10': 'pm_10',
            'atmospheric_pressure': 'pressure',
        }
        df['sensor'] = 'air_wings_indoor'
    else:
        new_column_names = {
            'timestamp': 'datetime',
            'CO2': 'co2',
            'TVOC': 'tvoc',
            'CO': 'co',
            'PM1': 'pm_1.0',
            'PM25': 'pm_2.5',
            'PM10': 'pm_10',
            'atmospheric_pressure': 'pressure',
            'NO2': 'no2',
            'O3': 'o3',
            'SO2': 'so2',
            'NO': 'no',
        }
        df['sensor'] = 'air_wings_outdoor'
        
    df.rename(columns=new_column_names, inplace=True)
    df.drop(['timezone'],axis=1,inplace=True)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    
    return df