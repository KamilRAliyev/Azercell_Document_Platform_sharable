import socket

from .base import *

from .production import *   

if socket.gethostname() ==  'kamil-KLV-WX9':
    from .local import *
