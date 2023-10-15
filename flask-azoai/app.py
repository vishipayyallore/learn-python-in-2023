import os
import openai
from flask import Flask, request, render_template

# Load config values
from dotenv import dotenv_values
config_details = dotenv_values(".env")

openai.api_type = "azure"
openai.api_base = config_details['OPENAI_API_BASE']
openai.api_version = config_details['OPENAI_API_VERSION']
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/get")
def get_completion_response():
    userText = request.args.get('msg')
    print("User Text: ", userText)
    user_prompt = "Tell me a joke on software engineering.\n\n"

    print('Azure Open AI Key: ', openai.api_key)

    try:
        response = openai.Completion.create(
            engine=config_details['COMPLETIONS_MODEL'],
            prompt=user_prompt,
            temperature=1,
            max_tokens=150,
            top_p=0.5,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)

        answer = response.choices[0].text
        return str(answer)
    except:
        print("An exception has occurred. \n")
        # print("Error Message:", response)


if __name__ == "__main__":
    app.run()
