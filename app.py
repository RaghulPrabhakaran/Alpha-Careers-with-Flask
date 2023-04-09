from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data Analyst",
  'location': 'Chennai,India',
  'salary': 'Rs.5,00,000'
}, {
  'id': 2,
  'title': "Data Scientist",
  'location': 'Banglore,India',
  'salary': 'Rs.20,00,000'
}, {
  'id': 3,
  'title': "Full-Stack Engineer",
  'location': 'Remote',
  'salary': '$4,500'
}, {
  'id': 4,
  'title': "Network Engineer",
  'location': 'Coimabtore,India',
  'salary': 'Rs.15,00,000'
}]


@app.route("/")
def HelloWorld():
  return render_template('index.html', jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
