import os


primaryColor = "#a6de9b"
accentColor = "#325343"

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'serenity'
}

api_key = "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"

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

width = 1366
height = 768
geometry = f"{width}x{height}"