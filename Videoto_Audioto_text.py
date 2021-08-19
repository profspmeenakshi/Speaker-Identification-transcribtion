from pydub import AudioSegment
import speech_recognition as sr

recognizer=sr.Recognizer()
recognizer.energy_threshold=300
#fp="C:/Users/Admin/Documents/Win20-21/CSE3020_Lab/Recording_1.wav"
fp="C:/Users/Admin/Documents/Win20-21/CSE3020_Lab/sampl4.wav"
#fp="C:/Users/Admin/Documents/Win20-21/CSE3020_Lab/Test_Record_1.wav"
#Convert wav file to audio file
audio_file_=sr.AudioFile(fp)
print(type(audio_file_))

#Convert Audio file to audio data
with audio_file_ as source:
    recognizer.adjust_for_ambient_noise(source,duration=0.5)
    audio_file=recognizer.record(source)
    #result=recognizer.recognize_google(audio_data=audio_file,language="en-IN")
    try:
        print("Speech Recognition recognize_google api is enabled")
        result = recognizer.recognize_google(audio_file, language="en-IN")
        print("Your class discussion : " + result)
    except sr.UnknownValueError:
        print("Google speech recognition software could not able to understand the audio")
    except sr.RequestError as e:
        print("Could not request google speech recognition service {0}".format(e))

print(type(audio_file))
print(result)