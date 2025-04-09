import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Funkcija saglabāšanai datu bāzē
def save_calculation(input_value, conversion_type, result):
    conn = sqlite3.connect('calculations.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO calculations (input_value, conversion_type, result)
        VALUES (?, ?, ?)
    ''', (input_value, conversion_type, result))
    conn.commit()
    conn.close()

# Funkcija, lai iegūtu pēdējos 5 ierakstus
def get_last_5_calculations():
    conn = sqlite3.connect('calculations.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT input_value, conversion_type, result, timestamp
        FROM calculations
        ORDER BY timestamp DESC
        LIMIT 5
    ''')
    results = cursor.fetchall()
    conn.close()
    return results

# Esošā konvertēšanas funkcija
def convert_time():
    print("Time converter")
    choice = input("Choose what you want to convert (seconds to minutes, seconds to hours, minutes to hours, hours to minutes, hours to seconds): ").lower()

    if "seconds to minutes" in choice:
        seconds = int(input("Enter seconds: "))
        minutes = seconds / 60
        print(f"{seconds} seconds is about {minutes:.2f} minutes.")

    elif "seconds to hours" in choice:
        seconds = int(input("Enter seconds: "))
        hours = seconds / 3600
        print(f"{seconds} seconds is about {hours:.2f} hours.")

    elif "minutes to hours" in choice:
        minutes = int(input("Enter minutes: "))
        hours = minutes / 60
        print(f"{minutes} minutes is about {hours:.2f} hours.")

    elif "hours to minutes" in choice:
        hours = float(input("Enter hours: "))
        minutes = hours * 60
        print(f"{hours} hours is about {minutes:.2f} minutes.")

    elif "hours to seconds" in choice:
        hours = float(input("Enter hours: "))
        seconds = hours * 3600
        print(f"{hours} hours is about {seconds:.2f} seconds.")

    else:
        print("Unknown option. Please try again.")

convert_time()

# Maršruts aprēķiniem un saglabāšanai
@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    input_value = data['input_value']
    conversion_type = data['conversion_type']

    # Konvertēšanas loģika
    if conversion_type == "seconds-to-minutes":
        result = input_value / 60
    elif conversion_type == "minutes-to-hours":
        result = input_value / 60
    elif conversion_type == "hours-to-seconds":
        result = input_value * 3600
    else:
        return jsonify({"error": "Unknown conversion type"}), 400

    # Saglabāt aprēķinu datu bāzē
    save_calculation(input_value, conversion_type, result)

    return jsonify({"input_value": input_value, "conversion_type": conversion_type, "result": result})

# Maršruts, lai iegūtu pēdējos 5 aprēķinus
@app.route('/history', methods=['GET'])
def history():
    last_5 = get_last_5_calculations()
    return jsonify(last_5)

if __name__ == '__main__':
    app.run(debug=True)