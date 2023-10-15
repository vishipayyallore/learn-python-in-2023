import os
from flask import Flask, request, render_template
import openai

openai.api_type = "azure"
openai.api_base = "https://azure-YOUR-dev-001.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.Completion.create(
        engine="gpt-35-turbo-dev-001",
        prompt=userText,
        temperature=1,
        max_tokens=150,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    answer = response.choices[0].text
    return str(answer)


if __name__ == "__main__":
    app.run()
