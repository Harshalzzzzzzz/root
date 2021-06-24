# Authors:
# * Hinnerk C. Schmidt 02/2021
# * Jonas Rembser 06/2021
# * Harshal Shende 06/2021

################################################################################
# Copyright (C) 1995-2020, Rene Brun and Fons Rademakers.                      #
# All rights reserved.                                                         #
#                                                                              #
# For the licensing terms see $ROOTSYS/LICENSE.                                #
# For the list of contributors see $ROOTSYS/README/CREDITS.                    #
################################################################################


def _getter(k, v):
    # helper function to get CmdArg attribute from `RooFit`
    # Parameters:
    # k: key of the kwarg
    # v: value of the kwarg

    # We have to use ROOT here and not cppy.gbl, because the RooFit namespace is pythonized itself.
    import ROOT

    func = getattr(ROOT.RooFit, k)

    if func.__class__.__name__ == "CPPOverload":
        if "()" in func.func_doc:
            if not isinstance(v, bool):
                raise TypeError("The keyword argument " + k + " can only take bool values.")
            return func() if v else ROOT.RooCmdArg.none()

    if isinstance(v, (tuple, list)):
        return func(*v)
    elif isinstance(v, (dict,)):
        return func(**v)
    else:
        return func(v)


def _kwargs_to_roocmdargs(*args, **kwargs):
    """Helper function to check kwargs and pythonize the arguments using _getter"""
    if kwargs:
        args = args + tuple((_getter(k, v) for k, v in kwargs.items()))
    return args, {}


def _string_to_root_attribute(value, _lookup_map):
    import ROOT

    if isinstance(value, str):
        if value in _lookup_map:
            return getattr(ROOT, _lookup_map[value])
        else:
            try:
                return getattr(ROOT, value)
            except:
                raise ValueError(
                    "Unsupported value passed. The value either has to be the name of an attribute of the ROOT module, or match with one of the following values that get translated to ROOT attributes: {}".format(
                        _lookup_map
                    )
                )
    elif isinstance(value, int):
        return value


def _decaytype_string_to_enum(caller, kwargs):
    """Helper function to pythonize DecayType enums and check for enum value names."""
    type_key = "type"

    if type_key in kwargs:
        val = kwargs[type_key]
        if isinstance(val, str):
            try:
                kwargs[type_key] = getattr(caller.__class__, val)
            except AttributeError as error:
                raise ValueError(
                    "Unsupported decay type passed to "
                    + caller.__class__.__name__
                    + ". Supported decay types are : 'SingleSided', 'DoubleSided', 'Flipped'"
                )
            except Exception as exception:
                raise exception

    return kwargs
