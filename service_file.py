def Str_(*args,**kwargs):
    str= ''
    if len(args) != 0:
        if len(kwargs) != 0:
            for p in args:
                str += f"{p}; "
            for key,val in kwargs.items():
                str+= f"{key} = {val};"
            return str
        else:
            for p in args:
                str += f"{p}; "
            return str
    elif len(kwargs) != 0:
        for key,val in kwargs.items():
            str+= f"{key} = {val}; "
        return str
    else:
        return '-'
