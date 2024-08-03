from flask import Flask, request, render_template
from diabetes_prediction import DiabetesPredictor
from heart_attack_prediction import HeartAttackPredictor

app = Flask(__name__)

#Press Ctrl + C to exit



@app.route('/', methods=["GET", "POST"])
def home():
    
    return render_template("index.html")

@app.route("/Option1.html", methods=["GET", "POST"])
def calculator():
    '''if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return render_template('index2.html', content=first_name + '' + last_name)'''
    
    if request.method == "POST":
        pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age = request.form["pregnancies"], request.form["glucose"], request.form["bloodpressure"], request.form["skinthickness"], request.form["insulin"], request.form["bmi"], request.form["diabetespedigreefunction"], request.form["age"]
        predictor = DiabetesPredictor()
        prediction = predictor.has_diabetes([pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age])
        statement = "You are at risk of diabetes." if prediction else "You are not at risk of diabetes."

    return render_template("Option1.html", statement=statement)

@app.route("/Option2.html")
def quiz():
    return render_template("Option2.html")

if __name__ == "__main__":
    app.run(debug=True)