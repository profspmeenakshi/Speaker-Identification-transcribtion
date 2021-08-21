# Speaker-Identification-transcription
We shall see how to convert a video file to text using python. This can be achieved just with 30th lines of code with the help of python package called moviepy and SpeechRecognition.
# Installation
This python library can be easily installed using pip as follows.                                                                                                                     1)pip install SpeechRecognition                                                                                                                                                     2)pip install moviepy
# How it works?
Moviepy import the editor module from the moviepy library.
We will pass the video file to the VideoFileClip method from the editor module
It will call the audio method from the video object.
It will write the audio to a new file 
then import the recognition module from the SpeechRecognition library.
It will pass the audio file to the AudioFile method from the recognition module.
It will create a .txt file in a write mode according to file name we given. It will the call source from the audio file use for loop it continues this process till end of the input given by user 
