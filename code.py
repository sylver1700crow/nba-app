import requests

def get_latest_games():
    url = "https://www.balldontlie.io/api/v1/games"
    params = {
        "per_page": 10,
        "page": 1,
        "seasons[]": 2023,
        "postseason": False
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()["data"]
        for game in data:
            home = game["home_team"]["full_name"]
            visitor = game["visitor_team"]["full_name"]
            home_score = game["home_team_score"]
            visitor_score = game["visitor_team_score"]
            print(f"{visitor} {visitor_score} - {home_score} {home}")
    else:
        print("Erreur lors de la récupération des données.")

if __name__ == "__main__":
    get_latest_games()
