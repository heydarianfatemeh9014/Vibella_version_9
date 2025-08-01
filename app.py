from flask import Flask, request, send_file
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static')

@app.route('/')
def home():
    return send_file("index.html")

@app.route("/about")
def about():
    return send_file("about.html")

@app.route("/vibe_Post")
def vibe_Post():
    return send_file("vibe_Post.html")

@app.route("/feel_map")
def feel_map():
    return send_file("feel_map.html")

@app.route("/feel_room")
def feel_room():
    return send_file("feel_room.html")

@app.route("/open_sadness")
def open_sadness():
    return send_file("tears.html")

@app.route("/open_joy")
def open_joy():
    return send_file("joy.html")

@app.route("/open_love")
def open_love():
    return send_file("love.html")

@app.route("/open_peace")
def open_peace():
    return send_file("peace.html")

@app.route("/open_stress")
def open_stress():
    return send_file("stress.html")

@app.route("/open_hope")
def open_hope():
    return send_file("hope.html")

@app.route("/open_despair")
def open_despair():
    return send_file("despair.html")

@app.route("/open_pride")
def open_pride():
    return send_file("pride.html")

@app.route("/open_anxiety")
def open_anxiety():
    return send_file("anxiety.html")

@app.route("/open_loneliness")
def open_loneliness():
    return send_file("loneliness.html")

@app.route("/open_fear")
def open_fear():
    return send_file("fear.html")

@app.route("/open_anger")
def open_anger():
    return send_file("anger.html")

from werkzeug.utils import secure_filename

@app.route("/profile", methods=["GET", "POST"])
def profile():
    content = ""
    if os.path.exists("pro.txt"):
        with open("pro.txt", 'r') as file:
            content = file.read().strip()

    if request.method == "GET":
        if content == "":
            with open("profile.html") as f:
                base = f.read()
            return base + '''
                <body>
                    <form method="POST" action="/profile" enctype="multipart/form-data">
                        <input type="text" name="namee" placeholder="Your name" required>
                        <input type="text" name="last_name" placeholder="Your last name" required>
                        <input type="email" name="emaill" placeholder="Your email" required>
                        <input type="password" name="pass1" placeholder="Password" required>
                        <input type="password" name="pass2" placeholder="Repeat your password" required>
                        <input type="file" name="imgg" accept="image/*" required>
                        <button type="submit">Done</button>
                    </form>
                </body>'''
        else:
            with open("profile.html") as f:
                base = f.read()
            return base + '''
                <body>
                    <form method="POST" action="/profile" enctype="multipart/form-data">
                        <input type="email" name="emaill" placeholder="Your email" required>
                        <input type="password" name="pass1" placeholder="Password" required>
                        <input type="text" name="username" placeholder="Your username" required>
                        <input type="file" name="imgg" accept="image/*" required>
                        <button type="submit">Done</button>
                    </form>
                </body>'''

    if request.method == "POST":
        if content == "":
            name = request.form.get('namee')
            last_name = request.form.get('last_name')
            emaill = request.form.get('emaill')
            pass1 = request.form.get('pass1')
            pass2 = request.form.get('pass2')
            image = request.files.get('imgg')

            if len(pass1) < 8 or len(pass1) > 15:
                return send_file("sign_up.html") + "<h1>Password must be 8-15 characters</h1>"
            elif pass1 != pass2:
                return send_file("sign_up.html") + "<h1>Passwords do not match</h1>"

            username = ''.join([str(i) + '!' if i % 3 == 0 else '' for i in range(len(pass1))])
            username += ''.join(['@' for i in range(len(pass1)) if i % 5 == 0])

            with open("pro.txt", 'w') as file:
                file.write(f"name:{name},last_name:{last_name},password:{pass1},username:{username},email:{emaill}")

            if image and image.filename:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], "profile.jpg"))

            return send_file("sign_up.html") + f"<h1>Welcome {name} {last_name}! Username: {username}</h1>"
        else:
            emaill = request.form.get('emaill')
            pass1 = request.form.get('pass1')
            username = request.form.get('username')

            dic = {}
            for item in content.split(','):
                key, value = item.split(':')
                dic[key] = value

            if dic.get('email') != emaill:
                return send_file("sign_up.html") + "<h1>Wrong email</h1>"
            elif dic.get('password') != pass1:
                return send_file("sign_up.html") + "<h1>Wrong password</h1>"
            elif dic.get('username') != username:
                return send_file("sign_up.html") + "<h1>Wrong username</h1>"
            else:
                return send_file("sign_up.html") + f"<h1>Welcome {dic.get('name')}</h1><img src='/static/profile.jpg' width='300'>"

if __name__ == '__main__':
    app.run(debug=True)
