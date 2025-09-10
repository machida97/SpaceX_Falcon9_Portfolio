# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read SpaceX data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__) 

# App layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Multi-select dropdown for Launch Sites
    html.P("Select Launch Site(s):"),
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()] + [{'label': 'ALL', 'value': 'ALL'}],
        value=['ALL'],
        multi=True,
        placeholder="Select Launch Site(s)",
        searchable=True
    ),
    html.Br(),
    
    # Dropdown to filter by Booster Version Category
    html.P("Select Booster Version Category:"),
    dcc.Dropdown(
        id='booster-dropdown',
        options=[{'label': cat, 'value': cat} for cat in spacex_df['Booster Version Category'].unique()] + [{'label': 'ALL', 'value': 'ALL'}],
        value='ALL',
        placeholder="Select Booster Version Category",
        searchable=True
    ),
    html.Br(),
    
    # Summary statistics
    html.Div(id='summary-stats', style={'fontSize': 16, 'marginBottom': 20}),
    
    # Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    
    html.P("Payload range (Kg):"),
    # Payload range slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),
    html.Br(),
    
    # Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
    html.Br(),
    
    # Line chart of success rate over flight number
    html.Div(dcc.Graph(id='success-over-time-chart'))
])

# Callback to update summary stats
@app.callback(
    Output('summary-stats', 'children'),
    Input('site-dropdown', 'value'),
    Input('booster-dropdown', 'value'),
    Input('payload-slider', 'value')
)
def update_summary(selected_sites, selected_booster, payload_range):
    df = spacex_df.copy()
    
    # Filter by payload
    df = df[(df['Payload Mass (kg)'] >= payload_range[0]) & (df['Payload Mass (kg)'] <= payload_range[1])]
    
    # Filter by sites
    if 'ALL' not in selected_sites:
        df = df[df['Launch Site'].isin(selected_sites)]
    
    # Filter by booster
    if selected_booster != 'ALL':
        df = df[df['Booster Version Category'] == selected_booster]
    
    total_launches = df.shape[0]
    successes = df['class'].sum()
    success_rate = (successes / total_launches * 100) if total_launches > 0 else 0
    
    return [
        html.P(f"Total Launches: {total_launches}"),
        html.P(f"Successful Launches: {successes}"),
        html.P(f"Success Rate: {success_rate:.2f}%")
    ]

# Callback to update pie chart
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value'),
    Input('booster-dropdown', 'value'),
    Input('payload-slider', 'value')
)
def update_pie_chart(selected_sites, selected_booster, payload_range):
    df = spacex_df.copy()
    df = df[(df['Payload Mass (kg)'] >= payload_range[0]) & (df['Payload Mass (kg)'] <= payload_range[1])]
    
    if 'ALL' not in selected_sites:
        df = df[df['Launch Site'].isin(selected_sites)]
    
    if selected_booster != 'ALL':
        df = df[df['Booster Version Category'] == selected_booster]
    
    if df.empty:
        return px.pie(title="No data to display")
    
    if 'ALL' in selected_sites or len(selected_sites) > 1:
        fig = px.pie(df, names='Launch Site', values='class', title='Total Success Launches by Site')
    else:
        site = selected_sites[0]
        class_counts = df['class'].value_counts().reset_index()
        class_counts.columns = ['class', 'count']
        fig = px.pie(class_counts, values='count', names='class', title=f'Success vs Failure for {site}')
    
    return fig

# Callback to update scatter chart
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    Input('site-dropdown', 'value'),
    Input('booster-dropdown', 'value'),
    Input('payload-slider', 'value')
)
def update_scatter(selected_sites, selected_booster, payload_range):
    df = spacex_df.copy()
    df = df[(df['Payload Mass (kg)'] >= payload_range[0]) & (df['Payload Mass (kg)'] <= payload_range[1])]
    
    if 'ALL' not in selected_sites:
        df = df[df['Launch Site'].isin(selected_sites)]
    
    if selected_booster != 'ALL':
        df = df[df['Booster Version Category'] == selected_booster]
    
    fig = px.scatter(
        df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        hover_data=['Flight Number', 'Booster Version'],
        title="Payload vs Success"
    )
    return fig

# Callback to update success rate over time
@app.callback(
    Output('success-over-time-chart', 'figure'),
    Input('site-dropdown', 'value'),
    Input('booster-dropdown', 'value'),
    Input('payload-slider', 'value')
)
def update_success_over_time(selected_sites, selected_booster, payload_range):
    df = spacex_df.copy()
    df = df[(df['Payload Mass (kg)'] >= payload_range[0]) & (df['Payload Mass (kg)'] <= payload_range[1])]
    
    if 'ALL' not in selected_sites:
        df = df[df['Launch Site'].isin(selected_sites)]
    
    if selected_booster != 'ALL':
        df = df[df['Booster Version Category'] == selected_booster]
    
    if df.empty:
        return px.line(title="No data to display")
    
    df_grouped = df.groupby('Flight Number')['class'].mean().reset_index()
    fig = px.line(df_grouped, x='Flight Number', y='class', markers=True,
                  title="Success Rate Over Flight Number")
    fig.update_yaxes(title="Success Rate")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8080, debug=False)
