from flask import Flask
app = Flask(_name_)

@app.route('/')
def indec():
  return 'hello, world'
