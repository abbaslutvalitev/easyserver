# easyserver
A good and simple python server for sites and projects where a server is needed
# Short description
Today there are few good, simple and convenient server clients. Therefore easyserver was created. You can make a website on it exclusively with html and javascript or css. The entire server side is performed by easyserver.
# Install
For easyserver you need: Python (preferably above 3.8) if you have python 2 then easyserver will not work. For linux you will also need the following command: python3 -m http.server --cgi. Now for installation. Add the command: git clone https: / /github.com/abbaslutvalitev/easyserver Then open the easyserver folder and find the usage.txt file and follow the instructions there
# Working with easyserver
Execute these commands which were mentioned above

[![Screen-Shot-2021-11-21-at-15-28-18.png](https://i.postimg.cc/VNqWtzqK/Screen-Shot-2021-11-21-at-15-28-18.png)](https://postimg.cc/Z9qNttDN)

After you have completed these commands, you can start working
I created a folder where there is an index.html file also I installed easyserver

[![Screen-Shot-2021-11-21-at-15-34-30.png](https://i.postimg.cc/0jnk3WTY/Screen-Shot-2021-11-21-at-15-34-30.png)](https://postimg.cc/MfcJfDKH)

Following the instructions in the usage .txt file, move "easyserver .py" to your project folder.

[![Screen-Shot-2021-11-21-at-15-36-43.png](https://i.postimg.cc/NMPb4BMm/Screen-Shot-2021-11-21-at-15-36-43.png)](https://postimg.cc/Q91pNLcd)

Now open a terminal or cmd and enter the following command:
python easyserver.py

[![Screen-Shot-2021-11-21-at-15-42-54.png](https://i.postimg.cc/DwvTHP66/Screen-Shot-2021-11-21-at-15-42-54.png)](https://postimg.cc/w7GZsJSR)

Hit enter, enter ip and port. You are done messing with easyserver! Now go to the address in the "Server runned at" message and check
If you have this error:
Traceback (most recent call last):
  File "easyserver.py", line 4, in <module>
    ip = input("Enter the server ip! For example: localhost: ")
  File "<string>", line 1, in <module>
NameError: name 'localhost' is not defined
Run the "easyserver.py" in vscode or thonny

[![Screen-Shot-2021-11-21-at-15-49-06.png](https://i.postimg.cc/pLb9F42T/Screen-Shot-2021-11-21-at-15-49-06.png)](https://postimg.cc/0bn2gtKR)
  
Lets test!We go to the received url address and see that our html file is displayed!

[![Screen-Shot-2021-11-21-at-15-51-46.png](https://i.postimg.cc/nzC7kmNc/Screen-Shot-2021-11-21-at-15-51-46.png)](https://postimg.cc/TLvp2KRZ)
