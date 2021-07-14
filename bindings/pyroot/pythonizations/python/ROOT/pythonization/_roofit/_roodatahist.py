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
\class RooDataHist
\brief \parblock \endparblock
\htmlonly
<div class="pyrootbox">
\endhtmlonly

## PyROOT

Constructor of RooDataHist takes a RooCmdArg as argument also supports keyword arguments.
For example, the following code is equivalent in PyROOT:
\code{.py}
# Directly passing a RooCmdArg:
dh = ROOT.RooDataHist("dh", "dh", ROOT.RooArgList(x), ROOT.RooFit.Import("SampleA", histo))

# With keyword arguments:
dh = ROOT.RooDataHist("dh", "dh", ROOT.RooArgList(x), Import=("SampleA", histo))
\endcode

\htmlonly
</div>
\endhtmlonly
*/
"""

from ._utils import _kwargs_to_roocmdargs, _dict_to_std_map


class RooDataHist(object):
    def __init__(self, *args, **kwargs):
        # Redefinition of `RooDataHist` constructor for keyword arguments and converting python dict to std::map.
        # The keywords must correspond to the CmdArg of the constructor function.
        # The instances in dict must correspond to the template argument in std::map of the constructor.
        def all_values_of_class(d, klass):
            # Function to check all instances of the class object in dictionary.
            return all([isinstance(v, klass) for v in d.values()])

        def _get_template_args(import_dict):
            # Function to return the class type for dictionary to map conversion.
            import ROOT

            if all_values_of_class(import_dict, ROOT.RooDataHist):
                value_class_name = "RooDataHist"
            elif all_values_of_class(import_dict, ROOT.TH1):
                value_class_name = "TH1"
            else:
                raise TypeError(
                    """Unsupported value types in dictionary passed to RooDataHist(import_dict). The imported objects need to be either: * all instances of RooDataHist * all instances of TH1"""
                )

            return "std::string," + value_class_name + "*"

        for i, arg_dict in enumerate(args):
            if isinstance(arg_dict, dict):
                template_arg = _get_template_args(arg_dict)
                args = list(args)
                args[i] = _dict_to_std_map(arg_dict, template_arg)

        args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
        self._init(*args, **kwargs)

    def plotOn(self, *args, **kwargs):
        # Redefinition of `RooDataHist.plotOn` for keyword arguments.
        # The keywords must correspond to the CmdArg of the `plotOn` function.
        args, kwargs = _kwargs_to_roocmdargs(*args, **kwargs)
        return self._plotOn(*args, **kwargs)
