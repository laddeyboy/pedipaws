import os
import tornado.ioloop
import tornado.web
import tornado.log
import queries
from jinja2 import Environment, PackageLoader, select_autoescape

ENV = Environment(
    loader = PackageLoader('company-app', 'templates'),
    autoescape=select_autoescape(['html', 'xml']))
    
class TemplateHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = queries.Session(
            #CHANGE DATABASE NAME TO SERVICES ON PUSH/PRODUCTION
            'postgresql://postgres@localhost:5432/jjl-services')
    
    def render_template (self, tpl, context):
        template = ENV.get_template(tpl)
        self.write(template.render(**context))
        
class MainHandler(TemplateHandler):
    def get(self):
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        # name = self.get_query_argument('name', 'Vistor')
        self.render_template("index.html", {})
        
class ServicesHandler(TemplateHandler):
    def get(self): 
        ppservices = self.session.query('SELECT * FROM services')
        self.render_template('services.html'), {'ppservices': services})
        
class BlogPostHandler(TemplateHandler):
    def get(self, slug):
        posts = self.session.query( 'SELECT * FROM post WHERE slug = %(slug)s', {'slug': slug})
        self.render_template("post.html", {'post': posts[0]})
        
    def post (self, slug):
        comment = self.get_body_argument('comment')
        print(comment)
        posts = self.session.query( 'SELECT * FROM post WHERE slug = %(slug)s', {'slug': slug} )
        # Save Comment Here
        self.redirect('/post/' + slug, {'comment': comment})
        
#This is the "tornado" code!
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/post/(.*)", BlogPostHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': 'static'} ),
    ], autoreload=True)

if __name__ == "__main__":
    tornado.log.enable_pretty_logging()
    app = make_app()
    app.listen(int(os.environ.get('PORT', '8080')))
    tornado.ioloop.IOLoop.current().start()