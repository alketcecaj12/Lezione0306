from flask import Flask, request
import pickle
import numpy as np

# caricao il modello 
with open("modelli/modello_class.pkl", "rb") as model_file: 
     model = pickle.load(model_file)


# creo l'applicazione Flask 
app = Flask(__name__)


@app.route("/previsione/diabete/")
def predict_diabetes():
    input_p = request.args.get("p")
    int_input_p = int(input_p)
    
    input_g = request.args.get("g")
    int_input_g = int(input_g)
    
    input_b = request.args.get("b")
    int_input_b = int(input_b)
    
    arr_input = np.array([int_input_p, int_input_g, int_input_b]).reshape(1, -1)
    previsione = model.predict(arr_input)
    previsione = int(previsione)

    return str("<h1>previsione test diabete = "+str(previsione)+"</h1>")
    
    
    
if __name__ == "__main__":
    app.run()    
