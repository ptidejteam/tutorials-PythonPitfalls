from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn


class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass
