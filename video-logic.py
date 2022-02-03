from server import Server

# a bunch of video stuff
server = Server(8080)
while True:
    #
    server.put_point((100, 200))