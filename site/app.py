'''

Our dash front end site to input data

'''

try: 
    
    import dash
    from dash import html
    from dash  import dcc
    from dash.dependencies import Input,Output,State
    import dash_bootstrap_components as dbc
    import base64
    import time,json
    import uuid
    # from settings import config
    
    print("Loaded libraries")
    
    

except ImportError as ie:


    print(ie)
    print("Error importing {} ".format(ie.name))
    print("/n")
    print("To fix this we recommend running --pip install {} ".format(ie.name))
    exit(1)    
    
    
    

# app.title="Hospital Emergency Information System"
theme=dbc.themes.LUX

css = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'


#app Instance
app=dash.Dash(name="Hospital Emergency Information System",external_stylesheets=[dbc.themes.LUX])
app.title="H E I S"

####  Navbar  ####

#output
navbar=dbc.Nav(className="nab nav-pills",children=[
    
    ##logo
    dbc.NavItem(html.Img(src="https://img.icons8.com/dotty/80/null/hospital-2.png",height="40px")),
    ##about
    dbc.NavItem(html.Div([
        dbc.NavLink("About", href="/", id="about-this",active=False),
        dbc.Popover(id="about",is_open=False,target="about-this",children=[
            
            dbc.PopoverHeader("How it works"),
            dbc.PopoverBody("The text goes here")
        ])
    ])),
    
    ##links
    dbc.DropdownMenu(label="Links",nav=True,children=
                     [
                         dbc.DropdownMenuItem([
                             html.I(className="fa fa-linkedin"), " Contacts"
                         ], href="/",target="_blank"),
                         dbc.DropdownMenuItem([
                             html.I(className="fa fa-github"), " Contacts"
                         ], href="/",target="_blank"),
                     ])
])

#callbacks
@app.callback(output=[
        Output(component_id="about",component_property="is_open"),
        Output(component_id="about-popover", component_property="active"),
        
    ],
inputs=[
        Input(component_id="about-popover", component_property="n_clicks")
    ],
State=[
        
        State('about',"is_open"),State("about-popover","active")
    ])


def about_popover(n,is_open,active):
    if n:
        return not is_open,active
    return is_open,active


#### Body ####


#inputs
inputs =dbc.FormGroup([
    ###
    
    # html.Div(id="hide-seek",children=[
    #     dbc.Label("Hospital Id", html_for="hospital_id"),
    #     dbc.Input(id="max-capacity", placeholder="table capacity", type="number", value="10")
    # ])
    dbc.Label("Hospital Id", html_for="hospital_id"),
    dbc.Input(id="hospital_id", placeholder="table capacity", type="number", value="10"),
    
    html.Br(),
    
    dbc.Label("Hospital Type Code", html_for="Hospital_type_code"),
    dbc.Input(id="Hospital_type_code", placeholder="table capacity", type="number", value="10"),
   
    html.Br(),
    dbc.Label("Hospital Type Code", html_for="City_code"),
    dbc.Input(id="City_code", placeholder="City Code", type="text", value="10"),

    html.Br(),
    dbc.Label("Hospital Type Code", html_for="Hospital_regional_code"),
    dbc.Select(id="Hospital_regional_code",
               options=[
               
               
                {"label": "Option 1", "value": "1"},
                {"label": "Option 2", "value": "2"},
               
               
               ]),
    # dbc.Input(id="Hospital_regional_code", placeholder="table capacity", type="text", value="10"),

    html.Br(),
    
    dbc.Label("Available Extra Rooms in Hospital", html_for="Available_Room"),
    dbc.Input(id="Available_Room", placeholder="table capacity", type="number", value="10"),
   
   
    html.Br(),
    dbc.Label("Department Name", html_for="Department_code"),
    dbc.Select(id="Department_code",
               options=[
               
               
                {"label": "Option 1", "value": "1"},
                {"label": "Option 2", "value": "2"},
               
               
               ]),
    
    #Submit Button
    html.Br(),html.Br(),
    dbc.Col(dbc.Button("Submit", id="run", color="primary"))
    
])

#output
# no outputs
body=dbc.Row([
    ## input
    dbc.Col(md=5,
    children=[
        inputs,
        html.Br(),html.Br(),html.Br(),
        
    ]),
    dbc.Col(md=5,
    children=[
        inputs,
        html.Br(),html.Br(),html.Br(),
        
    ]),
    
    #second col
    dbc.Col(md=9, children=[
            dbc.Spinner([
                ### title
                html.H6(id="title")
                ### download
                # dbc.Badge(html.A('Download', id='download-excel', download="tables.xlsx", href="", target="_blank"), color="success", pill=True),
                ### plot
                # dcc.Graph(id="plot")
            ], color="primary", type="grow"), 
        ])
    
    
])
#callbacks
@app.callback(inputs=[Input(component_id="Submit", component_property="n_clicks")],
              state=[State("hospital_id","value"), State("Hospital_type_code","value"), State("City_code","value"), State("Hospital_regional_code","value"), State("Available_Room","value"),State("Department_code","value")
                     ])


