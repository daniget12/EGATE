from flask import Blueprint, request, make_response, render_template_string

web_challenges_bp = Blueprint("web_challenges", __name__, url_prefix="/web")

@web_challenges_bp.route("/get-ahead", methods=["GET", "POST", "HEAD"])
def get_ahead():
    if request.method == "HEAD":
        resp = make_response()
        resp.headers["X-Flag"] = "egate{r3j3ct_g3t_us3_h34d}"
        return resp
    elif request.method == "POST":
        return "<html style='background: blue; color: white;'><h1>Blue!</h1><p>Try something else</p></html>"
    else:
        # GET
        return "<html style='background: red; color: white;'><h1>Red!</h1><p>Try something else</p></html>"

@web_challenges_bp.route("/cookies", methods=["GET"])
def cookies():
    cookie_val = request.cookies.get("snickerdoodle")
    if cookie_val == "1":
        return "<h1>Admin area!</h1><p>egate{c00ki3s_4r3_d3l1c10us}</p>"
    else:
        resp = make_response("<h1>Guest area</h1><p>You need the right cookie. Check your developer tools.</p>")
        resp.set_cookie("snickerdoodle", "0")
        return resp

@web_challenges_bp.route("/local-auth", methods=["GET"])
def local_auth():
    html = '''
    <html>
    <head><title>Secure Login</title></head>
    <body>
        <h2>Login Area</h2>
        <form onsubmit="return checkPassword()">
            <input type="text" id="username" placeholder="Username"><br>
            <input type="password" id="password" placeholder="Password"><br>
            <button type="submit">Login</button>
        </form>
        <p id="msg"></p>
        <script src="/web/local-auth/secure.js"></script>
    </body>
    </html>
    '''
    return render_template_string(html)

@web_challenges_bp.route("/local-auth/secure.js", methods=["GET"])
def secure_js():
    js = '''
    function checkPassword() {
        var user = document.getElementById("username").value;
        var pass = document.getElementById("password").value;
        if (user === "admin" && pass === "strong_password_123") {
            document.getElementById("msg").innerText = "Success! The flag is: egate{1nspeC7_3l3ment_1s_k3y}";
        } else {
            document.getElementById("msg").innerText = "Login Failed.";
        }
        return false;
    }
    '''
    resp = make_response(js)
    resp.headers["Content-Type"] = "application/javascript"
    return resp

@web_challenges_bp.route("/robots.txt", methods=["GET"])
def robots_txt():
    txt = "User-agent: *\nDisallow: /web/secret-flag-page.html\n"
    resp = make_response(txt)
    resp.headers["Content-Type"] = "text/plain"
    return resp

@web_challenges_bp.route("/secret-flag-page.html", methods=["GET"])
def secret_flag_page():
    return "<h1>Secret Page</h1><p>egate{r0b0ts_txt_1s_pUbl1c}</p>"

@web_challenges_bp.route("/sql-direct", methods=["GET", "POST"])
def sql_direct():
    # Replacing the actual DB access with a simulated basic SQL injection challenge
    html = '''
    <html>
    <head><title>Admin Login</title></head>
    <body style="background: black; color: green; font-family: monospace; text-align: center; padding-top: 50px;">
        <h2>Admin Authentication System</h2>
        <p>Enter username and password (hint: bypass the auth!)</p>
        <form method="POST">
            <input type="text" name="username" placeholder="Username"><br><br>
            <input type="password" name="password" placeholder="Password"><br><br>
            <button type="submit">Login</button>
        </form>
        <br>
        {% if msg %}<p style="color: red;">{{ msg }}</p>{% endif %}
        {% if flag %}<p style="color: yellow; font-size: 20px;">{{ flag }}</p>{% endif %}
    </body>
    </html>
    '''
    msg = None
    flag = None
    if request.method == "POST":
        user = request.form.get("username", "")
        # A simple fake SQLi check: if user contains ' OR '1'='1 (or similar), grant access
        if "' OR" in user.upper() or "'OR" in user.upper():
            flag = "egate{p5ql_1nj3ct10n_w0rks}"
        else:
            msg = f"SELECT * FROM users WHERE username='{user}' AND password='...' -> 0 rows."
    return render_template_string(html, msg=msg, flag=flag)
