from flask import Flask
from flask import request
from flask import jsonify
from flask import redirect
from flask import render_template, url_for
from setuitem import SetuItem

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 配置编码显示中文

@app.route('/')
def index():
    return 'Hello world'

@app.route('/setus', methods=['GET'])
def get_setus():
    setu = SetuItem()
    data = setu.get_setus()
    print(data)
    print("获取成功！")
    return jsonify(data)
    setu.close()

@app.route('/setu', methods=['GET'])
def get_setu():
    setu = SetuItem()
    link = str(setu.get_setu())
    return render_template('index.html', link=link)
    # return redirect(link)

@app.route('/setu/max', methods=['GET'])
def get_setumax():
    setu = SetuItem()
    link = str(setu.get_setu())
    return render_template('setu.html', link=link)

@app.route('/setu/water', methods=['GET'])
def get_setuwater():
    setu = SetuItem()
    links = []
    for i in range(15):
        links.append(setu.get_setu())
    return render_template('water.html', links=links)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)