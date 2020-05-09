#!/usr/bin/env python3

HOST='0.0.0.0'
PORT=80
DEBUG_PORT=8099

import os
import json
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main_content.html')

if __name__ == "__main__":
    if 'DEBUG' not in os.environ:
        app.run(host=HOST, port=PORT, debug=False)
    else:
        app.run(host=HOST, port=DEBUG_PORT, debug=True)
