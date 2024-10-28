import plotly.graph_objects as go
import pandas as pd
import numpy as np

def plot_experiment_range(df: pd.DataFrame, col_name: str):
    # Define experiment time ranges and fill colors
    experiments = {
        "Doors opened": [("2024-10-16 09:15", "2024-10-16 09:47")],
        "Hall opened": [("2024-10-16 20:55", "2024-10-16 21:25")],
        "Indoor Room Air Exchange": [("2024-10-17 18:20", "2024-10-17 18:50")],
        "Exercise (Rowing)": [("2024-10-19 10:40", "2024-10-19 10:54"), ("2024-10-19 11:24", "2024-10-19 11:41")],
        "Human Presence": [("2024-10-19 12:02", "2024-10-19 12:53"), ("2024-10-19 13:34", "2024-10-19 14:08")],
        "Diffuser (Water)": [("2024-10-19 14:33", "2024-10-19 14:51")],
        "Diffuser (Oil)": [("2024-10-19 15:06", "2024-10-19 15:20")],
        "Car": [("2024-10-19 15:33", "2024-10-19 15:38"), ("2024-10-19 15:53", "2024-10-19 15:58")],
        "Gas Burner": [("2024-10-20 13:10", "2024-10-20 13:40"), ("2024-10-20 14:00", "2024-10-20 14:30")],
        "Candle": [("2024-10-20 14:51", "2024-10-20 15:15")]
    }
    
    colors = {
        "Doors opened": 'rgba(255, 0, 0, 0.3)',
        "Hall opened": 'rgba(0, 0, 255, 0.3)',
        "Indoor Room Air Exchange": 'rgba(0, 255, 0, 0.3)',
        "Exercise (Rowing)": 'rgba(255, 165, 0, 0.3)',
        "Human Presence": 'rgba(255, 20, 147, 0.3)',
        "Diffuser (Water)": 'rgba(30, 144, 255, 0.3)',
        "Diffuser (Oil)": 'rgba(75, 0, 130, 0.3)',
        "Car": 'rgba(128, 128, 128, 0.3)',
        "Gas Burner": 'rgba(255, 69, 0, 0.3)',
        "Candle": 'rgba(255, 223, 0, 0.3)'
    }

    # Create the plotly figure
    fig = go.Figure()

    # Plot the main time series data
    fig.add_trace(go.Scatter(x=df.index, y=df[col_name], mode='lines', name='Time Series Data'))

    # Loop through experiments and add shaded regions
    for experiment, times in experiments.items():
        for start_time, end_time in times:
            fig.add_trace(go.Scatter(
                x=[start_time, start_time, end_time, end_time],
                y=[min(df[col_name]), max(df[col_name]), max(df[col_name]), min(df[col_name])],
                fill='toself',
                fillcolor=colors[experiment],
                line=dict(color='rgba(255, 255, 255, 0)'),  # Transparent outline
                name=experiment
            ))

            # Add vertical lines as separators
            fig.add_shape(
                type="line",
                x0=start_time, y0=min(df[col_name]), x1=end_time, y1=max(df[col_name]),
                line=dict(color=colors[experiment].replace('0.3', '1.0'), width=2),
            )

    # Update layout with titles and legends
    fig.update_layout(
        title='Time Series Plot with Experiment Phases Highlighted',
        xaxis_title='Timestamp',
        yaxis_title=col_name,
        showlegend=True
    )

    # Display the plot
    fig.show()