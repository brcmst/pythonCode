#generator carpım tablosu ornegi

def carpım_tabl():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpım_tabl():
    print(i)
