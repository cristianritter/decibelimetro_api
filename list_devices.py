import hid
vendor_id = 25789
product_id = 29923
def list_hid_paths():
    try:
        devices = hid.enumerate(vendor_id, product_id)
        if devices:
            paths_list = []
            for device in devices:
                #print(f"Vendor ID: {device['vendor_id']}, Product ID: {device['product_id']}")
                #print(f"Manufacturer: {device['manufacturer_string']}, Product: {device['product_string']}")
                print(f"Serial Number: {device['serial_number']}, Path: {device['path']}")
                #print("----")
                paths_list.append(device['path'])
            return paths_list
        else:
            print("No HID devices found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    list_hid_paths()
