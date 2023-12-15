


import hid
import time
from list_devices import list_hid_paths

vendor_id = 25789
product_id = 29923
# Data to send to the HID device
request_data = bytes.fromhex("00B38130763C7F3076")

def open_hid_device(vendor_id, product_id):
    try:
        device = hid.device()
        device.open(vendor_id, product_id)
        return device
    except Exception as e:
        print(f"Error opening HID device: {str(e)}")
        return None

def close_hid_device(device):
    if device:
        device.close()

def write_data_to_hid(device, data_to_send):
    try:
        if device:
            bytes_written = device.write(data_to_send)
            #print(f"Sent data: {data_to_send}")
            #print(f"Bytes written: {bytes_written}")
    except Exception as e:
        print(f"Error writing data to HID device: {str(e)}")

def request():
    # Open the HID device
    sound_lvl = []
    hid_paths = list_hid_paths()
    device = hid.device()
    if not hid_paths:
        return []
    for idx, hid_path in enumerate(hid_paths):
        data = None
        print(hid_path)
        device.open_path(hid_path)
        write_data_to_hid(device, request_data)
        wg = time.time()
        while not data:
            if time.time() > wg+2: break
            data = device.read(8)  # You may need to adjust the buffer size
        if data:
            print(f"Received data: {data}")
            calc = ((data[0]<<8) + data[1])/10
            sound_lvl.append(calc)
            if idx > 0:
                if sound_lvl[idx]==sound_lvl[idx-1] or sound_lvl[idx-1]==0:
                    sound_lvl[idx]=0                
        # Close the HID device (This code may not be reached if you terminate the program externally)
        close_hid_device(device)
    return sound_lvl


if __name__ == "__main__":

    request() 


   