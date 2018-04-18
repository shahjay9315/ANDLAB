import getpass
import telnetlib

user=raw_input("Enter your uername:")
password=getpass.getpass()
HOST=("192.168.30.131","192.168.30.135","192.168.30.134")


for i in HOST:
   print("\n\nconecting to " +i)
   tn = telnetlib.Telnet(i,timeout = 15)
   if  i is  "192.168.30.131":
   tn.read_until("Username:")
   tn.write(user+ "\n")

   if password:
      tn.read_until("Password:")
      tn.write(password +"\n")
      tn.write("conf t\n")
            tn.write("int lo 0 \n")

                               [ Read 54 lines ]








