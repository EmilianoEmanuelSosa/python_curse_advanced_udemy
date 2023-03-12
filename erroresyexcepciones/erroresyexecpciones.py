while True:
    try:
        age=int(input('Tell me your Age'))
        print('Your Ageg is: ',age)
        break
    except ValueError:
        print('Introduce a number')
    finally:
        print('The process is end')
        break
