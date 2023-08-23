from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_words = request.form.get('input_text').split()

    if input_words:
        timestamp = f"2023-{str(random.randint(1, 12)).zfill(2)}-{str(random.randint(1, 28)).zfill(2)} " \
                    f"{str(random.randint(1, 24)).zfill(2)}:{str(random.randint(1, 59)).zfill(2)}:" \
                    f"{str(random.randint(1, 59)).zfill(2)}"
        num_words = min(len(input_words), random.randint(10, 30))
        selected_words = random.sample(input_words, num_words)
        combination = ''.join(selected_words)
        result = f'生成的错误日志:\n{timestamp}\n===================\n{combination}'
    else:
        result = '请输入词语'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
