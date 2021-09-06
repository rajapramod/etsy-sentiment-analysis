#------------------------- Imports -------------------------------
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords

import webbrowser
from threading import Timer
from layouts import (
    header,
    footer,
    piechart,
    check_review,
    wordcloud_bargraph
)
from layouts.check_review import load_model


#----------------------------------------------- Global Variables --------------------------------------------

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}], suppress_callback_exceptions = True)
df2 = pd.read_csv('data/words_frequency.csv', encoding='utf-8')
port = 8050
#----------------------------------------------- Defining App Layout ------------------------------------------

def create_app_ui():

    app_layout = html.Div([

        header.create_layout(app),

        html.Div([
                html.H1(['Sentiment Analysis of Customer Reviews on ', 
                html.A(['Etsy.com'], href='https://www.etsy.com', target='_blank', id='etsy-link')],
                id='main-title'),
        ], id='top'),


        html.H3(['Pie Chart Analysis'], id='piechart', className='subtitle'),

        html.Div([
                piechart.create_layout(app)
            ], id='piechart-main-div'),

        html.Div([
                html.H3('Check Sentiment Of Your Review', id='check-review', className='subtitle'),
                
                check_review.create_layout(app)

            ], id='check-review-main-div'),

        html.Div([
            html.H3('Most Frequent Words From Etsy.com Reviews', id='wordcloud', className='subtitle'),

            wordcloud_bargraph.create_layout()
        ]),

        footer.create_layout(app)

        ], id='main_app_layout', className='app-layout-div')
    return app_layout

#----------------------------------------------- Defining Functions ---------------------------------------------------
def open_browser():
    webbrowser.open_new("http://localhost:{}".format(port))

def black_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")

#-----------------------------------------------  App Callbacks ---------------------------------------------------
@app.callback(
                Output(component_id='review-result', component_property='children'),
             [
                Input(component_id='textarea-click-button', component_property='n_clicks')
             ],
             [
                State('text-area-box', 'value')
             ])
def update_text_review(n_clicks, textarea_value):
    print('Data type of textarea_value: ', str(type(textarea_value)))
    print('Value of textarea_value: ', str(textarea_value))
    
    print('Data type of n_clicks for textbox section: ', str(type(n_clicks)))
    print('Value of n_clicks for textbox section: ', str(n_clicks))
    if n_clicks > 0:
        response = check_review.check_review(textarea_value)
        if response[0] == 0:
            result = html.H4('Sentiment: Review is NEGATIVE!', style={'color':'red'}, className='result')
        elif response[0] == 1:
            result = html.H4('Sentiment: Review is POSITIVE!', style={'color':'green'}, className='result')
        else:
            result = ' Result Unknown'
        return result
    else:
        return ''

@app.callback(Output(component_id='dropdown-review-result', component_property='children'),
                [
                Input(component_id='review-dropdown', component_property='value'),
                Input(component_id='dropdown-click-button', component_property='n_clicks')
                ],
            )
def review_dropdown_function(review_dropdown, n_clicks):
    print('Data type of review_dropdown: ', str(type(review_dropdown)))
    print('Value of review_dropdown: ', str(review_dropdown))
    
    print('Data type of n_clicks for review_dropdown section: ', str(type(n_clicks)))
    print('Value of n_clicks for review_dropdown section: ', str(n_clicks))
    result = ''
    if n_clicks > 0:
        response = check_review.check_review(review_dropdown)
        if response[0] == 0:
            result = html.H4('Sentiment: Review is NEGATIVE!', style={'color':'red'}, className='result')
        elif response[0] == 1:
            result = html.H4('Sentiment: Review is POSITIVE!', style={'color':'green'}, className='result')
        else:
            result = 'Result Unknown'
        return result
    else:
        return ''


@app.callback(
        Output(component_id='bar-chart', component_property='figure'),
        [
        Input(component_id='bargraph-dropdown', component_property='value')
        ],
    )
def update_bargraph(no_of_words):
    print('Number of words: ', no_of_words)
    print(type(no_of_words))
    dff = df2.iloc[0:no_of_words, :]
    fig = px.bar(dff, x='words', y='frequency')

    fig.update_traces(hovertemplate='Word:%{x}<br>Repeated: %{y} times<extra></extra>')
    fig.update_layout(title = {'font': {'family': 'Playfair Display', 'size': 26}, 'pad': {'l': 380}, 'text': 'Words v/s Frequency Chart'})
    return fig

    
@app.callback(
        Output(component_id='wordcloud-figure', component_property='figure'),
        [
        Input(component_id='wordcloud-dropdown', component_property='value')
        ]
    )
def wordcloud(words_number):
    dff = pd.read_csv('data/words_frequency.csv')        
    wordcloud = WordCloud(font_path = '../data/arial.ttf', width=3000, height=2000,
                background_color ='white', 
                stopwords = stopwords,
                min_font_size = 10, max_words = words_number).generate_from_frequencies(dff.set_index('words')['frequency'].to_dict())
    wordcloud.recolor(color_func=black_color_func)
    
    fig_wordcloud = px.imshow(wordcloud, template='seaborn', title='WordCloud of Etsy.com Reviews')
    fig_wordcloud.update_layout(margin=dict(l=20, r=20, t=60, b=20), title_font_size=26, title_font_family='Playfair Display', hovermode=False)
    fig_wordcloud.update_xaxes(visible=False)
    fig_wordcloud.update_yaxes(visible=False)
    
    return fig_wordcloud
#----------------------------------------------- Defining main function ----------------------------------------
def main():
    print('Starting the project...')
    load_model()

    global app
    app.title = 'Sentiment Analysis With Insights.'
    app.layout = create_app_ui()

    Timer(1, open_browser).start()
    app.run_server(port=8050)

    app = None
    project_name = None

    print('Ending the project.')

#-------------------------------------------- Calling main function --------------------------------------------
if __name__ == '__main__':
    main()
