def SET_bit(value, bit):
    return value | (1<<bit)
def CLR_bit(value, bit):
    return value & ~(1<<bit)
def TOG_bit(value, bit):
    return value  ^(1<<bit)
def GET_bit(value, bit):
    return   (value>>bit)
