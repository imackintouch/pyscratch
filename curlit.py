import pycurl
from io import BytesIO

#headers = StringIO("ggggggggggggggggggggggggg")

headers=BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://netflix.com/')
c.setopt(c.HEADER, 1)
c.setopt(c.NOBODY, 1)
c.setopt(c.HEADERFUNCTION, headers.write)
c.perform()


print(headers.getvalue())
print(c.getinfo(pycurl.HTTP_CODE))

c.close()
