from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/poke', methods=['GET', 'POST'])
def poke():
    if request.method == 'POST':
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        if response.ok:
            if not response.json():
                 return "ERROR"
            data = response.json()
            new_data=[]
            pokemon_name = data['name']
            pokemon_dict={}
            pokemon_dict= {
                'name':data['name'],
                'ability_name': data['ability_name'],
                'base_experience': data['base_experience'],
                'sprite_front_shiny': data['sprite_front_shiny']
                }
            new_data.append(pokemon_dict)
            return new_data
            return render_template('poke.html', names=new_data)     
        else:
            return "connection error message ? "
    return render_template('poke.html')


    