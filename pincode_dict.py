d1={'rajasthan':101,'Haryana':102}
d2={'assam':103}
d1.update(d2)
print(d1)

d={}.fromkeys(d1)
print(d)

d3={'Goa':104}
d1.update(d3)
print(d1)