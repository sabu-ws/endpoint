from app import socketio
from app import app

if __name__ == "__main__":
    # For production
    # socketio.run(app,"127.0.0.1", 8888, debug=True,use_reloader=False)
    # ../sabu-venv/bin/gunicorn -w 2 app:app --certfile ../ssl/sabu.crt --keyfile ../ssl/private/sabu.key -b 127.0.0.1:8888

    # For dev
    socketio.run(app, "0.0.0.0", 8888, debug=True, use_reloader=True, allow_unsafe_werkzeug=True)
