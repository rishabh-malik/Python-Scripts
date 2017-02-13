import webbrowser;
import sys;
address=input();
if len(sys.argv)>1:
     address=''.join(sys.argv[1:])
webbrowser.open('https://www.google.co.in/maps/place/'+address)
