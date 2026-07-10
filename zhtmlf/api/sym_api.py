# -*- coding: utf8 -*-
"""
Sympy Calculator API
版本(Version):1.2.0
作者(Anthor):YGT314159
"""
import os
import sys
import json
import xml.etree.ElementTree as ET
from bottle import Bottle, response, request, static_file
import urllib.parse

# 检查 sympy 是否已安装
try:
    import sympy
except ImportError:
    print("Error: sympy not installed. Run: pip install sympy", file=sys.stderr)
    sys.exit(1)

### 全局变量
app = Bottle()
server = None

### CORS 中间件
def add_cors_headers():
    """为所有响应添加 CORS 头，支持 file:// 和跨域访问"""
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With')
    response.set_header('Access-Control-Max-Age', '86400')

@app.hook('after_request')
def enable_cors():
    add_cors_headers()

@app.route('/<:re:.*>', method='OPTIONS')
def cors_options():
    add_cors_headers()
    return ''

### 辅助函数：生成XML响应
def generate_xml_response(data):
    root = ET.Element("response")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return ET.tostring(root, encoding='utf-8').decode('utf-8')

### 辅助函数：生成HTML响应
def generate_html_response(data):
    html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Sympy Calculation Result</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; }
        .container { border: 1px solid #ddd; border-radius: 8px; padding: 20px; }
        .success { color: #28a745; }
        .error { color: #dc3545; }
        .expr { background: #f8f9fa; padding: 10px; border-radius: 4px; font-family: monospace; }
        .result { font-size: 1.2em; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sympy Calculation Result</h1>"""

    if data.get("status") == "success":
        html += f"""
        <p class="success">Status: Success</p>
        <p>Expression: <div class="expr">{data.get('expression', '')}</div></p>
        <p>Format: {data.get('format', 'text')}</p>
        <p class="result">Result: <strong>{data.get('result', '')}</strong></p>"""
    else:
        html += f"""
        <p class="error">Status: Error</p>
        <p>Message: {data.get('message', '')}</p>"""

    html += """
    </div>
</body>
</html>"""
    return html

### 内置路由函数 ###
@app.route('/__exit', method=['GET','HEAD'])
def __exit():
    global server
    if server:
        server.stop()
    return "Server stopped"

@app.route('/__ping')
def __ping():
    return "ok"

@app.route('/assets/<filepath:path>')
def server_static(filepath):
    # 向上找一层，使 /assets/math/index.html 能对应到 ../math/index.html
    return static_file(filepath, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

@app.route('/')
def serve_index():
    """根路径重定向到 math/index.html"""
    response.status = 302
    response.set_header('Location', '/assets/math/index.html')
    return ''

@app.route('/math')
@app.route('/math/')
def serve_math_index():
    """/math 路径重定向到 math/index.html"""
    response.status = 302
    response.set_header('Location', '/assets/math/index.html')
    return ''

### 辅助函数：从请求中提取参数
def _get_param(name, default=None):
    """从 GET query、POST form、JSON body 或路径中提取参数"""
    # 1. 优先从 query string 获取（GET/POST 都支持 query）
    val = request.query.get(name)
    if val:
        return val

    # 2. 尝试从 POST form 获取
    if request.content_type and 'application/x-www-form-urlencoded' in request.content_type:
        val = request.forms.get(name)
        if val:
            return val

    # 3. 尝试从 JSON body 获取
    if request.content_type and 'application/json' in request.content_type:
        try:
            body = request.json
            if body and isinstance(body, dict) and name in body:
                return body[name]
        except Exception:
            pass

    # 4. 尝试从 multipart form 获取
    val = request.forms.get(name)
    if val:
        return val

    return default


def _get_expr_from_path():
    """从路径中提取表达式（/calculate/expr）"""
    parts = request.path.split('/', 2)
    if len(parts) > 2:
        return urllib.parse.unquote(parts[2])
    return None


### 业务路由函数 ###
@app.route('/calculate', method=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def calculate():
    # 获取参数（支持多种请求方式）
    expr_str = _get_param('expr')
    format_type = _get_param('format', 'text')   # 默认text格式
    result_type = _get_param('result', 'json')    # 默认json响应

    # 验证参数合法性
    if format_type not in ['text', 'latex']:
        response.status = 400
        error_data = {"status": "error", "message": "Invalid format parameter, supported: text, latex"}
        return handle_response(error_data, result_type)

    if result_type not in ['json', 'html', 'text', 'xml']:
        response.status = 400
        error_data = {"status": "error", "message": "Invalid result parameter, supported: json, html, text, xml"}
        return handle_response(error_data, result_type)

    # 获取表达式参数：query > form > json body > 路径
    if not expr_str:
        expr_str = _get_expr_from_path()

    if not expr_str:
        response.status = 400
        error_data = {"status": "error", "message": "Missing expression parameter, use ?expr=... or JSON body {'expr': '...'} or /calculate/expr"}
        return handle_response(error_data, result_type)

    try:
        # URL解码表达式
        decoded_expr = urllib.parse.unquote(expr_str)
        # 使用sympy计算表达式
        sympy_result = sympy.sympify(decoded_expr)

        # 根据format参数处理表达式格式
        if format_type == 'latex':
            # 转换为LaTeX格式
            result_val = sympy.latex(sympy_result)
            expr_display = sympy.latex(sympy.sympify(decoded_expr))
        else:  # text格式
            try:
                if sympy_result.is_number:
                    result_val = str(sympy_result)+" = "+str(sympy_result.evalf())
                else:
                    result_val = str(sympy_result)
            except Exception:
                result_val = str(sympy_result)
            expr_display = str(sympy_result)

        # 构造响应数据
        response_data = {
            "status": "success",
            "expression": decoded_expr,
            "format": format_type,
            "result": result_val,
            "latex_expression": sympy.latex(sympy.sympify(decoded_expr)) if format_type == 'text' else result_val,
            "latex_result": sympy.latex(sympy_result)
        }

        return handle_response(response_data, result_type)

    except Exception as e:
        response.status = 400
        error_data = {
            "status": "error",
            "message": f"Failed to calculate expression: {str(e)}"
        }
        return handle_response(error_data, result_type)

### 响应处理统一函数
def handle_response(data, result_type):
    response.content_type = get_content_type(result_type)

    if result_type == 'json':
        return json.dumps(data, ensure_ascii=False)
    elif result_type == 'html':
        return generate_html_response(data)
    elif result_type == 'text':
        if data.get("status") == "success":
            return f"Expression: {data.get('expression')}\nFormat: {data.get('format')}\nResult: {data.get('result')}"
        else:
            return f"Error: {data.get('message')}"
    elif result_type == 'xml':
        return generate_xml_response(data)
    else:
        response.status = 400
        return json.dumps({"status": "error", "message": "Unsupported result type"})

### 获取内容类型
def get_content_type(result_type):
    content_types = {
        'json': 'application/json',
        'html': 'text/html',
        'text': 'text/plain',
        'xml': 'application/xml'
    }
    return content_types.get(result_type, 'application/json')


### 路由注册 ###
app.route('/__exit', method=['GET','HEAD'])(__exit)
app.route('/__ping', method=['GET','HEAD'])(__ping)
app.route('/assets/<filepath:path>', method='GET')(server_static)
app.route('/', method='GET')(serve_index)
app.route('/math', method='GET')(serve_math_index)
app.route('/math/', method='GET')(serve_math_index)
app.route('/calculate', method=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])(calculate)
# 支持路径传参方式
app.route('/calculate/<expr:path>', method=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])(calculate)


if __name__ == '__main__':
    try:
        from bottle import run
        print("=" * 60)
        print("[__Sympy Calculator API__]")
        print("=" * 60)
        print("服务启动: http://127.0.0.1:8080/")
        print("示例: http://127.0.0.1:8080/calculate?expr=1+2")
        print("示例: http://127.0.0.1:8080/calculate?expr=sin(pi/2)&format=latex&result=html")
        print("示例: http://127.0.0.1:8080/calculate?expr=integrate(x**2,x)")
        print("=" * 60)
        print("按 Ctrl+C 停止服务")
        run(app=app, host="127.0.0.1", port=8080, reloader=False)
    except KeyboardInterrupt:
        print("\n服务已停止")
    except Exception as ex:
        print(f"启动失败: {repr(ex)}", file=sys.stderr)
        sys.exit(1)
