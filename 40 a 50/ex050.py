def metro():
    metros = float(input('digite quantos metros voce quer converter: '))
    return metros


def centimetros(metros):
    return metros * 100


def milimitros(metros):
    return metros * 1000

m = metro()
c = centimetros(m)
mm = milimitros(m)

print('metros: ', m)
print('centimetros: ', c)
print('milimitros: ', mm)