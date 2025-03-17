def print_formatted(number):
    # your code goes here
    n_oct = [oct(n).lstrip("0o") for n in range(1,number+1)]
    n_hex = [hex(n).lstrip("0x").upper() for n in range(1,number+1)]
    n_bin = [bin(n).lstrip("0b") for n in range(1,number+1)]
    
    max_l = len(n_bin[-1])
   
    
    for i in range(1,number+1):
        print(f"{str(i).rjust(max_l)} {n_oct[i-1].rjust(max_l)} {n_hex[i-1].rjust(max_l)} {n_bin[i-1].rjust(max_l)}")
    
    #print(max_l)
    #print(f"{n} {oct(n).lstrip("0o"):>} {hex(n).lstrip("0x"):>} {bin(n).lstrip("0b"):>}")


n = int(input())
print_formatted(n)

