from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <script>
        function add(chr) {
            document.getElementById("display").value += chr;
        }
        function reset() {
            document.getElementById("display").value = "";
            document.getElementById("result").value = "";
        }
        function equal() {
            try {
                expression = document.getElementById("display").value;
                document.getElementById("result").value = eval(expression);
            } catch (e) {
                document.getElementById("result").value = e.message;
            }
        }
    </script>
    <table border="1">
        <tr>
            <td colspan="4">
                <input placeholder="Expression" type="text" id="display">
            </td>
        </tr>
        <tr>
            <td colspan="4">
                <input placeholder="Result" disabled="disabled" type="text" id="result">
            </td>
        </tr>
        <tr>
            <td colspan="3" onclick="reset()">AC</td>
            <td onclick="add('/')">/</td>
        </tr>
        <tr>
            <td onclick="add(7)">7</td>
            <td onclick="add(8)">8</td>
            <td onclick="add(9)">9</td>
            <td onclick="add('*')">*</td>
        </tr>
        <tr>
            <td onclick="add(4)">4</td>
            <td onclick="add(5)">5</td>
            <td onclick="add(6)">6</td>
            <td onclick="add('-')">-</td>
        </tr>
        <tr>
            <td onclick="add(1)">1</td>
            <td onclick="add(2)">2</td>
            <td onclick="add(3)">3</td>
            <td onclick="add('+')">+</td>
        </tr>
        <tr>
            <td colspan="2" onclick="add(0)">0</td>
            <td onclick="add('.')">.</td>
            <td onclick="equal()">=</td>
        </tr>
    </table>
</body>
<style>
    tr {text-align: center;}
</style>
</html>
"""

app.run()