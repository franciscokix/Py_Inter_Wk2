#Test __pychache__
if __name__ == '__main__':
    #import libraries
    import time
    #define vars
    frank_list = []
    #prompt for final number
    try:
        final_number = int(input('Enter final number: '))
    except: 
        print('Please enter an integer.  Exiting...')
        time.sleep(3)
        exit()

    for i in range (0,final_number,2):
        frank_list.append(i)

print(f'list of even numbers from 0 to {final_number}: \n{frank_list}')
