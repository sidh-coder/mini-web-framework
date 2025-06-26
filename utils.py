import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

def render_template(filename):
    filepath = os.path.join(TEMPLATE_DIR, filename)
    if not os.path.isfile(filepath):
        return "<h1>Template Not Found</h1>"
    
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
