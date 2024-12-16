import pprint

def introspection_info(other):
    dict_other = {}
    info_tools = [type, dir, id]
    for tools in info_tools:
        result = tools(other)
        dict_other.setdefault(str(tools.__name__), result)
    dict_other['module'] = introspection_info.__module__
    dict_other['attributes'] = [x for x in dir(other) if not callable(getattr(other, x))]
    return dict_other

def_call = introspection_info(42)
pprint.pprint(def_call)