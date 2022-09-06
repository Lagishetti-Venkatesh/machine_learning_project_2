

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "CI CD pipeline got created. No need of creating Docker images to upload the changes to the deployment"

if __name__ == "__main__":
    app.run(debug=True)