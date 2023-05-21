from flask import Flask, render_template, request

app = Flask(__name__)

data = [
    {'id': 0, 'name': '中秋节', 'num': 0},
    {'id': 1, 'name': '春节', 'num': 0},
    {'id': 2, 'name': '端午节', 'num': 0}

]

@app.route('/index')
def index():
    # return "hello!"
    return render_template('index.html', data=data)

@app.route('/like')
def like():
    id = request.args.get('id')
    print(f'想要给{id}点赞！')
    data[int(id)]['num'] += 1
    return render_template('index.html', data=data)

app.run(debug=True)
