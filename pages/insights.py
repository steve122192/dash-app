# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Model Insights
            
            ##### Here's a breakdown of the features the model used, and how they affected it's decision making. Green indicates an overall positive relationship with 'success' as we've defined it (NFL starts per season) and red means the opposite.

            ##### Some of this comes as no surprise. Winning many times and completing a lot of passes every year in college is naturally indicative of some talent. But, some features are a bit counter-intuitive.

            ##### **Total Completions & TDs:** Maybe staying in college and racking up stats is indicative of a QB that is under-challenged and under-prepared for the NFL?

            ##### **40-Yard Dash:** Slower times are associated with more success. This supports the idea that running quarterbacks might struggle in the NFL.

            ##### **Power 5 Conference:** This turned out to hardly be a factor. Score one for the the underdogs!

            ...
            """
        ),
        dcc.Link(dbc.Button('Predict', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/permutaions.png', className='img-fluid'),
    ],
)

layout = dbc.Row([column1, column2])