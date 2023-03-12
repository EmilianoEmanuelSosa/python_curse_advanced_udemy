while True:
    try:
        num1=int(input('Introduce a number'))
        resultado= 100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print('\ncannot be divided by zero ')
    except ValueError:
        print('\nNot is a number')
    except KeyboardInterrupt:
        print('\nyou have stopped the execution')
    finally:
        print('the process is end')


