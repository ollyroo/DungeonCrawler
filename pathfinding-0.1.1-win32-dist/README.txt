Path Finding Demo 0.1.1

Something I found
run server then client



Project HomePage: 
    http://code.google.com/p/mycodeplayground/

Code License:
    MIT License

Author: 
    Xueqiao Xu <xueqiaoxu@gmail.com>
    http://about.me/xueqiaoxu

Desciption:
    This is a demo visualizing the execution of various path finding algorithms.

    Curently five algorithms are included:
        1. A* (using Manhattan distance)
        2. A* (using Euclidean distance)
        3. A* (using Chebyshev distance)
        4. Dijkstra 
        5. Bi-Directional Breadth-First-Search 

    This is a Client/Server application. You should start the server first 
    and then the client. 
    Also, you can start the server on one machine and run the client on a 
    different machine, as long as the two machines are connected. 
    Meanwhile, The server is capable of handling multiple concurrent requests. 

Usage:
    Simply double click on server.exe and client.exe

    By default, the server starts on 127.0.0.1(localhost) and uses the 
    port 31416.
    If you want to specify another port, add options while executing
    the server.py. This can be done by either executing the program in cmd
	or executing it via a modified shortcut.
    For example:
        server.exe -p 27183
    
    As stated in the description section above, you can start the server on
    one machine and start the client on another machine, as long as these
    two machines are connected. If you want to connect to a remote server,
    add options while executing the client.
    For example:
        python client.exe -a 172.18.241.2 -p 27183

Updates:
    version 0.1.1 Feb 17 2011
    Add: If client fails to connect to the server, it will continuously 
         attemp to connect every 5 seconds. Related Notification is also added.
    Add: Window icons.
    Fix: Asynchat related message queue issue.
    Fix: Working directory related issue.
    Chg: Refactored some codes, and added more documents and comments.

    version 0.1.0 Feb 12 2011
    First version of Path Finding
