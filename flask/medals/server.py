from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/getData', methods=['GET'])
def getData():
    medals = []
    with open('data.csv', 'r') as file:
        for line in file.readlines():
            medals.append(line.strip().split(','))
    return jsonify({"medals": medals})


if __name__ == '__main__':
    app.run(debug=True)