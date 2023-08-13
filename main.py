from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_fact">View a random fact!</a> <a href="/coinflip">Flip a coin!</a>'
@app.route("/random_fact")
def fact():
    facts_list = ["Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.", "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan"]
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coinflip")
def ask():
    return'<a href="/coin">Flip!</a>'

@app.route("/coin")

def run():
    flip = ["Head","Back"]
    return f'<p>{random.choice(flip)}</p> <a href="/coin">Flip!</a>'
app.run(debug=False)
 
