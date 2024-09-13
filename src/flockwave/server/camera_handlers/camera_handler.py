import socket
import time

from .control_commands import stop ,zoom_stop
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def camera_controller(msg, cameraip):
    global sock
    sock.sendto(msg, (cameraip, 14551))
    time.sleep(0.5)
    sock.sendto(bytes.fromhex(stop),(cameraip, 14551))
    return True

def camera_controll_zoom(msg,cameraip):
    global sock
    sock.sendto(msg,(cameraip,14551))
    time.sleep(0.5)
    sock.sendto(bytes(zoom_stop), (cameraip,14551))
    return True