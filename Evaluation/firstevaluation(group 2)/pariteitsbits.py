# https://dodona.be/nl/courses/4157/series/46293/activities/204377153

bitstring = input('bit string ')
w = int(input('the packet length w of the protocol '))
parity = input('even if the protocol uses even parity or odd if it used odd parity ')
protocol = input('send if the protocol must send the bitstring or receive if it received the bitstring ')


l = len(bitstring)


if protocol == 'send':

    list_bits = [bitstring[(w - 1) * i:(w - 1) * (i + 1)]
                 for i in range(int(l / (w - 1)))]
    zip_bits = zip(list_bits,[sum([int(i)  for i in list(j)]) for j in list_bits])

    res = []

    if l % (w - 1) != 0:
        print('invalid bitstring')

    elif parity == 'even':
        for b, s in zip_bits:
            res.append(b + '0') if s % 2 == 0 else res.append(b + '1')
        print(''.join(res))

    elif parity == 'odd':
        for b, s in zip_bits:
            res.append(b + '1') if s % 2 == 0 else res.append(b + '0')
        print(''.join(res))

elif protocol == 'receive':
    list_bits = [bitstring[(w) * i:(w) * (i + 1)]
                 for i in range(int(l / (w)))]

    if l % w != 0:
        print('invalid bitstring')

    elif  parity == 'even' and all([sum(int(bit) for bit in bits[:w - 1]) % 2 == int(bits[-1]) for bits in list_bits ])\
            or \
        parity == 'odd' and all([sum(int(bit) for bit in bits[:w - 1]) % 2 != int(bits[-1]) for bits in list_bits]):
        print(''.join([bits[:w - 1] for bits in list_bits]))

    else:
        print('invalid bitstring')

