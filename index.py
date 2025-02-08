from flask import Flask, request, jsonify
import requests

cliente_id =  "0c34f715c565cc576b7a919ed24e58bb20f30ca0"
secret =  "b872f58b84a1d3e1d0074dd293df507e699f5e0783ff3329136b2ee09c1c"
auth64 = "MGMzNGY3MTVjNTY1Y2M1NzZiN2E5MTllZDI0ZTU4YmIyMGYzMGNhMDpiODcyZjU4Yjg0YTFkM2UxZDAwNzRkZDI5M2RmNTA3ZTY5OWY1ZTA3ODNmZjMzMjkxMzZiMmVlMDljMWM="
url = "https://api.bling.com.br/Api/v3/oauth/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "1.0",
    "Authorization": "Basic " + auth64
}


app = Flask(__name__)

@app.get('/')
def index():
    return jsonify({"run": True})

@app.route('/refresh', methods=["GET", "POST"])
def refresh():
    data = {
        "grant_type": "refresh_token",
        "refresh_token": request.args.get('refresh_token')
    }

    response = requests.post(url, headers=headers, data=data)

    return jsonify(response.json())


@app.route('/token', methods=["GET", "POST"])
def token():
    code = request.args.get('code')

    data = {
        "grant_type": "authorization_code",
        "code": code
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)

    return jsonify(response.json())



if __name__ == "__main__":
    app.run()