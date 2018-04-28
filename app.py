import tornado.ioloop
import tornado.web
import os

from jinja2 import Environment, PackageLoader, select_autoescape
  
ENV = Environment(
    loader=PackageLoader('company-app', 'templates'),
    autoescape=select_autoescape(['html', 'xml']))
    
class TemplateHandler(tornado.web.RequestHandler):
    def render_template (self, tpl, context):
        template = ENV.get_template(tpl)
        self.write(template.render(**context))

class MainHandler(TemplateHandler):
    def get(self):
        self.render_template("index.html", {})
        
class TestHandler(TemplateHandler):
    def get(self):
        self.render_template("test.html", {})
        
class RecipeHandler(TemplateHandler):
    def get(self):
        self.render_template("recipes.html", {})
        
class AboutHandler(TemplateHandler):
    def get(self):
        self.render_template("about.html", {})
        
class ContactHandler(TemplateHandler):
    def get(self):
        self.render_template("contact.html", {})
        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/test", TestHandler),
        (r"/recipes", RecipeHandler),
        (r"/about", AboutHandler),
        (r"/contact", ContactHandler),
        (
            r"/static/(.*)",
            tornado.web.StaticFileHandler,
            {'path': 'static'}
        ),
        ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()

    app = make_app()
    PORT = int(os.environ.get('PORT', '8888'))
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()