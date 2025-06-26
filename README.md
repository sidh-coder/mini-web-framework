# Mini-web-framework

A minimal Python-based web framework, built from scratch with detailed documentation and learning-focused structure.

This is a basic yet functional web framework you can use to host small web apps or websites, either locally or globally.

---

##  Getting Started

### 1. Configure `main.py`

In `main.py`, set the following:

- `HOST`: The IP address of the server (e.g., `127.0.0.1` for localhost, or your LAN IP).
- `PORT`: Any available port you'd like to serve on (e.g., `9999`).

No other major changes are required to run the server.

---

### 2. Define Routes in `routes.py`

To add routes to your app:

1. Create a new function (see examples in `routes.py`).
2. Use the `@route("your-path")` decorator above the function.
3. Inside the function, use `html = render_template("your_template.html")` to load your HTML file.
4. Return the response like so:

```python
return 200, "text/html", htmlpanel-22-12
```
### 3. Add HTML Templates

Place your .html files inside the templates/ directory. These will be rendered via the render_template() utility.
### Notes:
* This project is a learning-focused mini-framework, not meant to replace Flask, Django, or other production-level tools.
    
* It is ideal for beginners wanting to understand the inner workings of a web framework.

* Full documentation and a step-by-step explanation will be published in a blog post and linked here soon.

💡 Contribution & Feedback

Bug fixes and improvements will be added gradually. If you'd like to contribute or suggest changes, feel free to open issues or pull requests!
