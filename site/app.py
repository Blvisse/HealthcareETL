'''

Our dash front end site to input data

'''

try: 
    
    import dash
    import dash_html_components as html
    import dash_core_components as dcc
    from dash.dependencies import Input,Output,State
    import base64
    import time,json
    import uuid
    
    print("Loaded libraries")
    
    

except ImportError as ie:


    print(ie)
    print("Error importing {} ".format(ie.name))
    print("/n")
    print("To fix this we recommend running --pip install {} ".format(ie.name))
    exit(1)    
    
    
    
app=dash.Dash(__name__)


app.css.append_css({"external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"})

initialLayout =[
    
    
    html.Div([html.H3("Hospital Information System", style={"textAllign": "center"})]),
    html.Div (
        
        [
            
            html.Div([
                
                #creating the layout
                #First Column for Image
                html.Img(
                    
                    src="https://img.icons8.com/dotty/80/null/hospital-2.png",
                    style={
                        "height": "25%",
                        "width": "25%",
                        "margin": ".5px 150px",
                    },
                    
                    
                    
                )
                
            ],
            className="four columns",
            ),
            html.Div(
                [
                    #html.H3 ("column 2")
                    html.Br(),
                    dcc.Markdown("Hospital Id"),
                    dcc.Input(id="prod5", type="number", debounce=False, min=0,),
                    
                ],
                className="four columns",
            ),
        
        
        
    ],
        className="row"
        ),
        html.Div (
        
        [
            
            html.Div([
                
                #creating the layout
                #First Column for Image
                html.Img(
                    
                    src="https://img.icons8.com/dotty/80/null/hospital-2.png",
                    style={
                        "height": "25%",
                        "width": "25%",
                        "margin": ".5px 150px",
                    },
                    
                    
                    
                )
                
            ],
            className="four columns",
            ),
            html.Div(
                [
                    #html.H3 ("column 2")
                    html.Br(),
                    dcc.Markdown("column"),
                    dcc.Input(id="prod4", type="number", debounce=False, min=0,),
                    
                ],
                className="four columns",
            ),
        
        
        
    ],
        className="row"
        ),
        html.Div (
        
        [
            
            html.Div([
                
                #creating the layout
                #First Column for Image
                html.Img(
                    
                    src="assets/product.png",
                    style={
                        "height": "25%",
                        "width": "25%",
                        "margin": ".5px 150px",
                    },
                    
                    
                    
                )
                
            ],
            className="four columns",
            ),
            html.Div(
                [
                    #html.H3 ("column 2")
                    html.Br(),
                    dcc.Markdown("column"),
                    dcc.Input(id="prod3", type="number", debounce=False, min=0,),
                    
                ],
                className="four columns",
            ),
        
        
        
    ],
        className="row"
        ),
        html.Div (
        
        [
            
            html.Div([
                
                #creating the layout
                #First Column for Image
                html.Img(
                    
                    src="assets/product.png",
                    style={
                        "height": "25%",
                        "width": "25%",
                        "margin": ".5px 150px",
                    },
                    
                    
                    
                )
                
            ],
            className="four columns",
            ),
            html.Div(
                [
                    #html.H3 ("column 2")
                    html.Br(),
                    dcc.Markdown("column"),
                    dcc.Input(id="prod2", type="number", debounce=False, min=0,),
                    
                ],
                className="four columns",
            ),
        
        
        
    ],
        className="row"
        ),
        
    html.Div(
        [
            html.Button(
                "Submit",id="submit-val",n_clicks=0,style={"margin": "10px 700px"}
            ),
        ]
    ),
    
    html.Div([html.Br()]),
    html.Div(id="output")   
]



app.layout = html.Div(id="main-page", children=initialLayout)


if __name__ == "__main__":
    app.run_server(debug=False)