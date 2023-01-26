import argparse

args = argparse.ArgumentParser(description="coba entry")

args.add_argument("-c","--port",help="port number")
args.add_argument("-s","--hostname",help="hostname database")
args.add_argument("-u","--username",help="username database")
args.add_argument("-p","--password",help="password database")

args = args.parse_args()

print("this database is {hostname} with port {port} whose {username} and the password is {password}".format(hostname=args.hostname,port=args.port,username=args.username,password=args.password))