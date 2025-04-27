from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from src.demo_001_langchain import get_user_info


load_dotenv()

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = get_user_info(name)
    return jsonify({"summary": summary.to_dict(), "photoUrl": profile_pic_url})


if __name__ == "__main__":
    app.run(debug=True)
