import web  # pip install web.py
git
urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
