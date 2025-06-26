import requests
from datetime import datetime

from flask import (
    Flask, 
    flash, 
    redirect,
    render_template, 
    request,
    url_for
)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "cualquiercosa"
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://root:@localhost/segundo_unificado"
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import City, Climate

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/city', methods=['POST', 'GET'])
def city():
    if request.method == "POST":
        name = request.form["name"]
        latitude = request.form["lat"]
        longitude = request.form["long"]

        new_city = City(name=name, lat=latitude, long=longitude)
        db.session.add(new_city)
        db.session.commit()
        flash("City added succefully", "success")


    cities_list = City.query.all()
    return render_template(
        'city.html',
        cities=cities_list # nombre en html = nombre en back
    )


@app.route('/city/<int:city_id>')
def city_detail(city_id):
    city = City.query.get_or_404(city_id)
    latest_weather = city.climates[-1] if len(city.climates)>0 else None

    return render_template(
        'city_detail.html', 
        city=city, 
        latest_weather=latest_weather
    )


@app.route('/city/<int:city_id>/get_current_climate')
def get_current_climate(city_id):
    city = City.query.get_or_404(city_id)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city.lat}&longitude={city.long}&timezone=auto&current_weather=true"
    
    try:
        response = requests.get(url)
        data = response.json()

        if 'current_weather' in data:
            current_weather = data['current_weather']
            now = datetime.now()
            # Verificar si existe un registro para hoy
            existing_weather = Climate.query.filter(
                Climate.ciudad_id == city.id,
                db.func.date(Climate.date) == now.date()
            ).first()

            if existing_weather:
                existing_weather.temperature = current_weather['temperature']
                existing_weather.windspeed=current_weather['windspeed']
                existing_weather.winddirection=current_weather['winddirection']
                existing_weather.date=now
                db.session.commit()

            else:
                weather = Climate(
                    temperature=current_weather['temperature'],
                    windspeed=current_weather['windspeed'],
                    winddirection=current_weather['winddirection'],
                    date=now,
                    ciudad_id=city.id
                )
                db.session.add(weather)
                db.session.commit()

    except:
        db.session.rollback()
        
    return redirect(url_for('city_detail', city_id=city_id))




if __name__ == '__main__':
    app.run(debug=True)
