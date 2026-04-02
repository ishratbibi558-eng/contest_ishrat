import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample Data Preparation

# Generating a sample dataset

# This data would typically be fetched from a database or API in a real-world scenario
# For the sake of demonstration, I'm creating a simple dataframe

sample_data = {
    'Date': pd.date_range(start='2026-01-01', periods=100, freq='D'),
    'Value': pd.np.random.randint(1, 100, size=100)
}

df = pd.DataFrame(sample_data)

# Create a Dash application
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Visual Analytics Dashboard'),
    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bar-chart'),
])


@app.callback(Output('line-chart', 'figure'), Input('interval-component', 'n_intervals'))
def update_line_chart(n):
    line_fig = px.line(df, x='Date', y='Value', title='Line Chart of Values')
    return line_fig


@app.callback(Output('bar-chart', 'figure'), Input('interval-component', 'n_intervals'))
def update_bar_chart(n):
    bar_fig = px.bar(df, x='Date', y='Value', title='Bar Chart of Values')
    return bar_fig


if __name__ == '__main__':
    app.run_server(debug=True)