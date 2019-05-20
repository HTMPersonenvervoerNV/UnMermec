#!/usr/bin/env python2

import sys
import re
from struct import unpack
from exif import set_gps_location

f = open(sys.argv[1], 'rb')
all = f.read()
counter = 1

start_of_image = [m.start() for m in re.finditer('\xff\xd8', all)]
end_of_image = [m.start() for m in re.finditer('\xff\xd9', all)]

for x in range(0, len(start_of_image)):
    lat, lon, distM = unpack('ddI', all[start_of_image[x] - 316:start_of_image[x]][212:232])
    filename = ('/tmp/%03d.jpg' % counter)
    with open(filename, 'w') as w:
        w.write(all[start_of_image[x]:(end_of_image[x]+2)])
        w.close()
    set_gps_location(filename, lat, lon)

    counter += 1

