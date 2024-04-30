#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech for 10 seconds and print it
def recognize_speech():
    with sr.Microphone() as source:
        print("Say something for 10 seconds...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source, timeout=10)  # Listen for 10 seconds

        try:
            # Recognize the speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the function to recognize speech
recognize_speech()


# In[ ]:


import speech_recognition as sr
from googletrans import Translator

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech for 10 seconds and translate it into Telugu
def recognize_and_translate():
    with sr.Microphone() as source:
        print("Say something for 30 seconds...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source, timeout=30)  # Listen for 10 seconds

        try:
            # Recognize the speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            
            # Translate the recognized text into Telugu
            translator = Translator()
            translated_text = translator.translate(text, src='en', dest='te').text
            print("Translated text (Telugu):", translated_text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except Exception as e:
            print("Error:", e)

# Call the function to recognize speech and translate it into Telugu
recognize_and_translate()


# In[ ]:


import tkinter as tk
import speech_recognition as sr
from googletrans import Translator

class SpeechToTextGUI:
    def __init__(self, master):
        self.master = master
        master.title("Speech to Text Translator")

        self.label = tk.Label(master, text="Click 'Start Recording' and speak...")
        self.label.pack()

        self.translated_text_label = tk.Label(master, text="")
        self.translated_text_label.pack()

        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

    def start_recording(self):
        recognizer = sr.Recognizer()
        translator = Translator()

        with sr.Microphone() as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source, timeout=30)

            try:
                text = recognizer.recognize_google(audio_data)
                print("You said:", text)

                translated_text = translator.translate(text, src='en', dest='te').text
                print("Translated text (Telugu):", translated_text)

                self.translated_text_label.config(text=f"English: {text}\nTelugu: {translated_text}")
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
                self.translated_text_label.config(text="Sorry, I couldn't understand what you said.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                self.translated_text_label.config(text="Error accessing Google Speech Recognition service.")
            except Exception as e:
                print("Error:", e)
                self.translated_text_label.config(text="An error occurred.")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = SpeechToTextGUI(root)
    root.mainloop()


# In[ ]:


import tkinter as tk
import speech_recognition as sr
from googletrans import Translator

class SpeechToTextGUI:
    def __init__(self, master):
        self.master = master
        master.title("Speech to Text Translator")
        master.geometry("800x800")

        self.label = tk.Label(master, text="Click 'Start Recording' to speak...")
        self.label.pack()

        self.translated_text_label = tk.Label(master, text="")
        self.translated_text_label.pack()

        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_app)
        self.quit_button.pack()

        self.recording = False

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        recognizer = sr.Recognizer()
        translator = Translator()

        while self.recording:
            with sr.Microphone() as source:
                print("Say something...")
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio_data)
                    print("You said:", text)

                    translated_text = translator.translate(text, src='en', dest='te').text
                    print("Translated text (Telugu):", translated_text)

                    self.translated_text_label.config(text=f"English: {text}\nTelugu: {translated_text}")
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand what you said.")
                    self.translated_text_label.config(text="Sorry, I couldn't understand what you said.")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    self.translated_text_label.config(text="Error accessing Google Speech Recognition service.")
                except Exception as e:
                    print("Error:", e)
                    self.translated_text_label.config(text="An error occurred.")

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def stop_recording(self):
        self.recording = False

    def quit_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = SpeechToTextGUI(root)
    root.mainloop()


# In[ ]:


CHECKPOINT


# In[4]:


import tkinter as tk
import speech_recognition as sr
from googletrans import Translator

class SpeechToTextGUI:
    def __init__(self, master):
        self.master = master
        master.title("Speech to Text Translator")
        master.geometry("800x800")

        self.label = tk.Label(master, text="Click 'Start Recording' to speak...")
        self.label.pack()

        self.translated_text_label = tk.Label(master, text="")
        self.translated_text_label.pack()

        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.NORMAL)
        self.stop_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_app)
        self.quit_button.pack()

        self.recording = False
        self.translated_text = ""

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.label.config(text="Recording Started...")
        self.translated_text = ""  # Clear previous recordings
        self.listen_and_translate()

    def listen_and_translate(self):
        recognizer = sr.Recognizer()
        translator = Translator()

        if self.recording:
            with sr.Microphone() as source:
                print("Say something...")
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio_data)
                    print("You said:", text)

                    translated_text = translator.translate(text, src='en', dest='te').text
                    print("Translated text (Telugu):", translated_text)

                    self.translated_text += f"English: {text}\nTelugu: {translated_text}\n\n"
                    self.translated_text_label.config(text=self.translated_text)
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand what you said.")
                except sr.RequestError as e:
                    print("Could not connect to internet; {0}".format(e))
                except Exception as e:
                    print("Error:", e)

        if self.recording:
            self.master.after(50, self.listen_and_translate)  # Call the function again after 100 milliseconds

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.label.config(text="Recording Stopped...")

    def quit_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = SpeechToTextGUI(root)
    root.mainloop()


# In[6]:


get_ipython().system('pip install textblob')


# In[8]:


import tkinter as tk
import speech_recognition as sr
from googletrans import Translator
from textblob import TextBlob

class SpeechToTextGUI:
    def __init__(self, master):
        self.master = master
        master.title("Speech to Text Translator")
        master.geometry("800x800")

        self.label = tk.Label(master, text="Click 'Start Recording' to speak...")
        self.label.pack()

        self.translated_text_label = tk.Label(master, text="")
        self.translated_text_label.pack()

        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.NORMAL)
        self.stop_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_app)
        self.quit_button.pack()

        self.recording = False
        self.translated_text = ""
        self.english_text_list = []

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.label.config(text="Recording Started...")
        self.translated_text = ""  # Clear previous recordings
        self.english_text_list = [] 
        self.listen_and_translate()

    def listen_and_translate(self):
        recognizer = sr.Recognizer()
        translator = Translator()

        if self.recording:
            with sr.Microphone() as source:
                print("Say something...")
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio_data)
                    print("You said:", text)
                    self.english_text_list.append(text)

                    translated_text = translator.translate(text, src='en', dest='te').text
                    print("Translated text (Telugu):", translated_text)

                    self.translated_text += f"English: {text}\nTelugu: {translated_text}\n\n"
                    self.translated_text_label.config(text=self.translated_text)
                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand what you said.")
                except sr.RequestError as e:
                    print("Could not connect to internet; {0}".format(e))
                except Exception as e:
                    print("Error:", e)

        if self.recording:
            self.master.after(50, self.listen_and_translate)  # Call the function again after 100 milliseconds

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.label.config(text="Recording Stopped...")
        self.analyze_and_display_sentiment()

    def analyze_and_display_sentiment(self):
        # Joining English text list into a single string
        text = " ".join(self.english_text_list)
        
        # Analyzing sentiment
        sentiment = self.analyze_sentiment(text)
        
        # Displaying sentiment
        self.translated_text_label.config(text=f"Sentiment: {sentiment}")

    def analyze_sentiment(self, text):
        analysis = TextBlob(text)
    
        # Determine polarity (-1 to 1, negative to positive sentiment)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

    def quit_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = SpeechToTextGUI(root)
    root.mainloop()


# In[ ]:




