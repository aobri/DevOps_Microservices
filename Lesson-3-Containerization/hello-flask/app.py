# save this as app.py
from flask import Flask, request
from markupsafe import escape
from sensible.loginit import logger

log = logger(__name__)
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# if __name__ == '__main__':
#     log.info("START Flask")
#     app.debug = True
#     app.run(host='0.0.0.0')
#     log.info("SHUTDOWN Flask")