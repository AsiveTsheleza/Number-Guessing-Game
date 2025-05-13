from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number_to_guess' not in session:
        session['number_to_guess'] = random.randint(1, 100)
        session['attempts'] = 0
        session['max_attempts'] = 10

    message = ''
    game_over = False

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
        except ValueError:
            message = "Invalid input! Please enter a number."
        else:
            session['attempts'] += 1
            if guess < session['number_to_guess']:
                message = "Too low!"
            elif guess > session['number_to_guess']:
                message = "Too high!"
            else:
                message = f"Congratulations! You guessed it in {session['attempts']} attempts."
                game_over = True

            if session['attempts'] >= session['max_attempts'] and not game_over:
                message = f"Game Over! The number was {session['number_to_guess']}."
                game_over = True

    if game_over:
        session.clear()  # Reset all session variables after the game ends
    
    return render_template(
        'index.html',
        message=message,
        attempts=session.get('attempts', 0),
        max_attempts=session.get('max_attempts', 10),
        game_over=game_over
    )

@app.route('/reset')
def reset():
    session.clear()  # Reset the session for a new game
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
