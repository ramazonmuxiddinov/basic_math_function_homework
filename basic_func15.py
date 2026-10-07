def main(a, b):
    '''A soni b ga bo'linganda qoldiqni toping va uning 3 darajasini hisoblab qaytaring.
    
     Args:
     a (int): raqam
     b (int): raqam
    
     Qaytaradi:
     int: natija.
     '''
    import math
    return pow(a%b,3)
print(main(23,5))
