thickness = int(input()) #This must be an odd number
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).rjust(thickness-4))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness+2)+(c*thickness).rjust(thickness*4))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).rjust(thickness*5+2).rjust(thickness))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness+2)+(c*thickness).rjust(thickness*4))

for i in range(thickness):
    print((c*(thickness-i-1)).rjust(thickness).rjust(thickness*5-1)+c+(c*(thickness-i-1)))
#
# print('H'.rjust(5))
# print('H'.rjust(4)+'H'*2)
# print('H'.rjust(3)+'H'*4)
# print('H'.rjust(2)+'H'*6)
# print('H'.rjust(1)+'H'*8)