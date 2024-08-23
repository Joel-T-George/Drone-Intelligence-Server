# import trio


# async def sendGimbal(command, server):
#     bytesCommand = bytes.fromhex(command)
#     udp_socket = trio.socket.socket(trio.socket.AF_INET, trio.socket.SOCK_DGRAM) 
#     await udp_socket.sendto(bytesCommand,server)

#     response, _ = await udp_socket.recvfrom(1024)

#     print("Recevied",response)


# trio.run(sendGimbal)


import socket



