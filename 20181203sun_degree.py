# from 6:00 to 18:00 means from 0°to 180°

def get_sun_degree(time:str):
    mins = (int(time[:2]) - 6)*60 + int(time[3:])
    if int(time[:2]) >= 6 and int(time[:2]) < 18:
        if str(mins*0.25)[2:] == '.0' or str(mins*0.25)[1:] == '.0':
            return int(str(mins*0.25).rsplit('.0')[0])
        return mins*0.25
    elif int(time[:2]) == 18 and int(time[3:])==0:
        return 180
    else:
        return 'I don\'t see the sun!'


if __name__ == '__main__':
    a = get_sun_degree('17:59')
    print(a)
