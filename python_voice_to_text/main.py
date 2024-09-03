import speech_recognition as sr
import json
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox


r = sr.Recognizer()

def openJson():
    with open('sware.json') as json_file:
        data = json.load(json_file)
        return data

def drawMessageBox(sware_count):
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(f"You swore {sware_count} times.")
    msg.setWindowTitle("Swear Word Counter")
    msg.exec_()


def openMic():
    try:
        with sr.Microphone() as source:
            data = openJson()

            print("Speak Anything :")
            audio = r.listen(source)
            try:
                swareCounter = 0
                text = r.recognize_google(audio)
                for sware in data['words']:
                    if sware in text:
                        swareCounter += 1
                
                totalScore(swareCounter)
                drawMessageBox(swareCounter)
                
            except sr.UnknownValueError:
                print("Sorry, could not understand the audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
    except OSError as e:
        print("Could not access the microphone; {0}".format(e))

def totalScore(count):
    with open('score.json', 'r') as file:
        data = json.load(file)
    
    data['score'] = count
    
    with open('score.json', 'w') as file:
        json.dump(data, file)

openMic()


