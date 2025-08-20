from flask import Flask, render_template
import requests

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

# Tvůj Steam Web API klíč
STEAM_API_KEY = "72547210A1D49DA9A8CD3497ADCB6568366FE1E71F6"
STEAM_ID = "76561198274487668"  # tvoje SteamID64

def get_steam_userinfo(steam_id):
    url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={STEAM_API_KEY}&steamids={steam_id}"
    try:
        resp = requests.get(url)
        print("HTTP status:", resp.status_code)
        print("Raw response:", resp.text)  # celý JSON, co API vrací
        if resp.status_code == 200:
            data = resp.json()
            print("Parsed JSON:", data)
            players = data.get("response", {}).get("players", [])
            print("Players list:", players)
            if players:
                return players[0]
    except Exception as e:
        print(f"Chyba při získávání Steam uživatelských informací: {e}")
    return None

@app.route("/")
def index():
    steam_user = get_steam_userinfo(STEAM_ID)
    if steam_user is None:
        # fallback, pokud API nevrátí žádná data
        steam_user = {"steamid": STEAM_ID, "personaname": STEAM_ID}
    return render_template("index.html", steam_user=steam_user)

if __name__ == "__main__":
    app.run(debug=True)