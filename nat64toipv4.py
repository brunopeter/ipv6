'''
NAT64 to IPv4 Convertor
2023-09-20 v0.3 Peter Bruno

Example:
  64:ff9b::cc4f:c5db
  should result in:
  cc4f:c5db = 204.79.197.219
'''

def nat64toipv4(nat64):
  ipv4 = []
  base16 = 16   # hex (base16) convert to dec

  for nibble in nat64.rsplit(':', 2)[-2:]:
    nibble = nibble.zfill(4)  # ensure each nible is 4 characters, zero pad if necessary
    ipv4.append(str(int(nibble[0:2], base16)))
    ipv4.append(str(int(nibble[2:4], base16)))

  return '.'.join(ipv4)


if __name__ == '__main__':
  print('=== NAT64 -> IPv4 Convertor - [Q]uit ===')
  while True:
    ipv6address = input('Enter nat64 address: ')
    if ipv6address.upper() == 'Q':
      break
    print(nat64toipv4(ipv6address))
