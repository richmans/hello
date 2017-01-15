#Where's the raspberry?
I got a bit tired of using nmap and dhcp logs to find my raspberry pi when i plugged it into a network. This pair of scripts solve that problem. Start findme.py on the raspberry, and it will respond with its hostname to a UDP broadcast sent by the search.py script.

I use crontab to start the findme.py script on the raspberry:

    @reboot ~/hello/findme.py
    
Then, i can search for the raspberry from my laptop:

    $ ./search.py
    Sending broadcast: Hello?
    Got response from 192.168.2.30: Hello, i am stan
    $
    
### Why aren't you using <some other technology>?
Because i couldn't find a simple solution for this problem within 30 minutes, and i love programming sockets!
