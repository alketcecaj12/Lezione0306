from flask import Flask, request
import pickle
import numpy as np

# caricao il modello 
with open("modelli/modello_rl.pkl", "rb") as model_file: 
     model = pickle.load(model_file)


# creo l'applicazione Flask 
app = Flask(__name__)


@app.route("/previsione/ombrelli/")
def predict_sales():
    input_x = request.args.get("x")
    int_input_x = int(input_x)
    
    pioggia = np.array([int_input_x]).reshape(1, -1)
    previsione = model.predict(pioggia)
    previsione = int(previsione)

    return str("<h1>previsione di ombrelli venduti = "+str(previsione)+"</h1>")
    
    
    
if __name__ == "__main__":
    app.run()    
