#Test __pychache__
if __name__ == '__main__':
    import os
    frank_list = []

    for i in range (0,5):
        frank_list.append(i)

current_dir = os.curdir
print(frank_list)
print(current_dir)   
