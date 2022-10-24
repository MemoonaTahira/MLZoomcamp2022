#### code for flask app whether a use is likely to apply for a credit card,  run from ubuntu terminal: #######

import pickle
from flask import Flask
from flask import request
from flask import jsonify


model_file = "model2.bin"
dv_file = "dv.bin"


with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)
    f_in.close()
    
with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)
    f_in.close()


app = Flask('credit_card')
@app.route('/predict', methods=['POST'])
def predict():
    
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    credit_bool = y_pred >= 0.5

    result = {
        'credit_card_prob': float(y_pred),
        'credit_bool': bool(credit_bool)
    }
    return jsonify(result)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=9000)



