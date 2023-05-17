import dash 
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import random

with open("qrep.txt","r") as file:
     quest = file.read().splitlines()

#Création de l'interface interactive

app = dash.Dash(__name__)


#Mise en page 

app.layout = html.Div(
          children = [
                       html.H1("Bonjour à toi !"),
                       html.Button("Generate new question", id="generate-button"),
                       html.H3(id="quest"),
                       dcc.Input(id="answer-input",type= "text", placeholder="Votre réponse"),
                       html.Div(id="reponse"),
                     ]
                     )


def generate_question():
  return random.choice(quest)


@app.callback(
     Output("quest","children"),
     [Input("generate-button", "n_clicks")]
              )

def update_question(n_clicks):
   if n_clicks: 
      return generate_questions()

   else:
      return " "

@app.callback(
     Output("response","children"),
     [Input("answer-input","value")]
              )

def display_response(value):
   if value:
       return html.H4(f"Votre réponse: {value}")
   else:
       return  ""



#Lancer le serveur 

if __name__ == '__main__' :
    app.run_server(host = "0.0.0.0", port = 8050, debug = True)
 
