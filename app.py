import os
from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['max_attempts'] = 10

    message = ""
    game_over = False

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess < session['number']:
            message = "Too low!"
        elif guess > session['number']:
            message = "Too high!"
        else:
            message = f"Correct! The number was {session['number']}."
            game_over = True

        if session['attempts'] >= session['max_attempts'] and not game_over:
            message = f"You've run out of attempts. The number was {session['number']}."
            game_over = True

    return render_template('index.html',
                           message=message,
                           game_over=game_over,
                           attempts=session.get('attempts', 0),
                           max_attempts=session.get('max_attempts', 10))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port)
