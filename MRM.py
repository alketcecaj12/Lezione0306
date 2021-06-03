from flask import Flask, request
import pickle
import numpy as np

# caricao il modello 
with open("modelli/modello_migliore.pkl", "rb") as model_file: 
     model = pickle.load(model_file)


# creo l'applicazione Flask 
app = Flask(__name__)

@app.route("/previsione/vendite/")
def predict_sales():
    input_t = int(request.args.get("t"))
    input_r = int(request.args.get("r"))
    input_g = int(request.args.get("g"))
    
    values = np.array([input_t, input_r, input_g]).reshape(1, -1)
    
    previsione = int(model.predict(values))
    
    return str("<h2> Ecco la previsione delle vendite in seguito alla capmagna pub! "+str(previsione))
    
    
if __name__ == "__main__":
    app.run()    
    
    
    
    
