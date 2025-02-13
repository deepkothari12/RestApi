from flask import Flask , jsonify , request , json
import ipl
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/api/teams")
def get_teams():
    teams = ipl.TeamApi() ##Noe here we het dict
    return jsonify(teams)

@app.route("/api/teamvteam")
def get_teamVsteam():
    # teams = ipl.team_Vs_team()
    team1 = request.args.get('team1'),
    team2 = request.args.get('team2'),
    teams_list = [team1 , team2]
    team1 = []
    #team2 = []
    for i in teams_list:
        #print(i[0])
        team1.append(i[0])
        #team2.append(i[0])
    
    #print(team1 )
    teams = ipl.team_Vs_team(teams1= team1[0] , teams2=team1[1])
    #print(teams)
    return jsonify(teams)

@app.route("/api/team_name") # type: ignore
def get_teamname():
    team_name = request.args.get("teamname"),
    #print("Team", team_name)
    
    team_responce = ipl.Ipl_team_allrecored(team=team_name[0]),
    #print(team_responce)
    

    return jsonify(team_responce) 


@app.route("/api/teamApi")
def getTeamApiwith():
    team_name = request.args.get("teamname")
    team_with_all = ipl.team_api(team_name)
    #print(team_with_all)
    return jsonify(team_with_all)




if __name__ == "__main__":
    app.run(debug=True)