from flask import Flask, request, render_template

app = Flask(__name__)

#Press Ctrl + C to exit



@app.route('/', methods=["GET", "POST"])
def home():
    
    return render_template('index.html')

@app.route('/Option1.html', methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return render_template('index2.html', content=first_name + '' + last_name)
    return render_template('Option1.html')

@app.route('/Option2.html')
def quiz():
    return render_template('Option2.html')

if __name__ == "__main__":
    app.run(debug=True)