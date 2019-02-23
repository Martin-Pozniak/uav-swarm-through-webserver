xterm -hold -title "server" -e "python server.py" &
xterm -hold -title "master" -e "python master.py" &
xterm -hold -title "slave 1" -e "python slave1.py" &
xterm -hold -title "slave 2" -e "python slave2.py"
