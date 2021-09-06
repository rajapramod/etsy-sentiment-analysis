import pandas as pd

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer



pickle_model = None
vocab = None
df = pd.read_csv('data/etsyReviews.csv')

def load_model():

    global pickle_model
    file = open('data/pickle_model.pkl', 'rb')
    pickle_model = pickle.load(file)
    
    # Loading the vocabulary
    global vocab
    file = open('data/features.pkl', 'rb')
    vocab = pickle.load(file)


def check_review(review):
    
    load_model()
    
    # Recreating the vectorizer
    loaded_vec = CountVectorizer(decode_error='replace', vocabulary=vocab)
    
    # Defining transformer
    transformer = TfidfTransformer()
    vectorized_review = transformer.fit_transform(loaded_vec.fit_transform([review]))

    result = pickle_model.predict(vectorized_review)
    return result


def create_layout(app):

	layout = html.Div([

			html.Div([

				html.H4('Pick a review from the dropdown to find out its sentiment.', className='sub-heading'),

				html.Br(),

				dcc.Dropdown(id='review-dropdown',
		             options=[{'label':x, 'value':x} for x in df['Reviews'].sample(50).values],
		             optionHeight=100, 
		             value='Select a review...',
		             multi=False,
		             clearable=False,
		             placeholder='Select a review...',
	            ),

	            html.Br(),

	            dbc.Button(
	                children='Find Sentiment',
	                id='dropdown-click-button',
	                color='info',
	                n_clicks=0,
	                className='ml-4 btn-info'
		        ),

		        html.Div([html.Br(), html.Strong(id='dropdown-review-result', children=None)]), 

		    ], id='dropdown-div'),

	        html.Div([

		        html.H4(id='text-area-title', children='Enter your review here to find out its sentiment.', className='sub-heading'),
		        
		        dcc.Textarea(
		                id='text-area-box',
		                placeholder='Enter your review here...',
		                className='textarea'
		            ),
		            
	            html.Br(),
	        
	            dbc.Button(
	                children='Find Sentiment',
	                id='textarea-click-button',
	                color='info',
	                n_clicks=0,
	                className='ml-4 btn-info'
	            ),
	            
	            html.Br(),
	        
	            html.Div([html.Br(), html.Strong(id='review-result', children=None)])

			], id='find-review-section-div')

		], id='check-review-inner-div')

	return layout
