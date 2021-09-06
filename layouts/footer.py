import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def create_layout(app):
	return html.Div([
			
			html.Div([
				
				html.P(html.H5('Designed by Raja Pramod K J')),

				html.P([
					html.P(['as a part of internship project at ', html.A('Forsk Technologies', href='https://www.forskcodingschool.com/', target='_blank')]),
					html.P(['using ', html.A('Plotly Dash', href='https://www.plotly.com/', target='_blank'), '. Web Fonts from ', html.A('Google', href='https://fonts.google.com', target='_blank'), '.'])
					]),

				html.Br(),

				dbc.Button("Github", href='https://github.com/rajapramod/', target='_blank', color='info', className='mr-2 ml-2'),
				dbc.Button("LinkedIn", href='https://in.linkedin.com/in/raja-pramod-k-j/', target='_blank', color='info'),


			], id='footer-text-div', className='footer-content'),
			
			html.Div([html.P(html.A(html.H5('Navigate to Top'), href='#top'))], id='nav-div', className='footer-content')

			
		], id='footer-contact')