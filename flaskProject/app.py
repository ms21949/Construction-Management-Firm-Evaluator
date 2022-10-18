from flask import Flask, render_template
import pickle
import numpy as np
import sklearn
from flask import request

model = pickle.load(open('model1.pkl','rb'))
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_Investment():
    Rank = int(request.form.get('Rank_2019'))
    Revenue = float(request.form.get('Total_2018_Revenue($ MILL.)'))

    result = model.predict(np.array([Rank,Revenue]).reshape(1,2))

    if result[0] == 1:
        result = 'You should consider investing'
    else:
        result = 'It is probably not worth investing'

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
