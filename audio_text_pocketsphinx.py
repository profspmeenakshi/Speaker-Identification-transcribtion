import speech_recognition as sr



r=sr.Recognizer()
r.energy_threshold=300

fp="C:/Users/Admin/Documents/Win20-21/CSE3020_Lab/Test_Record_1.wav"
#Convert wav file to audio file
audio_file_=sr.AudioFile(fp)
print(type(audio_file_))

#using microphone
#with sr.Microphone() as source:
# listen for 5 seconds and create ambient noise energy level
#    r.adjust_for_ambient_noise(source,duration=5)
#    print("Say something: ")
#    audio=r.listen(source,phrase_time_limit=5)

with audio_file_ as source:
# listen for 5 seconds and create ambient noise energy level
    r.adjust_for_ambient_noise(source,duration=5)
    audio_file=r.record(source)

#Recognize speech using sphinx
try:
    print("Sphinx thinks you said: ' " + r.recognize_sphinx(audio_file) + "'")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print(" Sphinx error; {0}".format(e))