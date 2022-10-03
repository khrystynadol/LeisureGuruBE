from waitress import serve
import main

serve(app.app, host='127.0.0.1', port=5000)
