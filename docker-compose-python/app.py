import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/')
def index():
    count = cache.get('hits')
    return 'You are get: {} times.\n'.format(count)

@app.route('/incr')
def incr():
    count = cache.incr('hits')
    return 'You are incr: {} times.\n'.format(count)

@app.route('/decr')
def decr():
    count = cache.decr('hits')
    return 'You are decr: {} times.\n'.format(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)