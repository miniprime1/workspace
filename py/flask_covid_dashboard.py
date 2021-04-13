from covid import Covid
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return f"""
<!DOCTYPE html>
<html>

<head>
    <title>COVID-19 Dashboard</title>
</head>

<body>
    <h1>COVID-19 Dashboard</h1>
    <hr/>
    <h2>Worldwide</h2>
    <h3>Confirmed: {Covid().get_total_confirmed_cases()}</h3>
    <h3>Deaths: {Covid().get_total_deaths()}</h3>
    <h3>Recovered: {Covid().get_total_recovered()}</h3>
</body>

</html>
"""

app.run()
