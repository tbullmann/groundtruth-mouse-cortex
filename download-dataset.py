from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    from urllib.request import urlopen # python 3
except ImportError:
    from urllib2 import urlopen # python 2
import sys
import zipfile
import tempfile
import shutil

dataset = sys.argv[1]
try:
    path = sys.argv[2]
except IndexError:
    path ='.'

url = "http://brainiac2.mit.edu/SNEMI3D/sites/default/files/%s.zip" % dataset
with tempfile.NamedTemporaryFile() as tmp:
    print("downloading", url)
    shutil.copyfileobj(urlopen(url), tmp)
    print("extracting")
    tmp.seek(0)
    tar = zipfile.ZipFile(tmp.name, 'r')
    tar.extractall(path=path)
    tar.close()
    print("done")
