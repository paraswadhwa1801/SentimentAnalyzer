# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:35:28 2017

@author: lenovo
"""
import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from flask import Flask, render_template
app = Flask(__name__)
 

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/my-link/')
def my_link():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    with open("speech data.txt","r+") as myfile:
        myfile.truncate()
        myfile.write(r.recognize_google(audio))
        
    analyzer=SentimentIntensityAnalyzer()
    f=open('speech data.txt','r')
    for sentence in f:
        vs=analyzer.polarity_scores(sentence)

    a="{:-<100} {}".format(sentence,str(vs))
    return render_template('output2.html',value=a)


if __name__ == '__main__':
  app.run(debug=True)