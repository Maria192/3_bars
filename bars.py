import json
import math

def load_data():
    size = {}
    loc = {}
    with open('Бары.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
        data = json.load(fh)
        #write(data)
        for key in data:
            for elem in key:
                if elem == 'Cells':
                    for dat in key[elem]:
                        if dat == 'Name':
                            name = key[elem][dat]
                        elif dat == 'SeatsCount':
                            seats = key[elem][dat]
                        elif dat == 'geoData':
                            for wrd in key[elem][dat]:
                                if wrd == 'coordinates':
                                    coord = key[elem][dat][wrd]
                                    
                    size[name] = seats
                    loc[name] = coord
        
    get_biggest_bar(size)
    get_closest_bar(loc)
                        
                        
    


def get_biggest_bar(size):
    biggest = 0
    smallest = 1000
    nameb = ''
    names = ''
    for key in size:
        if int(size[key]) > biggest:
            biggest = int(size[key])
            nameb = key
        if int(size[key]) < smallest:
            smallest = int(size[key])
            names = key
    print ('Самый большой: ' + nameb)
    print ('Самый маленький: ' + names)





def get_closest_bar(loc):
    sh = float(input('Широта: '))
    d = float(input('Долгота: '))


    sh = sh*math.pi/180
    d = d*math.pi/180

    minim = 100
    name = ''

    for key in loc:
        sh1 = loc[key][1]*math.pi/180
        d1 = loc[key][0]*math.pi/180
        dist = math.acos(math.sin(sh)*math.sin(sh1) + math.cos(sh)*math.cos(sh1)*math.cos(d-d1))
        dist = dist*6371
        if dist < minim:
            minim = dist
            name = key
    print ('Самый близкий: ' + name)



def main():
    load_data()

    
if  __name__ == '__main__':
    main()
