'''mr z is selected for olympics he is participating in swimming competition only one
winner is selected in th e competition MR X mr y are friends of z mr x is part badmint mr y in table tennies,according to the selection commite the
require of badmintion height 140 cmp weight faactors of 2 body fat < than 12% according to selection committee
require table tennies height min 118 cm to 148cm weight factors of no of medals won by mr z body fat 14%
according to previous history z participated in 14 games out which he is hvaing success rate of 65%'''

z=True
h1=int(input())
w1=int(input())
body_fat1=int(input())
if(h1>140 and w1%2==0 and body_fat1<12):
    print("x is selected")
    x=True
h2=int(input())
w2=int(input())
body_fat2=int(input())
if((h2>=118 and h2<=148)  and w2%7==0 and body_fat2<14):
    print("y is selected")
    y=True
if(x==True and y==True and z==True):
    print("All three are travelling in same plane")
else:
    print("No")


