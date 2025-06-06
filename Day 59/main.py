def header_footer(hf):
    def m_hf(*args , **kwagrs):
        print("\nStory Title:")
        hf(*args, **kwagrs)
        print("The End!")
    return m_hf

# @header_footer
def Story():
    print("How Zayan become a Millionaire")
header_footer(Story)()

@header_footer
def Story2():
    print("How Shafique and Hamdan become a Billionaire")
Story2()



def sum(a , b):
    print(a + b)

header_footer(sum)(1,2)



