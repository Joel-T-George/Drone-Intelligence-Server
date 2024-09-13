from pymavlink import mavutil
from target_pos import getPos
import time, cv2, os, threading, math, csv

# Start a connection listening on a UDP port
master = mavutil.mavlink_connection('udpin:localhost:14550')

# Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))
# Once connected, use 'the_connection' to get and send messages
lat , lng, rel_alt , yaw_angle, roll, pitch = 0,0,0,0,0,0

def vehicle_location():
    global master , lat, lng,rel_alt, yaw_angle,roll, pitch

while True:
    msg = master.recv_match(type='GPS_RAW_INT', blocking=True)
    if msg is not None:
        latitude = msg.lat/1e7
        longitude = msg.lon/1e7
        altitude = msg.alt/1000.0
        print(f"Latitude: {latitude}, Longitude:{longitude}, Altitude: {altitude}")

    msg = master.recv_match(type='ATTITUDE', blocking=True)
    if msg is not None:
        roll = msg.roll
        pitch = msg.pitch
        yaw = msg.yaw
        print(f"Roll: {roll}, Pitch: {pitch}, Yaw:{yaw}")
    msg = master.recv_match(type='VFR_HUD', blocking=True)

    if msg is not None:
        bearing = msg.heading
        ground_speed = msg.groundspeed
        air_speed = msg.airspeed
        print(f"Bearing: {bearing}, Ground Speed:{ground_speed}, Air Speed: {air_speed}")