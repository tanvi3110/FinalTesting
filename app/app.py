from flask import Flask, Markup, render_template, make_response, request, jsonify
# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
)


@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
