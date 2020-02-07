# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

from joblib import load
pipeline = load('assets/pipeline.joblib')

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [#Input('completions_per_year', 'value'), Input('wins_per_year', 'value'), Input('height', 'value'),
    #Input('forty_yard_dash', 'value')],
    Input('games_played', 'value'), Input('passing_completions', 'value'), Input('passing_attempts', 'value'),
    Input('passing_percentage', 'value'), Input('passing_yards', 'value'), Input('passing_tds', 'value'),
    Input('passing_ints', 'value'), Input('passer_rating', 'value'), Input('passes_per_year', 'value'),
    Input('completions_per_year', 'value'), Input('yards_per_year', 'value'), Input('tds_per_year', 'value'),
    Input('ints_per_year', 'value'), Input('height', 'value'), Input('weight', 'value'),
    Input('forty_yard_dash', 'value'), Input('vert_leap', 'value'), Input('broad_jump', 'value'),
    Input('shuttle_run', 'value'), Input('three_cone', 'value'), Input('no_combine_attendance', 'value'),
    Input('power_five_conf', 'value'), Input('conference_championships', 'value'), Input('wins_per_year', 'value')],
)
def predict(#completions_per_year, wins_per_year, height, forty_yard_dash):
    games_played, passing_completions, passing_attempts, 
              passing_percentage, passing_yards, passing_tds, passing_ints,
              passer_rating, passes_per_year, completions_per_year, yards_per_year,
              tds_per_year, ints_per_year, height, weight, forty_yard_dash,
              vert_leap, broad_jump, shuttle_run, three_cone, no_combine_attendance,
              power_five_conf, conference_championships, wins_per_year):
    df = pd.DataFrame(
        columns=[#'completions_per_year','wins_per_year','height','forty_yard_dash'],
            'games_played','passing_completions','passing_attempts',
              'passing_percentage','passing_yards','passing_tds','passing_ints',
              'passer_rating','passes_per_year','completions_per_year','yards_per_year',
              'tds_per_year','ints_per_year','height','weight','forty_yard_dash',
              'vert_leap','broad_jump','shuttle_run','three_cone','no_combine_attendance',
              'power_five_conf','conference_championships','wins_per_year'], 
        data=[[#completions_per_year, wins_per_year, height, forty_yard_dash]]
            games_played, passing_completions, passing_attempts, 
              passing_percentage, passing_yards, passing_tds, passing_ints,
              passer_rating, passes_per_year, completions_per_year, yards_per_year,
              tds_per_year, ints_per_year, height, weight, forty_yard_dash,
              vert_leap, broad_jump, shuttle_run, three_cone, no_combine_attendance,
              power_five_conf, conference_championships, wins_per_year]]
    )
    y_pred = pipeline.predict(df)[0]
    return html.H1(f'{y_pred:.0f} Starts')


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Input the college stats of the quarterback that you would like to predict.

            """
        ),
        dcc.Markdown('#### Completions per Year'),
        dcc.Input(
        id='completions_per_year',
        placeholder='AVG: 178',
        type='number',
        value=178
        ),
        dcc.Markdown('#### Passing Yards per Season'),
        dcc.Input(
        id='yards_per_year',
        placeholder='AVG: 2194',
        type='number',
        value=2194
        ),
        dcc.Markdown('#### Passes per Year'),
        dcc.Input(
        id='passes_per_year',
        placeholder='AVG: 211',
        type='number',
        value=211
        ),       
        dcc.Markdown('#### Passing TDs per Season'),
        dcc.Input(
        id='tds_per_year',
        placeholder='AVG: 15',
        type='number',
        value=15
        ),
        dcc.Markdown('#### Interceptions per Season'),
        dcc.Input(
        id='ints_per_year',
        placeholder='AVG: 8',
        type='number',
        value=8
        ),
        dcc.Markdown('#### Height (in)'),
        dcc.Input(
        id='height',
        placeholder='AVG: 74',
        type='number',
        value=74
        ),
        dcc.Markdown('#### Weight (lb)'),
        dcc.Input(
        id='weight',
        placeholder='AVG: 222 lbs',
        type='number',
        value=222
        ),
        dcc.Markdown('#### 40 Time'),
        dcc.Input(
        id='forty_yard_dash',
        placeholder='AVG: 4.87 Seconds',
        type='number',
        value=4.87
        ),
        dcc.Markdown('#### Vertical Leap (in)'),
        dcc.Input(
        id='vert_leap',
        placeholder='AVG: 24 inches',
        type='number',
        value=24
        ),
        dcc.Markdown('#### 3-Cone Drill'),
        dcc.Input(
        id='three_cone',
        placeholder='AVG: 7.34 Seconds',
        type='number',
        value=7.34
        ),
        dcc.Markdown('#### Broad Jump'),
        dcc.Input(
        id='broad_jump',
        placeholder='AVG: 106 inches',
        type='number',
        value=106
        ),    
        dcc.Markdown('#### Shuttle Run'),
        dcc.Input(
        id='shuttle_run',
        placeholder='AVG: 4.46 Seconds',
        type='number',
        value=4.46
        ),                                   
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('#### Games Played'),
        dcc.Input(
        id='games_played',
        placeholder='AVG: 32 Games',
        type='number',
        value=32
        ),
        dcc.Markdown('#### Total Passing Completions'),
        dcc.Input(
        id='passing_completions',
        placeholder='AVG: 563',
        type='number',
        value=563
        ),
        dcc.Markdown('#### Total Passing Attempts'),
        dcc.Input(
        id='passing_attempts',
        placeholder='AVG: 939',
        type='number',
        value=939
        ),
        dcc.Markdown('#### Career Passing Percentage'),
        dcc.Input(
        id='passing_percentage',
        placeholder='AVG: 59.2',
        type='number',
        value=59.2
        ),
        dcc.Markdown('#### Total Passing Yards'),
        dcc.Input(
        id='passing_yards',
        placeholder='AVG: 6900',
        type='number',
        value=6900
        ),
        dcc.Markdown('#### Total Passing TDs'),
        dcc.Input(
        id='passing_tds',
        placeholder='AVG: 49',
        type='number',
        value=49
        ),
        dcc.Markdown('#### Total Interceptions'),
        dcc.Input(
        id='passing_ints',
        placeholder='AVG: 26',
        type='number',
        value=26
        ),
        dcc.Markdown('#### Career Passer Rating'),
        dcc.Input(
        id='passer_rating',
        placeholder='AVG: 131',
        type='number',
        value=131
        ),
        dcc.Markdown('#### Wins per Year'), 
        dcc.Slider(
            id='wins_per_year', 
            min=0, 
            max=12, 
            step=13, 
            value=5, 
            marks={n: str(n) for n in range(0,13,1)}, 
            className='mb-5', 
        ),      
        dcc.Markdown('#### Conference Championships Won'), 
        dcc.Slider(
            id='conference_championships', 
            min=0, 
            max=4, 
            step=4, 
            value=0, 
            marks={n: str(n) for n in range(0,5,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Attended Combine'), 
        dcc.Dropdown(
            id='no_combine_attendance', 
            options = [
                {'label': 'Yes', 'value': 0}, 
                {'label': 'No', 'value': 1}, 
            ], 
            value = 0, 
            className='mb-5',
        ),
        dcc.Markdown('#### Power 5 Conference'), 
        dcc.Dropdown(
            id='power_five_conf', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, 
            ], 
            value = 1, 
            className='mb-5',
        ),   
    ],
    md=4,
)

column3 = dbc.Col(
    [
        html.H2('Expected NFL Starts per Season', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2, column3])