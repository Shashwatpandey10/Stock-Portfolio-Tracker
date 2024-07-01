import datetime
import yfinance as yf
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash()
app.title = "Stock Visualization"

app.layout = html.Div(children=[
    html.H1("Stock Visualization Dashboard"),
    html.H4("Please enter the stock symbol"),
    dcc.Input(id='input', value='AAPL', type='text'),
    html.Div(id='output-graph')
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime.now()
    try:
        df = yf.download(input_data, start=start, end=end)
        graph = dcc.Graph(id="example", figure={
            'data': [{'x': df.index, 'y': df['Close'], 'type': 'line', 'name': input_data}],
            'layout': {'title': input_data}
        })
    except Exception as e:
        graph = html.Div(f"Error retrieving stock data: {str(e)}")
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)
