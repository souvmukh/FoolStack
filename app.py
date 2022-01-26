from flask import Flask,render_template,jsonify,request
from flask_restful import Resource, Api
from makesound import MakeSound

#1. To Save your Sound 2. Exception Handling API

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('playmusic.html')

class Application(Resource):

    sounds = []
    
    def get(self,value):
        
        if (value == 'playback'):
            DURATION = 750
            sound = MakeSound()
            for note in self.sounds:
                sound.oneNote(note,DURATION)
            return "PLAY BACK ALL NOTES"
        
        if (value == 'clear'):
            print(len(self.sounds))
            self.sounds.clear()
        
        else:
            sound = MakeSound()
            self.sounds.append(value)
            return sound.oneNote(value)

        
api.add_resource(Application, '/scaleoctave/<string:value>')
app.run(port = 5000)