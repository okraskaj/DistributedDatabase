import os

def make_tree(path=""):
    tree = dict(name=path, children=[])
    try: lst = os.listdir(path)
    except OSError:
        # print(OSError.strerror)
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=fn))
    return tree
print(os.getcwd())
print(make_tree('static'))

