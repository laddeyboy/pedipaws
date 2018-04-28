# class BlogPostHandler(TemplateHandler):
#     def get(self, slug):
#         posts = self.session.query( 'SELECT * FROM post WHERE slug = %(slug)s', {'slug': slug})
#         self.render_template("post.html", {'post': posts[0]})
        
#     def post (self, slug):
#         comment = self.get_body_argument('comment')
#         print(comment)
#         posts = self.session.query( 'SELECT * FROM post WHERE slug = %(slug)s', {'slug': slug} )
#         # Save Comment Here
#         self.redirect('/post/' + slug, {'comment': comment})
        
import os
import tornado.ioloop
import tornado.web
import tornado.log
import queries
import boto3
from jinja2 import Environment, PackageLoader, select_autoescape

client = boto3.client(
  'ses',
  region_name='us-east-1',
  aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
  aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
)

ENV = Environment(
  loader=PackageLoader('company-app', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])
)

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
    self.set_header( 'Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
    context = {}
    self.render_template("index.html", context)
    
class ServicesHandler(TemplateHandler):
    def get(self): 
        # ppservices = self.session.query('SELECT * FROM services')
        # print(ppservices[0])
        # self.render_template('services.html', {'ppservices': services})
        self.render_template('services.html', {})

class PageHandler(TemplateHandler):
    def get(self, page):
        context = {}
        self.set_header('Cache-Control','no-store, no-cache, must-revalidate, max-age=0')
        self.render_template(page, context)

class FormHandler(TemplateHandler):
  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("form.html", {})
    
  def post(self):
    email = self.get_body_argument('email', None)
    comments = self.get_body_argument('comments', None)
    error = ''
    if email:
      print('EMAIL:', email)
      send_email(email, comments)
      self.redirect('/form-success')

    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("form.html", {'error': error})
    
def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/form", FormHandler),
    (r"/page2", PageHandler),
    (r"/services",ServicesHandler),
    (r"/(form-success)", PageHandler),
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
