# Connect Từ - Vietnamese Word Connection Web App
Connect Từ is a Vietnamese word connection game that produces a meaningful phrase whose first word is the last word of the player's input. The game ends when either the player or the computer cannot find a meaningful phrase to connect.

We utilized Natural Language Processing by training a bigram language model on 20,000,000+ Vietnamese sentences reinforced by a beam search technique to generate meaningful phrases. Besides, we used the following languages and tools to develop the web app: Python, React, Flask, HTML, CSS, and JavaScript.

# How to Install and Run the Game
After cloning the project, run these lines to run the game:

<b>For MacOS:</b>
```
pip install flask
cd src/backend
export FLASK_APP=transfer.py
flask run
```
<i>Open a new terminal here.</i>
```
cd src/frontend
npm start
```
<b>For Windows:</b>
```
pip install flask
cd src\backend
export FLASK_APP=transfer.py
flask run
```
<i>Open a new terminal here.</i>
```
cd src\frontend
npm start
```
To turn off the game, hit Ctrl + C on both 
