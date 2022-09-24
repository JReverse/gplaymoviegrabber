#!/usr/bin/env python3
# By JReverse
from mitmproxy import ctx
import re

class GPlayGrabber:
    parts = 0
    def __init__(self):
        ctx.log.warn( "GPlayGrabber class initiated" )
    
    def writefile(self, filename, content):
        ctx.log.warn( "Writing File: {}".format( filename ) )
        with open( filename, "wb" ) as f:
            f.write( content )
        f.close()

    def response(self, flow):
        url = flow.request.path
        matches = re.search( 'videoplayback/id/(\d+)', url )
        if matches:
            self.writefile( str(self.parts) + ".mkv", flow.response.content )
            self.parts += 1

addons = [
    GPlayGrabber()
]
