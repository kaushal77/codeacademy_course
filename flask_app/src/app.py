from flask import Flask
app = Flask(__name__)
from data import pets

@app.route('/')
def index():
  return f'''<h1>Adopt a Pet!</h1>
             <p>Browse through the links below to find your new furry friend:</p>
             <ul>
             <li><a href="/animals/dogs" >Dogs</a></li>
             <li><a href="/animals/cats" >Cats</a></li>
             <li><a href="/animals/rabbits" >Rabbits</a></li>
             </ul>'''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  val = pets[pet_type]
  html = f'<h1>List of {pet_type}</h1>'
  html = html + '<ul>'
  for key,i in enumerate(val):
    html = html+f'<li><a href="/animals/{pet_type}/{key}" >{i["name"]}</a></li>'
  html = html+' </ul>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type,pet_id):
    value = pets[pet_type]
    pet = value[pet_id]
    return f'''<h1>{pet["name"]}</h1>
    <img src = "{pet["url"]}"/>
    <p>Desc:- {pet["description"]}</p>
     <p>Breed:- {pet["breed"]}</p>
      <p>Age:- {pet["age"]}</p>'''


if __name__ == "__main__" :
    app.run(host='0.0.0.0')   