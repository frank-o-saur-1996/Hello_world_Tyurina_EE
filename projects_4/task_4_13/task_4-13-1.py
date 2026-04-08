A, B, C, D = (int(input()), int(input()), int(input()), int(input()))
if A > B:
    if A > C:
        if A > D:
            print (f'max = {A}')
        else:
            print (f'max = {D}')
    elif C > D:
        print (f'max = {C}')
    else:
        print (f'max = {D}')
elif B > C:
    if B > D:
        print (f'max = {B}')
    else:
        print (f'max = {C}')
elif C > D:
    print (f'max = {C}')
else:
    print (f'max = {D}')