from flask import Flask, render_template, redirect, url_for,send_from_directory
import xml.etree.ElementTree as ET
from werkzeug.serving import run_simple

app = Flask(__name__)

lst = [
    {'title':'جرائم', 'content':'1.html' , 'route':'جرائم', 'date':'2024-04-06', 'category':'قوانین', 'image':"Law-of-tax-crimes.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html', lst=lst)

@app.route('/blog/<route>')
def blog(route):
    target_dic = filter(lambda item: item['route'] == route, lst)
    result = next(target_dic, None)
    if result:
        return render_template('blog.html', dic=result)
    return redirect(url_for('blogs'))

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    base_url = 'https://ibarge.work'
    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    #index
    page = ET.SubElement(root, "url")
    loc = ET.SubElement(page, "loc")
    loc.text = base_url
    lastmod = ET.SubElement(page, "lastmod")
    lastmod.text = '2024-04-06'
    changefreq = ET.SubElement(page, "changefreq")
    changefreq.text = 'weekly'
    priority = ET.SubElement(page, "priority")
    priority.text = '1'
    #blogs
    page = ET.SubElement(root, "url")
    loc = ET.SubElement(page, "loc")
    loc.text = base_url+'/blogs'
    lastmod = ET.SubElement(page, "lastmod")
    lastmod.text = '2024-04-06'
    changefreq = ET.SubElement(page, "changefreq")
    changefreq.text = 'weekly'
    priority = ET.SubElement(page, "priority")
    priority.text = '0.75'
    for url in lst:
        page = ET.SubElement(root, "url")
        loc = ET.SubElement(page, "loc")
        loc.text = base_url+'/blog/'+url['route']
        lastmod = ET.SubElement(page, "lastmod")
        lastmod.text = url['date']
        changefreq = ET.SubElement(page, "changefreq")
        changefreq.text = 'monthly'
        priority = ET.SubElement(page, "priority")
        priority.text = '0.5'
    sitemap_xml = ET.tostring(root, encoding='utf-8')
    # برگرداندن رشته به عنوان پاسخ
    return sitemap_xml, {'Content-Type': 'application/xml; charset=utf-8'}

if __name__ == '__main__':
    run_simple('0.0.0.0', 8443, app, use_reloader=False, threaded=True)
    # app.run(debug=True, host='0.0.0.0' , port=8443)
