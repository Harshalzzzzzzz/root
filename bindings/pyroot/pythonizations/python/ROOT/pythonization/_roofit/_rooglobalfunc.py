# Authors:
# * Jonas Rembser 06/2021
# * Harshal Shende 06/2021

################################################################################
# Copyright (C) 1995-2020, Rene Brun and Fons Rademakers.                      #
# All rights reserved.                                                         #
#                                                                              #
# For the licensing terms see $ROOTSYS/LICENSE.                                #
# For the list of contributors see $ROOTSYS/README/CREDITS.                    #
################################################################################


r"""
/**
\class RooGlobalFunc
\brief \parblock \endparblock
\htmlonly
<div class="pyrootbox">
\endhtmlonly

## PyROOT

Some member functions of RooGlobalFunc that take a RooCmdArg as argument also support keyword arguments.
So far, this applies to FitOptions, Format, Frame, MultiArg, YVar and ZVar.

# Directly passing a RooCmdArg:
ROOT.RooMCStudy(model, ROOT.RooArgSet(x), ROOT.RooFit.FitOptions=(ROOT.RooFit.Save(True), ROOT.RooFit.PrintEvalErrors(0)))

# With keyword arguments:
ROOT.RooMCStudy(model, ROOT.RooArgSet(x), FitOptions=dict(Save=True, PrintEvalErrors=0))

\htmlonly
</div>
\endhtmlonly
*/
"""

from ._utils import _kwargs_to_roocmdargs, _string_to_root_attribute

RooFit = None

# Color and Style dictionary to define matplotlib conventions
_color_map = {
    "r": "kRed",
    "b": "kBlue",
    "g": "kGreen",
    "y": "kYellow",
    "w": "kWhite",
    "k": "kBlack",
    "m": "kMagenta",
    "c": "kCyan",
}
_linestyle_map = {"-": "kSolid", "--": "kDashed", ":": "kDotted", "-.": "kDashDotted"}


def _RooFit():
    """Does lazy import of RooFit namespace and then returns it.
    We can't do `from cppyy.gbl import RooFit` directly, because then we would
    see the RooFit banner every time pyROOT is initialized.
    Code inspired by:
    https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Import_Statement_Overhead
    """
    global RooFit
    if RooFit is None:
        from cppyy.gbl import RooFit
    return RooFit


def FitOptions(*args, **kwargs):
    # Redefinition of `FitOptions` for keyword arguments.
    # The keywords must correspond to the CmdArg of the `FitOptions` function.
    args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
    return _RooFit()._FitOptions(*args, **kwargs)


def Format(*args, **kwargs):
    # Redefinition of `Format` for keyword arguments.
    # The keywords must correspond to the CmdArg of the `Format` function.
    if "what" in kwargs:
        args = (kwargs["what"],) + args
        del kwargs["what"]
    args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
    return _RooFit()._Format(*args, **kwargs)


def Frame(*args, **kwargs):
    # Redefinition of `Frame` for keyword arguments.
    # The keywords must correspond to the CmdArg of the `Frame` function.
    args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
    return _RooFit()._Frame(*args, **kwargs)


def MultiArg(*args, **kwargs):
    # Redefinition of `MultiArg` for keyword arguments.
    # The keywords must correspond to the CmdArg of the `MultiArg` function.
    args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
    return _RooFit()._MultiArg(*args, **kwargs)


def YVar(*args, **kwargs):
    # Redefinition of `YVar` for keyword arguments.
    # The keywords must correspond to the CmdArg of the `YVar` function.
    if "var" in kwargs:
        args = (kwargs["var"],) + args
        del kwargs["var"]
    args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
    return _RooFit()._YVar(*args, **kwargs)


def ZVar(*args, **kwargs):
    # Redefinition of `ZVar` for keyword arguments.
    # The keywords must correspond to the CmdArg of the `ZVar` function.
    if "var" in kwargs:
        args = (kwargs["var"],) + args
        del kwargs["var"]
    args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
    return _RooFit()._ZVar(*args, **kwargs)


def LineColor(color):
    # Redefinition of `LineColor` for matplotlib conventions and string arguments.
    return _RooFit()._LineColor(_string_to_root_attribute(color, _color_map))


def FillColor(color):
    # Redefinition of `FillColor` for matplotlib conventions and string arguments.
    return _RooFit()._FillColor(_string_to_root_attribute(color, _color_map))


def MarkerColor(color):
    # Redefinition of `MarkerColor` for matplotlib conventions and string arguments.
    return _RooFit()._MarkerColor(_string_to_root_attribute(color, _color_map))


def LineStyle(style):
    # Redefinition of `LineStyle` for matplotlib conventions and string arguments.
    return _RooFit()._LineStyle(_string_to_root_attribute(style, _linestyle_map))


def FillStyle(style):
    # Redefinition of `FillStyle` for matplotlib conventions and string arguments.
    return _RooFit()._FillStyle(_string_to_root_attribute(style, {}))


def MarkerStyle(style):
    # Redefinition of `MarkerStyle` for matplotlib conventions and string arguments.
    return _RooFit()._MarkerStyle(_string_to_root_attribute(style, {}))
