from string import ascii_lowercase

def is_isogram(string):
    # iso = None
    # while iso == None:
        # for i in string.lower():
        #     if i in ascii_lowercase:
        #         if string.count(i) > 1:
        #             return False
        for i in ascii_lowercase:
            if string.lower().count(i) > 1:
                return False
        return True        


# print('thumbscrew-jAppingly'.lower().split('-'))