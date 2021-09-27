import socket
import struct


def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    # listener to listen for network data
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mc, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mc, eth_proto))

# unpack ethernate frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_address(dest_mac), get_mac_address(src_mac), socket.htons(proto), data[14:]


def get_mac_address(bytes_addr):
    bytes_str = map('{:2x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()


main()