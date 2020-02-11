from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    return render_template('output.html')

@app.route('/output', methods=['GET','POST'])
def getvalue():
    if request.method =='POST':
        name = request.form['yo'].split(",")
        print(name)
    return render_template('output.html', n = name)

if __name__ == '__main__':
    app.run(debug=True)
