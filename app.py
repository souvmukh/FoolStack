from flask import Flask,render_template,jsonify,request
from flask_restful import Resource, Api
from makesound import MakeSound

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('playmusic.html')

class Application(Resource):
    
    def get(self,value):    
        sound = MakeSound(value)
        return sound.getSound()
        
api.add_resource(Application, '/scaleoctave/<string:value>')
app.run(port = 5000)