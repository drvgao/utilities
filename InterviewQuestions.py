# how to generate random elements from list using random.choice method
import random
foo = [1,2,5,6,7]
random_element = random.choice(foo)
print('random_element', random_element)

# with secrets module

# with randrange


# Don't do this msg=’hello’+mymsg+’world’. instead try below
msg=’hello %s world’ % mymsg

#Don't
# mymsg=’line1\n’
# mymsg+=’line2\n’

mymsg=[‘line1’,’line2']
‘\n’.join(mymsg)
       
# https://towardsdatascience.com/memory-management-in-python-6bea0c8aecc9#:~:text=The%20Python%20memory%20manager%20manages%20chunks%20of%20memory%20called%20%E2%80%9CBlocks,object%20of%20the%20same%20size.     
