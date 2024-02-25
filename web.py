from flask import Flask,request, render_template

from speech_to_text import ConvertAudioToText
from text_to_speech import SpeakText
from jarvis import jarvis
import os
import test



app = Flask(__name__,static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/',methods=["POST","GET"])

def home():
    if request.method=="POST":
        text=request.form["text"]
        print(text)
        


        '''
        filename = 'audio.wav'  # or generate a unique filename
        audio_path = os.path.join(os.path.dirname(__file__), filename)
        audio.save(audio_path)
        
        
        # import required libraries
        from pydub import AudioSegment 
        from pydub.playback import play 

# Import an audio file 
# Format parameter only
# for readability 
        wav_file = AudioSegment.from_file(file = audio, 
								format = "wav") 


        
        audio = test.convert_audio("audio.wav")

        
        text=ConvertAudioToText("audio.wav")'''


        jarvis_report=jarvis("AIzaSyC-7GISlhn3Il0Go72YhCHXnw1vn2lz-jg",text)
        speak=SpeakText(jarvis_report)
        return render_template("Index.html",jarvis_report=jarvis_report)





        

    return render_template("Index.html")




    

if __name__=="__main__":
    app.run(debug=True)