import regex as r

def main():

    return print(validate(input('IPv4 Address:')))


def validate(ip):

    #   Regular expression to match the range of an IPV4 address
    regex = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'

    #   Split the IPV4 address into segments
    ipv4 = [i for i in str(ip).split('.')]
    
    try:

        for segment in ipv4:
            
            #   Ensure that the segment is a number and that it is within the range of 0-255
            if not r.match(regex, segment):
                raise Exception()
        

    except Exception:
        return False
    
    return True



if __name__ == "__main__":
    main()
