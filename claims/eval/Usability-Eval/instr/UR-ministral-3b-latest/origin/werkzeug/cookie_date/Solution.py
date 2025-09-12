from werkzeug import formats

d = formats.date_format(today.datetime.now(), '%a, %d %b %Y %H:%M:%S GMT')

print(d)
