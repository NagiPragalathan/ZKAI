import datetime  # Import the datetime module
import speech_recognition as sr
import pyaudio
import os
import wave
from .Ai_Modules.Emotion import classify_emotion_efficient, find_unwanted_words, find_unwanted_words_bool
from django.conf import settings
import os

def record_audio(stream, filename):
    chunk = 4096  # Larger chunk size for faster recording
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 16000  # Lower sample rate for faster processing
    seconds = 10
    frames = []

    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


def convert_audio(i):
    if i >= 0:
        sound = 'record.wav'
        r = sr.Recognizer()

        while not os.path.exists(sound):
            pass  # Wait until the recording is complete

        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            print(f"Converting Audio To Text and saving to file...")
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio)
            try:
                os.remove(sound)
            except:
                print("Error from 'os' trying to remove the created Audio file")
            print("writing...")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
            Text_file = os.path.join(settings.BASE_DIR, 'base', 'generated_files', 'converted_text.txt')
            print(Text_file)
            with open(Text_file, "a") as f:
                if value and value != " " and value != "":
                    f.write(f"[{timestamp}], {find_unwanted_words(value)}, {classify_emotion_efficient(value)}, {find_unwanted_words_bool(value)}\n")  # Write timestamp and value to file
                    print(value)
                else:
                    f.write(f"[{timestamp}] \n") 
        except sr.UnknownValueError:
            print("unknown..!")
        except sr.RequestError as e:
            print(e)
            

p = pyaudio.PyAudio()
chunk = 4096
sample_format = pyaudio.paInt16
channels = 2
fs = 16000
