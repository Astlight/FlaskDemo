from flask import request, make_response, Response, jsonify, render_template, send_file, current_app
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_wtf.csrf import generate_csrf
from apps import create_app
from forms import addUserForm

app = create_app("dev")
mgr = Manager(app)  # flask_script 管理
mgr.add_command("mg", MigrateCommand)  # flask_script 管理


# $ python main.py mg init 初始化生成文件夹
# $ python main.py mg migrate -m "备注" . 生成表迁移版本py文件
# $ python main.py mg upgrade .同步表结构至数据库
# 降级有bug， 只升不降。

@app.route("/zxp")
def zxp():
    if request.method == "GET":
        data = '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form id="zqwssubmit" name="zqwssubmit" action="http://sign.zqsign.com/mobileSignView" method='post'>

        <input type="hidden" name='no' value="HMCONTRACT20181227155623110979"/>
        <input type="hidden" name='user_code' value="HMZQb2a874222e944d05adf45af995ba7e0f"/>
        <input type="hidden" name='return_url' value="https://dl.hmdata.com.cn/zhognqian/successed.html"/>
        <input type="hidden" name='zqid' value="ZQF4643748CAF147E48267C1EC4AAB17A3"/>
        <input type="hidden" name='notify_url' value="http://app.hmdata.com.cn:9191/hemo/spAudit/pdd/sign/notify"/>
        <input type="hidden" name='sign_val' value="HTyqfb+Md0zv7jnxzbCXebKegubOOBHHyOnKxPdIx/r4wOma537kRNWhAfIJ2T+sFNgBbv1oFGiDcycEdI9or7/j8wPdyXH0r2E/gphhwwtfLoerH86vAJMji62firIku6uqy6VfG7KQncH04Jc/0YxVUNoQPIq9APAFi20Y6+w="/>
        <input type="hidden" name='sign_type' value="WRITTENCODE"/><input type="hidden" name='sign_val' value="JLYlJp0x6jEepTWfoDZzi/u4YfhL6neejyIp6yvpCi+7VDISvuTdcyoiRMcMkKsArn6VCQI9kRcyXWviNDlqX4qAj3/VohGBwgBKQqI7+M6kUJn/eeSW4WQGwiy+zPVDV2dctIA2fM0mq9EHySyAHlUSYjrx8prIgMFXM7l1xTs="/>
        <input type="submit" value='确认' style="display:none;">

    </form>
    <script>document.forms['zqwssubmit'].submit();</script>
