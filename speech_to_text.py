import speech_recognition as sr

# Function to convert speech from an audio file to text
def ConvertAudioToText(audio_file):
    # Initialize the recognizer 
    r = sr.Recognizer() 
    
    with sr.AudioFile(audio_file) as source:
        print("Reading audio file...")
        audio = r.record(source)  # Read the entire audio file
        
        print(audio)
        print("Recognizing...")
            # Using Google Speech Recognition
        text = r.recognize_google(audio)
        print("Transcribed text: ", text)
        return text
        