def results(hospital_id, Hospital_type_code, City_code,  Hospital_regional_code, Available_Room,Department_code):

    return hospital_id, Hospital_type_code, City_code, Department_code, Hospital_regional_code, Available_Room,Department_code
    # return {'display':'block'} 

# def upload_event(filename):
#     div = "" if filename is None else "Use file "+filename
#     return {'display':'block'} if filename is None else {'display':'none'}, 






# @app.callback()
# def function():
#     return 0


#App Layout
app.layout=dbc.Container(fluid=True,children=[
    html.H1("Hospital Emergency Information System",id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    body
])

########################## Run ##########################
if __name__ == "__main__":
    app.run_server(debug=True)


# app.css.append_css({"external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"})

# initialLayout =[
    
    
#     html.Div([html.H3("Hospital Information System", style={"textAllign": "center"})]),
#     html.Div (
        
#         [
            
#             html.Div([
                
#                 #creating the layout
#                 #First Column for Image
#                 html.Img(
                    
#                     src="https://img.icons8.com/dotty/80/null/hospital-2.png",
#                     style={
#                         "height": "25%",
#                         "width": "25%",
#                         "margin": ".5px 150px",
#                     },
                    
                    
                    
#                 )
                
#             ],
#             className="four columns",
#             ),
#             html.Div(
#                 [
#                     #html.H3 ("column 2")
#                     html.Br(),
#                     dcc.Markdown("Hospital Id"),
#                     dcc.Input(id="prod5", type="number", debounce=False, min=0,),
                    
#                 ],
#                 className="four columns",
#             ),
        
        
        
#     ],
#         className="row"
#         ),
#         html.Div (
        
#         [
            
#             html.Div([
                
#                 #creating the layout
#                 #First Column for Image
#                 html.Img(
                    
#                     src="https://img.icons8.com/dotty/80/null/hospital-2.png",
#                     style={
#                         "height": "25%",
#                         "width": "25%",
#                         "margin": ".5px 150px",
#                     },
                    
                    
                    
#                 )
                
#             ],
#             className="four columns",
#             ),
#             html.Div(
#                 [
#                     #html.H3 ("column 2")
#                     html.Br(),
#                     dcc.Markdown("column"),
#                     dcc.Input(id="prod4", type="number", debounce=False, min=0,),
                    
#                 ],
#                 className="four columns",
#             ),
        
        
        
#     ],
#         className="row"
#         ),
#         html.Div (
        
#         [
            
#             html.Div([
                
#                 #creating the layout
#                 #First Column for Image
#                 html.Img(
                    
#                     src="assets/product.png",
#                     style={
#                         "height": "25%",
#                         "width": "25%",
#                         "margin": ".5px 150px",
#                     },
                    
                    
                    
#                 )
                
#             ],
#             className="four columns",
#             ),
#             html.Div(
#                 [
#                     #html.H3 ("column 2")
#                     html.Br(),
#                     dcc.Markdown("column"),
#                     dcc.Input(id="prod3", type="number", debounce=False, min=0,),
                    
#                 ],
#                 className="four columns",
#             ),
        
        
        
#     ],
#         className="row"
#         ),
#         html.Div (
        
#         [
            
#             html.Div([
                
#                 #creating the layout
#                 #First Column for Image
#                 html.Img(
                    
#                     src="assets/product.png",
#                     style={
#                         "height": "25%",
#                         "width": "25%",
#                         "margin": ".5px 150px",
#                     },
                    
                    
                    
#                 )
                
#             ],
#             className="four columns",
#             ),
#             html.Div(
#                 [
#                     #html.H3 ("column 2")
#                     html.Br(),
#                     dcc.Markdown("column"),
#                     dcc.Input(id="prod2", type="number", debounce=False, min=0,),
                    
#                 ],
#                 className="four columns",
#             ),
        
        
        
#     ],
#         className="row"
#         ),
        
#     html.Div(
#         [
#             html.Button(
#                 "Submit",id="submit-val",n_clicks=0,style={"margin": "10px 700px"}
#             ),
#         ]
#     ),
    
#     html.Div([html.Br()]),
#     html.Div(id="output")   
# ]



# app.layout = html.Div(id="main-page", children=initialLayout)


# if __name__ == "__main__":
#     app.run_server(debug=False)