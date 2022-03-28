"""Flask service that returns date now."""

from flask import Flask
import datetime


def main():
    """Entry-point of the program."""
    app = Flask(__name__)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def handler(path):
        """Handle all requests."""
        # Save time now to change it in "human" and "timestamp" form
        date = datetime.datetime.now()
        return 'Current time: {human}<br>Timestamp: {timestamp}'.format(
            human=date.ctime(),
            timestamp=date.timestamp()
        )

    app.run(host='127.0.0.1', port=8000)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        input('Exit program by pressing ^C\nType any key to continue...')
