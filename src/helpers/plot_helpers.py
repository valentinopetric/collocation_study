import plotly.graph_objects as go
import pandas as pd
import numpy as np

def plot_experiment_range(df:pd.DataFrame,col_name:str):

    # Create a Plotly figure
    fig = go.Figure()

    # Add time series data
    fig.add_trace(go.Scatter(x=df.index, y=df[col_name], mode='lines', name='Time Series Data'))

    # Fill area for Doors opened
    fig.add_trace(go.Scatter(
        x=["2024-10-16 09:15", "2024-10-16 09:15", "2024-10-16 09:47", "2024-10-16 09:47"],
        y=[min(df[col_name]), max(df[col_name]), max(df[col_name]), min(df[col_name])],
        fill='toself',
        fillcolor='rgba(255, 0, 0, 0.3)',  # Fill color for Doors opened
        line=dict(color='rgba(255, 255, 255, 0)'),  # Transparent line
        name='Doors opened'
    ))

    # Fill area for Hall opened
    fig.add_trace(go.Scatter(
        x=["2024-10-16 20:55", "2024-10-16 20:55", "2024-10-16 21:25", "2024-10-16 21:25"],
        y=[min(df[col_name]), max(df[col_name]), max(df[col_name]), min(df[col_name])],
        fill='toself',
        fillcolor='rgba(0, 0, 255, 0.3)',  # Fill color for Hall opened
        line=dict(color='rgba(255, 255, 255, 0)'),  
        name='Hall opened'
    ))

    # Add vertical line separators
    fig.add_shape(
        type="line",
        x0="2024-10-16 09:15", y0=min(df[col_name]), x1="2024-10-16 09:47", y1=max(df[col_name]),
        line=dict(color="Red", width=2),
    )

    fig.add_shape(
        type="line",
        x0="2024-10-16 20:55", y0=min(df[col_name]), x1="2024-10-16 21:25", y1=max(df[col_name]),
        line=dict(color="Blue", width=2),
    )

    # Update layout
    fig.update_layout(
        title='Time Series Plot with Filled Areas for Phases',
        xaxis_title='Date',
        yaxis_title='Values',
        showlegend=True
    )

    # Show the figure
    fig.show()