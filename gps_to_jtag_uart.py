import serial
import time
import re
import pyautogui

ARDUINO_PORT = 'COM3'
ARDUINO_BAUD = 9600

current_x = None
current_y = None

def connect_to_arduino():
    try:
        ser = serial.Serial(ARDUINO_PORT, ARDUINO_BAUD, timeout=1)
        print(f"Connected to Arduino on {ARDUINO_PORT}")
        return ser
    except Exception as e:
        print(f"Error connecting to Arduino: {e}")
        return None

def parse_arduino_output(line):
    global current_x, current_y
    
    x_match = re.search(r'startx=(\d+)', line)
    if x_match:
        current_x = int(x_match.group(1))
        print(f"Parsed X coordinate: {current_x}")
    
    y_match = re.search(r'starty=(\d+)', line)
    if y_match:
        current_y = int(y_match.group(1))
        print(f"Parsed Y coordinate: {current_y}")
    
    return current_x is not None and current_y is not None

def send_to_map_program():
    global current_x, current_y
    
    if current_x is None or current_y is None:
        print("Coordinates not available yet")
        return False
    
    coord_string = f"{current_x},{current_y}"
    print(f"Sending coordinates to map program: {coord_string}")
    
    pyautogui.press('enter')
    pyautogui.write(coord_string)
    pyautogui.press('enter')
    
    return True

def main():
    print("GPS Coordinate Bridge - Arduino to Map Program")
    print("Press Ctrl+C to exit")
    
    arduino_serial = connect_to_arduino()
    if not arduino_serial:
        print("Failed to connect to Arduino. Exiting.")
        return
    
    try:
        while True:
            if arduino_serial.in_waiting:
                line = arduino_serial.readline().decode('utf-8', errors='replace').strip()
                print(f"Arduino: {line}")
                
                if parse_arduino_output(line):
                    if current_x is not None and current_y is not None:
                        time.sleep(0.5)
                        send_to_map_program()
                
            time.sleep(0.1)
                
    except KeyboardInterrupt:
        print("\nScript terminated by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if arduino_serial:
            arduino_serial.close()
            print("Arduino connection closed")

if __name__ == "__main__":
    main()