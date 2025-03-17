def print_rangoli(size):
    # your code goes here

    # Upper part of Rangoli
    for i in range(1,size+1): # i is the number of characters in the middle
        back = [chr(ord('a')+size-j-1) for j in range(i)] # Get list of characters from latest to first
        base = back[::-1] # Reverse the list to get complete set of characters to form a line
        back.extend(base[1:]) # Add base to back, but skip the first character
        print('-'.join(back).center(size*4-3, '-')) # Print the line centered with '-' as padding and size*4-3 as width
        
    # Lower part of Rangoli
    for i in reversed(range(1,size)): # same as above, but reversed
        back = [chr(ord('a')+size-j-1) for j in range(i)]
        base = back[::-1]
        back.extend(base[1:])
        print('-'.join(back).center(size*4-3, '-'))


# Test cases
print_rangoli(5) 
print_rangoli(19)