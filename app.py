from flask import (
    Flask, 
    flash, 
    render_template, 
    request, 
    redirect,
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
    return render_template(
        'city_detail.html', 
        city=city, 
    )

@app.route('/city/<int:city_id>/get_current_climate')
def get_current_climate(city_id):
    city = City.query.get_or_404(city_id)
    API_URL_BASE = f'https://api.open-meteo.com/v1/forecast?latitude={city.lat}&longitude={city.long}&timezone=auto&current_weather=true'
    return redirect(url_for('city_detail', city_id=city_id))




if __name__ == '__main__':
    app.run(debug=True)
