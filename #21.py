import textwrap
def wrap(string, max_width):
    s = string
    w = max_width
    a = textwrap.wrap(s,w)
    b = ' '.join(a)
    c = textwrap.fill(b,w)
    return  c