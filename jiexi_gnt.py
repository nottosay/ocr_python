#!/usr/bin/python
import struct
import Image
import os

count = 0
path = 'D:/HandWriting/test_data/'

for z in xrange(1241, 1301):
    ff = 'D:/HWDB1.1tst_gnt/' + str(z) + '-c.gnt'
    f = open(ff, 'rb')
    while f.read(1) != "":
        f.seek(-1, 1)
        global count
        count += 1
        length_bytes = struct.unpack('<I', f.read(4))[0]
        print
        length_bytes
        tag_code = f.read(2)
        print
        tag_code
        width = struct.unpack('<H', f.read(2))[0]
        print
        width
        height = struct.unpack('<H', f.read(2))[0]
        print
        height

        im = Image.new('RGB', (width, height))
        img_array = im.load()
        for x in xrange(0, height):
            for y in xrange(0, width):
                pixel = struct.unpack('<B', f.read(1))[0]
                img_array[y, x] = (pixel, pixel, pixel)
        filename = str(count) + '.png'
        print
        filename
        if (os.path.exists(path + tag_code)):
            filename = path + tag_code + '/' + filename
            im.save(filename)
        else:
            os.makedirs(path + tag_code)
            filename = path + tag_code + '/' + filename
            im.save(filename)
    f.close()
