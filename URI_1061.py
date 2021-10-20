import datetime


def main():
    day = int(input().split()[1])
    hour = input().split()
    date0 = datetime.datetime(
        2020,
        4,
        day,
        int(hour[0]),
        int(hour[2]),
        int(hour[4]),
        0
    )

    day = int(input().split()[1])
    hour = input().split()
    date1 = datetime.datetime(
        2020,
        4,
        day,
        int(hour[0]),
        int(hour[2]),
        int(hour[4]),
        0
    )

    time_delta = date1 - date0
    print(time_delta.days, 'dia(s)')
    tim = time_delta.seconds
    hora = tim // (60 * 60)
    print(hora, 'hora(s)')
    tim = tim - ((60 * 60) * hora)
    minutos = tim // 60
    print(minutos, 'minuto(s)')
    tim = tim - (60 * minutos)
    print(tim, 'segundo(s)')


if __name__ == '__main__':
    main()
