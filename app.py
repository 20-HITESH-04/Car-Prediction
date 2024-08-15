import pickle
from flask import Flask , render_template , request

app = Flask(__name__)
with open('car_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict(): 
    year = int(request.form.get('Year'))
    p_price = float(request.form.get('Present_Price'))
    km_driven = int(request.form.get('Kms_Driven'))
    owner = int(request.form.get('Owner'))
    fuel_type = request.form.get('Fuel_Type')
    seller_type = request.form.get('Seller_Type')
    transmission = request.form.get('Transmission')

    if fuel_type == 'Petrol':
        fuel_type_numeric = 0
    elif fuel_type == 'Diesel':
        fuel_type_numeric = 1
    elif fuel_type == 'CNG':
        fuel_type_numeric = 2
    else:
        fuel_type_numeric = None 

    seller_type_numeric = 0 if seller_type == 'Dealer' else 1  # Assuming Individual = 1

    transmission_numeric = 0 if transmission == 'Manual' else 1  # Assuming Automatic = 1

    inputt = [[year, p_price, km_driven, fuel_type_numeric, seller_type_numeric, transmission_numeric, owner]]
    prediction = loaded_model.predict(inputt)
    output = round(prediction[0],2)
    print(output)

    return render_template('predict.html',predicted_price=output)

if __name__ == '__main__' :
    app.run(debug=True)
