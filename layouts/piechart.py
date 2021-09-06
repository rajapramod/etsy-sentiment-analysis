import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def piechart():
    dff = pd.read_csv('data/etsyReviews.csv')
    labels = ['Positive', 'Negative']
    values = [sum(dff['SentimentValue'] == 1), sum(dff['SentimentValue'] == 0)]
    fig = go.Figure({
            'data': [{'hoverinfo': 'label+value+text',
                      'hovertemplate': '%{label} reviews: %{value} <br>Percentage: %{percent}<extra></extra>',
                      'labels': ['Positive', 'Negative'],
                      'text': ['reviews', 'reviews', 'each'],
                      'textinfo': 'label+text+percent',
                      'textposition': 'outside',
                      'type': 'pie',
                      'values': [43769, 4277]}],
            'layout': {'showlegend': True,
                       'title': {'font': {'family': 'Playfair Display', 'size': 26}, 'pad': {'l': 115, 'b': 60}, 'text': 'Pie Chart'},
                       'width': 400, 'height': 400}
})

    return fig

def create_layout(app):

	layout = html.Div([

        html.Div([
            dcc.Graph(id="pie-chart", 
                      figure=piechart())
            ]),


		html.Div([
				html.H5('What does the Pie Chart tell us?', className='details_title'),
				html.P(
					['The sentiment analysis of ', html.Strong('53,197'), ' scraped reviews from the e-commerce website ', html.A('Etsy.com', href='https://www.etsy.com/', target='_blank', ) ,' shows that ',
					html.Strong('91.1%'), ' of the reviews, i.e., ', html.Strong('48,462'), ' reviews are of positive sentiment (with ratings 4 & 5) and ',
					html.Strong('8.9%'), ' of the rest, i.e., ', html.Strong('4,735'), ' are of negative sentiment (with ratings 1 & 2).'
					])
				], id='piechart-details-div')

	   ], id='piechart-sub-main-div')

	return layout