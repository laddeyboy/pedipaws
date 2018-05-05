import os
import tornado.ioloop
import tornado.web
import tornado.log
import math
import queries
import markdown2
import boto3
import datetime

from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import datetime, timedelta

client = boto3.client(
    'ses',
    region_name='us-east-1',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'))

ENV = Environment(
    loader=PackageLoader('company-app', 'templates'),
    autoescape=select_autoescape(['html', 'xml']))

def send_email (cname, contactcomments, email):
    response = client.send_email(
    Destination={
      'ToAddresses': ['ContactPediPaws@gmail.com'],
    },
    Message={
      'Body': {
        'Text': {
          'Charset': 'UTF-8',
          'Data': '{} has asked a question: \n\n{}\n\n Please respond at: {}.'.format(cname, contactcomments, email),
        },
      },
      'Subject': {'Charset': 'UTF-8', 'Data': 'Client comment'},
    },
    Source='ContactPediPaws@gmail.com',
  )
class TemplateHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = queries.Session(os.environ.get('DATABASE_URL', 'postgresql://postgres@localhost:5432/pedipaws'))
            
    def post(self, context):
        cname = self.get_body_argument('cname', None)
        print('cname: ', cname)
        contactcomments = self.get_body_argument('contactcomments', None)
        print('contactcomments: ', contactcomments)
        email = self.get_body_argument('email', None)
        print('email: ', email)
        if email:
            send_email(cname, contactcomments, email)
            self.redirect('success.html', {})
        
    
    def render_template(self, tpl, context):
        template = ENV.get_template(tpl)
        self.write(template.render(**context))


  
class MainHandler(TemplateHandler):
    def get(self):
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')
        context = {}
        self.render_template("index.html", context)

class SuccessHandler(TemplateHandler):
    def get(self, context):
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')
        context = {}
        self.render_template("success.html", context)
        
class ServicesHandler(TemplateHandler):
    def get(self):
        ppservices = self.session.query('SELECT * FROM services')
        self.render_template('services.html', {'ppservices': ppservices})


class AboutHandler(TemplateHandler):
    def get(self):
        context = {}
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template('about.html', {})


class ReviewsHandler(TemplateHandler):
    def post(self, page):
        name = self.get_body_argument('name')
        stars = self.get_body_argument('rating')
        text = self.get_body_argument('review')
        page = self.get_argument('page')
        self.session.query('''
        INSERT INTO reviews VALUES(
        DEFAULT,
        %(name)s,
        %(stars)s,
        %(text)s)
        ''', {
            'name': name,
            'stars': stars,
            'text': text
        })
        self.redirect('/reviews?page=0')

    def get(self, page):
        page = int(self.get_argument('page'))
        offset = page * 5
        review_count = self.session.query('''
        SELECT COUNT(*) AS count FROM reviews
        ''')[0]['count']

        if math.ceil((review_count - 5) / 5) > page:
            nextpage = page + 1
        else:
            nextpage = page

        if page > 0:
            lastpage = page - 1
        else:
            lastpage = 0

        reviews = self.session.query('''
        SELECT *
        FROM reviews
        ORDER BY id DESC
        LIMIT 5 
        OFFSET %(offset)s
        ''', {'offset': offset})
        graphic_reviews = []
        for review in reviews:
            review['stars'] *= "\u2605"
            graphic_reviews.append(review)
        page = str(int(page) + 1)
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template(
            'reviews.html', {
                'reviews': graphic_reviews,
                'page': page,
                'nextpage': str(nextpage),
                'lastpage': str(lastpage)
            })


class AppointmentsHandler(TemplateHandler):
    def get(self):
        context = {}
        self.set_header('Cache-Control',
                        'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("appointment.html", {})

    def post(self):
        fname = self.get_body_argument('fname', None)
        lname = self.get_body_argument('lname', None)
        petname = self.get_body_argument('petname', None)
        email = self.get_body_argument('email', None)
        phone = self.get_body_argument('phone', None)
        service = self.get_argument('service', None)
        date = self.get_body_argument('date', None)
        time = self.get_argument('time', None)
        comment = self.get_body_argument('comments', None)
        error = ''
        print(service)
        
        service_length = self.session.query('''
        SELECT duration FROM services WHERE service = %(service)s
        ''', {'service': service})[0]['duration']
        
        fullname = fname + ' ' + lname
        
        time = datetime.strptime(time, '%I:%M%p')
        endtime = time + timedelta(minutes=service_length)
        
        self.session.query('''
        INSERT INTO appointment VALUES(
        DEFAULT,
        %(fullname)s,
        %(petname)s,
        %(service)s,
        %(date)s,
        %(time)s,
        %(endtime)s,
        %(email)s,
        %(phone)s,
        1,
        %(comment)s)
        ''', {
            'fullname': fullname,
            'petname': petname,
            'service': service,
            'date': date,
            'time': time,
            'endtime': endtime,
            'email': email,
            'phone': phone,
            'comment': comment
        })
        # if email:
        #     print('EMAIL:', email)
        # send_email(email, comments)
        # self.redirect('/form-success')

        self.set_header(
          'Cache-Control',
          'no-store, no-cache, must-revalidate, max-age=0')
        self.render_template("index.html", {'error': error})


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/services", ServicesHandler),
            (r"/about", AboutHandler),
            (r"/appointment", AppointmentsHandler),
            (r"/reviews(.*)", ReviewsHandler),
            (r"/success(.*)", SuccessHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {
                'path': 'static'
            }),
        ],
        autoreload=True)


if __name__ == "__main__":
    tornado.log.enable_pretty_logging()

    app = make_app()
    PORT = int(os.environ.get('PORT', '8000'))
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()