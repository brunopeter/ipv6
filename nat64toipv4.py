'''
NAT64 to IPv4 Convertor
2023-04-26 v0.2 Peter Bruno

Example:
  64:ff9b::cc4f:c5db
  should result in:
  cc4f:c5db = 204.79.197.219
'''

def nat64toipv4(nat64):
  ipv4 = []
  for nibble in nat64.rsplit(':', 2)[1:3]:
    # ensure each nible is 4 characters, zero pad if necessary
    nibble = nibble.zfill(4)
    # loop through nibbles, convert from hex to bin
    for x in [0,2]:
      ipv4.append(str(int(nibble[x:x+2],16)))

  return '.'.join(ipv4)


if __name__ == '__main__':
  print('=== NAT64 - IPv4 Convertor ===')
  addr = input('Enter nat64 address: ')

  print(nat64toipv4(addr))
