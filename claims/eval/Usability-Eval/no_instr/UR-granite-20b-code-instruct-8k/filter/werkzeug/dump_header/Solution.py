from werkzeug.http import dump_header

header = ('Content-Type', 'text/plain')
dumped_header = dump_header(header[0], header[1])
print(dumped_header)