</body>
</html>
'''
        response = make_response(data)
        response.content_type = "text/html"
        return response


@app.route("/demo")
def index():
    return jsonify(datalist={
        "2018-06": [{"port_code": "166001", "rate": 38.38, "asset": 24090723.17, "tdate": "2018-06", "fundname": "趋势A"},
                    {"port_code": "166006", "rate": 61.62, "asset": 38677160.67, "tdate": "2018-06",
                     "fundname": "行业成长A"}],
        "2018-07": [{"port_code": "166001", "rate": 29.49, "asset": 23514289.17, "tdate": "2018-07", "fundname": "趋势A"},
                    {"port_code": "166006", "rate": 70.51, "asset": 56235042.23, "tdate": "2018-07",
                     "fundname": "行业成长A"}],
        "2018-08": [{"port_code": "166001", "rate": 29.76, "asset": 22666040.77, "tdate": "2018-08", "fundname": "趋势A"},
                    {"port_code": "166006", "rate": 70.24, "asset": 53492789.27, "tdate": "2018-08",
                     "fundname": "行业成长A"}],
        "2018-09": [{"port_code": "166001", "rate": 29.53, "asset": 22497328.39, "tdate": "2018-09", "fundname": "趋势A"},
                    {"port_code": "166006", "rate": 70.47, "asset": 53692127.89, "tdate": "2018-09",
                     "fundname": "行业成长A"}],
        "2018-10": [{"port_code": "166001", "rate": 29.39, "asset": 20411855.81, "tdate": "2018-10", "fundname": "趋势A"},
                    {"port_code": "166006", "rate": 70.61, "asset": 49042689.16, "tdate": "2018-10",
                     "fundname": "行业成长A"}],
        "2018-11": [{"port_code": "166001", "rate": 0, "asset": 0, "tdate": "2018-11", "fundname": "趋势A"},
                    {"port_code": "166006", "rate": 0, "asset": 0, "tdate": "2018-11", "fundname": "行业成长A"}]})


@app.route('/', methods=["GET", "POST"])
def hello_world():
    '''请求与响应'''

    '''接收参数'''
    print(request.args.get("name"))  # Method=GET,URL传参
    print(request.form.get("name"))  # Method=POST,表单传参
    print(request.json.get("name"))  # Method=POST,表单传参
    print(request.data.decode())  # Json bytes类型
    file = request.files.get("name")  # Method=POST,表单传文件 > FileStorage
    if file:
        print(file.content_type)  # >>> image/jpeg
        file.save("目录.jpg")

    '''set_session,flask自动根据secret_key生成session.id（默认存在服务器内存中）'''
    # session["uid"] = uid
    # session["username"] = username

    '''get_session'''
    # uid = session.get("uid")
    # if uid:
    #     return "user_information"

    '''异常'''
    # abort(403)  # >>> rasie 异常

    '''响应'''
    response = make_response("index")  # type: Response
    # return response, 700  # 返回响应对象 + 状态码
    # return 'index' # 返回字符串/bytes
    return jsonify(dict)  # content-type = application/json
    # return redirect('http://www.baidu.com')  # 重定向至url
    # return redirect(url_for("index")  # 重定向至视图函数


@app.route("/favicon.ico")
def favicon():
    return current_app.send_static_file("1.bmp")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # csrf_token = generate_csrf()  # 前后端分离生成token , the raw token in ``session['csrf_token']``
        # response = make_response(app.send_static_file("login.html"))
        # response.set_cookie("csrf_token", csrf_token)  # == (request.headers["X-Csrftoken"])
        # 前端 headers:{"X-CSRFToken":getCookie("csrf_token")}, CSRFProtect(app) 自动校验
        # return response
        return render_template('login.html')
        # app.send_static_file这个html不经过jinja2修饰。render_template返回后端渲染html,经过jinja2修饰

    elif request.method == "POST":
        print(request.form)
        print(request.form.get("username"))
        print(request.form.get('password'))
        # print(request.headers['X-CSRFToken'])
        return jsonify({'message': "ok", 'code': '200'})
        # form = addUserForm()
        # if form.validate_on_submit():
        #     return jsonify({
        #         "status": "success",
        #         "msg": "添加成功",
        #         "data": {
        #             "name": form.username.data,
        #             "password": form.password.data
        #         }
        #     })
        #     # 验证未通过
        # return jsonify({
        #     "status": "failed",
        #     "msg": "添加失败",
        #     "error": form.errors
        # })


@app.route("/templates")
def templates():
    parameter = "阿斯顿发光"
    return render_template("baidu.html", parameter=parameter)  # 模板渲染 {{ parameter | 过滤器 }} （ 支持对象属性，对象方法，函数）


# view-flash("message"),T-{{get_flashed_message()}} 遍历取出message
# render默认会对参数的符号标记进行转义，通过过滤器safe取消转义。
'''
{% for data in my_list if data.id != 5 %} {# loop只能在循环内部使用 #}     
    {% if loop.index == 1 %}       index start from 1, index0 startf from 0  
        <li style="background-color: #ffb300">{{ data.value }}</li>     
    {% elif loop.index == 2 %}         
        <li style="background-color: #ff0000">{{ data.value }}</li>     
    {% else %}         
        <li style="background-color: #1cb7fd">{{ data.value }}</li>     
    {% endif %} 
{% endfor %}
'''


@app.route("/url_parameter/<parameter>")  # /url_parameter/1
# @app.route("/url_parameter/<int:parameter>||<string(length=2):parameter>")
# 正则parameter|BaseConverter(werkzeug) 可自定义
# 底层to_python方法，在传给视图之前触发，可以对路由变量进行加工。（大小写敏感，str转int）
def url_parameter(parameter):
    return parameter


if __name__ == "__main__":
    # print(app.url_map)  # >>> Map([<Rule '/' (OPTIONS, HEAD, GET) -> hello_world>
    #  <Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>])
    app.run(host="0.0.0.0", port=5000, debug=False,load_dotenv=True)
    # mgr.run()  # flask_script脚本管理 $ python main.py runserver -h 0.0.0.0 -p 5000
