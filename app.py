from flask import Flask, render_template, request, jsonify
import time

# Import computation functions
from logic.single_thread import compute_single_thread
from logic.multithread import compute_multithread
from logic.multiprocessing_impl import compute_multiprocessing
from logic.single_processor import compute_single_processor

app = Flask(__name__)

METHODS = {
    'single-thread': compute_single_thread,
    'multithread': compute_multithread,
    'multiprocessing': compute_multiprocessing,
    'single-processor': compute_single_processor,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    elapsed = None
    j_value = None
    method = None

    if request.method == 'POST':
        # Parse form inputs
        j_value = int(request.form.get('j', 0))
        method = request.form.get('method')

        # Validate
        if method in METHODS and j_value > 0:
            compute_fn = METHODS[method]
            start = time.perf_counter()
            result = compute_fn(j_value)
            end = time.perf_counter()
            elapsed = end - start
        else:
            result = 'Invalid input'

    return render_template('index.html', result=result, elapsed=elapsed, j=j_value, method=method, methods=METHODS.keys())

@app.route('/api/compute', methods=['POST'])
def api_compute():
    data = request.get_json() or {}
    j_value = data.get('j')
    method = data.get('method')

    if not isinstance(j_value, int) or method not in METHODS:
        return jsonify({'error': 'Invalid parameters'}), 400

    compute_fn = METHODS[method]
    start = time.perf_counter()
    result = compute_fn(j_value)
    elapsed = time.perf_counter() - start

    return jsonify({'result': result, 'elapsed': elapsed})

if __name__ == '__main__':
    app.run(debug=True)
