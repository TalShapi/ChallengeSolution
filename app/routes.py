from app import app
import challenge_funcs as CF

@app.route('/bikeshare/id/<number>')
def bikeshare(number):
    return CF.get_station_info(number);

@app.route('/towords/<number>')
def towords(number):
    return CF.convert_num_to_words(number);