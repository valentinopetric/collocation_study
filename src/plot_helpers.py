import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import json
from datetime import datetime
import os

def plot_range(df: pd.DataFrame, col_names: list,start_date: str="2024-10-16 07:15", end_date: str="2024-10-20 17:15",min_value:int=None,max_value:int=None):
    
    plot_start = datetime.fromisoformat(start_date)
    plot_end = datetime.fromisoformat(end_date)
    
    y_min = min_value if min_value is not None else df[col_names].min().min()
    y_max = max_value if max_value is not None else df[col_names].max().max()

    fig = go.Figure()
    
    for col_name in col_names:
        fig.add_trace(go.Scatter(x=df.index, y=df[col_name], mode='lines', name=col_name))
    
    fig.update_layout(
        title='Time Series Plot',
        xaxis_title='Timestamp',
        showlegend=True,
        xaxis=dict(
            range=[start_date, end_date] if start_date and end_date else [df.index.min(), df.index.max()]
        ),
        yaxis=dict(
        range=[y_min, y_max] if y_min is not None and y_max is not None else [df.min().min(), df.max().max()]
    ),
        width=1200, 
        height=700
    )
    
    fig.update_xaxes(rangeslider_visible=True)

    fig.show()
    

def plot_experiment_range(df: pd.DataFrame, col_names: list,start_date: str="2024-10-16 07:15", end_date: str="2024-10-20 17:15",min_value:int=None,max_value:int=None):

    
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../json','experiments.json'), 'r') as f:
        data = json.load(f)
    
    experiments = data["experiments"]
    colors = data["colors"]
    
    plot_start = datetime.fromisoformat(start_date)
    plot_end = datetime.fromisoformat(end_date)
    
    y_min = min_value if min_value is not None else df[col_names].min().min()
    y_max = max_value if max_value is not None else df[col_names].max().max()

    fig = go.Figure()
    
    for col_name in col_names:
        fig.add_trace(go.Scatter(x=df.loc[start_date:end_date].index, y=df[col_name], mode='lines', name=col_name))

    for experiment, times in experiments.items():
        for start_time, end_time in times:
            start = datetime.fromisoformat(start_time)
            end = datetime.fromisoformat(end_time)
            if start <= plot_end and end >= plot_start:
                fig.add_trace(go.Scatter(
                    x=[start_time, start_time, end_time, end_time],
                    y=[y_min, y_max, y_max, y_min],
                    fill='toself',
                    fillcolor=colors[experiment],
                    line=dict(color='rgba(255, 255, 255, 0)'),  
                    name=experiment
                ))

    fig.update_layout(
        title='Time Series Plot with Experiment Phases Highlighted',
        xaxis_title='Timestamp',
        showlegend=True,
        xaxis=dict(
            range=[start_date, end_date] if start_date and end_date else [df.index.min(), df.index.max()]
        ),
        yaxis=dict(
        range=[y_min, y_max] if y_min is not None and y_max is not None else [df.min().min(), df.max().max()]
    ),
        width=1200, 
        height=700
    )
    
    fig.update_xaxes(rangeslider_visible=True)

    fig.show()

def plot_correlation_matrix(df: pd.DataFrame, title: str = "Correlation Matrix"):

    plt.figure(figsize=(12, 10))
    sns.set(style='white')
    
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    
    sns.heatmap(
        df, 
        annot=True,         
        fmt=".2f",          
        cmap=cmap,          
        square=True,        
        cbar_kws={"shrink": .8},  
        linewidths=.5,      
        annot_kws={"size": 10}    
    )

    plt.title(title, fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(rotation=0, fontsize=10)
    plt.tight_layout()  
    
    plt.show()

def plot_boxplot(df:pd.DataFrame, col_names: list):
    
    fig = go.Figure()

    for col in col_names:
        
        fig.add_trace(go.Box(y=df[col], name=col))

    fig.show()
    