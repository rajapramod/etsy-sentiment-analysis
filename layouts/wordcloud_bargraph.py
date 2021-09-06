import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


# def bargraph():

# 	dff = pd.read_csv('data/words_frequency.csv', encoding='utf-8')
# 	print(dff.head())
# 	fig = px.bar(data_frame=dff, x='words', y='frequency',
# 		orientation='v')

# 	fig.update_layout(title='Bar Graph of Word Frequencies', title_font_size=26)
	
# 	return fig


def create_layout():
	return html.Div([

			html.Div([

				html.H4(id='subheading-bg-dd', children=['Pick the number of words to display on the graph from the dropdown below.'], className='sub-heading'),

				dcc.Dropdown(
						id='bargraph-dropdown',
						options=[{'label': x, 'value': x} for x in [25, 50, 100, 200, 500]],
						value=25,
						clearable=False,
						placeholder='Select the number of words to get the frequency...'
					),

				dcc.Graph(id='bar-chart', figure={}, config={'displayModeBar': False})

	        ]),


	        html.Div([

	        	html.Br(),

	        	html.H4(id='wordcloud-heading', children=['A WordCloud generated from the review data where word size in the wordcloud image\
	        	 corresponds to its frequency.'], className='sub-heading'),

	        	html.H5(id='wc-dd-instruction', children=['Select the number of words to display on the wordcloud here:']),

	        	dcc.Dropdown(
	        			id='wordcloud-dropdown',
	        			options=[{'label':x, 'value': x} for x in [25, 50, 100, 200, 500]],
	        			value=25,
	        			clearable=False,
	        			placeholder='Select the number of words to appear on the wordcloud below...'
	        	),

	        	html.Br(),

	        	dbc.Spinner(dcc.Graph(id='wordcloud-figure', figure={}), color='danger', type='grow'),

	        ], id='wordcloud-div')


	    ])
