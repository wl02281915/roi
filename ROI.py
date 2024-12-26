from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/roi')
def roi():
    return render_template('canvas.html')

@app.route('/pygetROIpoints', methods=['POST'])
def pygetROIpoints():
    ROIpoints = request.json.get('ROIpoints')
    print(ROIpoints)
    return ROIpoints

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)
