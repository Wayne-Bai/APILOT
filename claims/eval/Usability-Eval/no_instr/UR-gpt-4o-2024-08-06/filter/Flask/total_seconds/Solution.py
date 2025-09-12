from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/total_seconds', methods=['GET'])
def total_seconds():
    try:
        hours = float(request.args.get('hours', 0))
        minutes = float(request.args.get('minutes', 0))
        seconds = float(request.args.get('seconds', 0))
        
        total_seconds = int(hours * 3600 + minutes * 60 + seconds)
        
        return jsonify({
            'total_seconds': total_seconds
        }), 200
    
    except ValueError:
        return jsonify({
            'error': 'Invalid input. Please provide numerical values for hours, minutes, and seconds.'
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
