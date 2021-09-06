import dash_html_components as html
import dash_bootstrap_components as dbc

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
GITHUB_LOGO = 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'


def create_layout(app):
    return html.Div([

        html.Div([
            dbc.Navbar([

                dbc.Row([
                    html.A(dbc.Row(dbc.Col(html.Img(src=PLOTLY_LOGO, id='plotly-logo-img')), align="center"), 
                    href="https://plotly.com", target='_blank')], align="center", no_gutters=True, style={'margin-right':'auto'}),

                html.Ul([

                    html.Li(html.A('Home', href='#top', className='nav-link', id='home-button'), className='nav-item mr-3'),
                    html.Li(html.A('Pie Chart Analysis', href='#piechart', className='nav-link', id='piechart-button'), className='nav-item mr-3'),
                    html.Li(html.A('Check Your Review', href='#check-review', className='nav-link', id='check-review-button'), className='nav-item mr-3'),
                    html.Li(html.A('WordCloud & Bar Graph', href='#wordcloud', className='nav-link', id='wc-button'), className='nav-item mr-3'),
                    html.Li(html.A('Contact', href='#footer-contact', className='nav-link', id='contact-button'), className='nav-item'),
                        
                    ], id='menubar-container'),


                html.A(html.Img(src=GITHUB_LOGO, id='github-logo-img', alt='GitHub-Link'), 
                            target='_blank', href='https://github.com/rajapramod/etsy-sentiment-analysis.git', style={'margin-left':'auto'}),

            ], fixed='top', color='info', className='navbar-container'),
                     ], id='header-container'),

    ])
    return header_layout
