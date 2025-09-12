from mitmproxy import ctx, http

def load(loader):
    loader.add_option(
        name="validate_headers",
        typespec=bool,
        default=True,
        help="Validate request headers to prevent request smuggling attacks",
    )


def configureupdated(config):
    if config.validate_headers:
        ctx.master.addons.add(validate_headers())


class validate_headers:
    def __init__(self):
        self.seen_headers = {}

    def http_connect(self, flow):
        self.validate(flow)

    def request(self, flow):
        self.validate(flow)

    def validate(self, flow):
        for k, v in flow.request.headers.items():
            k_lower = k.lower()
            if k_lower in self.seen_headers:
                raise ValueError(f"Duplicate header {k}")
            self.seen_headers[k_lower] = True

            # Content-Length should be an integer
            if k_lower == 'content-length':
                try:
                    int(v[0])
                except ValueError:
                    raise ValueError(f"Invalid Content-Length header: {v[0]}")

            # Transfer-Encoding should be one of 'chunked', 'compress', 'deflate', 'gzip', 'identity'
            if k_lower == 'transfer-encoding':
                allowed_encodings = ['chunked', 'compress', 'deflate', 'gzip', 'identity']
                if v[0].lower() not in allowed_encodings:
                    raise ValueError(f"Invalid Transfer-Encoding header: {v[0]}")

            # TE should be one of 'trailers', 'chunked', 'compress', 'deflate', 'gzip'
            if k_lower == 'te':
                allowed_encodings = ['trailers', 'chunked', 'compress', 'deflate', 'gzip']
                if v[0].lower() not in allowed_encodings:
                    raise ValueError(f"Invalid TE header: {v[0]}")
