from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
  <head>
    <title>URL Redirector</title>
  </head>
  <body>
    <script>
    function redirect() {
      var url = document.getElementById("input").value;
      location.replace(url);
    }
    </script>
    <input placeholder="URL" type="text" id="input" name="url">
    <button onclick="redirect()" type="text">Redirect</button>
  </body>
</html>
'''

app.run()