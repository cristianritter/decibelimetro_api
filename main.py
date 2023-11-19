#import serial
import json
from flask import Flask, render_template, request, make_response
from hid_receiver import request
from datetime import datetime
app = Flask(__name__)

i = 0

"""def update_value():
    while 1:
        try:
            with serial.Serial('COM3', 9600) as ser: 
                global i
                linha = ser.readline()
                linha_str = linha.decode('utf-8') 	
                print(linha_str)
                i = int(linha_str)
                ser.flush
            sleep(1)
        except:
            pass
"""
            
@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    try:
        i = request()
    except Exception as err:
        print(err)
        print("Cant open device, try run main.py as sudo.")
        return "Cant open device, try run main.py as sudo"    
    data = [{'timestamp': datetime.now().timestamp().__round__()}]
    for idx, value in enumerate(i):
        line = {'device':idx, 'value': value}
        data.append(line)

    #if(len(data) == 1): data = ["Cant open device, try run main as sudo."]
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

#t1 = threading.Thread(target=update_value, args=())
#t1.start()

if __name__ == "__main__":
    app.run(debug=True)


