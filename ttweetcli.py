import socket
import sys
import getopt
import threading

unread_subscribed_tweets = []

def listening_for_tweets(s):
    while True:
        data = s.recv(1024)
        print("message recieved")
        if (not data == "b'ack'" and not data == "b'nack'"):
            unread_subscribed_tweets.append(data)

def main(argv):
    host = ''               # The server's hostname or IP address
    port = ''               # The port used by the server
    username = ''
    hashtag = ''            # hashtag string
    valid_commands = (("tweet",3),("subscribe",2),("unsubscribe",2),("timeline",1),("exit",1))
    if( len( sys.argv ) == 1):
        host = '127.0.0.1'
        port = 13069
        username = 'Dril'
    elif( len( sys.argv ) == 4 ):
        host = sys.argv[1]
        port = sys.argv[2]
        username = sys.argv[3]
    else:
        usage()

    if( not username.isalnum() ):
        print( 'Username must only contain letters and numbers' )
        sys.exit(2)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect( ( host, int( port ) ) )
            s.sendall( bytes( str ( ( username ) ), 'utf-8' ) )
            data = s.recv(1024)
        except socket.error as msg:
            socketError( msg )
        print( 'Received', repr( data ) )
        if (repr( data ) == "b'error: username already taken'"):
            print("username already taken")
            sys.exit(2)
        else:
            thread = threading.Thread(target=listening_for_tweets, args=(s,))
            thread.daemon = True
            thread.start()
            while(1):
                message = input()
                command = message
                if (command != ''):
                    command_length = len(command.split())
                    if (command.split()[0] == "tweet"):
                        command_length = len(command.split('"'))
                    if ((command.split()[0], command_length) in valid_commands):
                        if (command.split()[0] == "timeline"):
                            print("timeline: ")
                            for tweet in unread_subscribed_tweets:
                                print(username, tweet)
                        else:
                            s.sendall( bytes( str ( ( command ) ), 'utf-8' ) )
                            if (command.split('""')[0]  == "exit"):
                                sys.exit(0)
                    else:
                        commandUsage()



def commandUsage():
    print ("derp")

def usage():
    print( '\nUsage Error')
    print( 'Usage:$ ./ttweetcl <ServerIP> <ServerPort> <Username>' )
    sys.exit(2)

def messageTooLong():
    print( '\nUsage Error')
    print( 'Messages cannot be longer than 150 charecters, your message is', len( sys.argv[4] ), ' characeters long' )
    sys.exit(2)

def messageCannotBeEmpty():
    print( '\nUsage Error')
    print( 'Messages to be uploaded must not be empty')
    sys.exit(2)

def socketError(msg):
    print( 'Socket Error' )
    print( msg )
    sys.exit(3)

main( sys.argv )
