# Reverse_shell
To run a reverse shell (command prompt) of another/other's pc (client)  on our pc (server) 

-----Modules Included-----
1. socket
2. sys
3.threading
4. time
5. queue
6. os
7. subprocess

Essential information--

->In host variable (both in server and client file) you will assign IP address of platform on which you are hosting your server.

->Since the IP address of our PC is often variable (when we restart our PC) so, to write IP address of your PC in host will became meaningless .

->To avoid changing of IP address you should host server file on online platform (eg. Digital Ocean) because its IP address is constant.

->In place of host='###.###.##.###' in each client and server file write host=' IP address of server on Digital Ocean' 

->Then give client.py file to your friend's PC and tell him to run that python file after you run server.py file . 
  
There are two folder 
One for connecting only one client.
Other for connecting multiple client.


Note--
If you don't want to host on digital ocean , You can run locally BUT when you restart our pc your IP address may chance so it will only work untill your IP is not changing.
