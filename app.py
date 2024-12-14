from flask import Flask, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/counter_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Counter(db.Model):
    __tablename__ = 'table_Counter'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String, nullable=False)
    client_info = db.Column(db.String, nullable=False)

@app.before_first_request
def init_db():
    db.create_all()

@app.route('/')
def counter():
    client_info = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    new_entry = Counter(datetime=current_time, client_info=client_info)
    db.session.add(new_entry)
    db.session.commit()

    count = Counter.query.count()

    response = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Counter App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 50px;
                background-color: #f9f9f9;
                color: #333;
            }}
            h1 {{
                color: #555;
            }}
        </style>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>I have been seen <strong>{count}</strong> times.</p>
        <p>Timestamp: {current_time}</p>
        <p>Client Info: {client_info}</p>
    </body>
    </html>
    """
    return response

@app.route('/data', methods=['GET'])
def get_data():
    rows = Counter.query.all()
    data = [{"id": row.id, "datetime": row.datetime, "client_info": row.client_info} for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
