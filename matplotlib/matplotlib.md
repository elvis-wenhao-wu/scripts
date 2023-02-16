# Notes

This document is for some matplotlib meta information and other important notes on using this library

## Meta Info

* Version: `matplotlib.__version__`

* Installation Location: `matplotlib.__file__`

* Configuration and Cache Directory Locations: <br/>

    If you would like to use a different configuration directory, you can do so by specifying the location in your `MPLCONFIGDIR` environment variable -- see Setting environment variables in Linux and macOS. Note that `MPLCONFIGDIR` sets the location of both the configuration directory and the cache directory.

    * `matplotlib.get_configdir()`
    * `matplotlib.get_cachedir()`

* Debug: 

    * `plt.set_loglevel('info')` 
    * `logging.basicConfig(level="DEBUG")` through standard python `logging` module before importing `matplotlib`

## How artists are added to Axes 
* `add_artist` & other *add_...* methods (more refined control)
    * Artists are first created and added to `Axes` or `Figure`, e.g. `circle = mpatches.Circle(...); ax.add_artist(circle)` <br/>

    The general method is `add_artist` (without adjusting the data limit after addition). Other dedicated methods will be primitive-oriented (e.g. `add_line`) or collection-oriented (e.g. `add_collection`). Normally primitive-oriented methods will not adjust the data limit after addition but collection-oriented methods will have this option.

* Axes plotting methods e.g. `Axes.plot`, `Axes.bar` 

    * Artists are created and added to `Axes` in one step. Autoscaling (datalim & viewlim adjustments have been made) internally. Returned are artists being created and added to `Axes`.

Note: some artists are not bundled into a built-in plotting method, in this case you'll have to use the first method. In interactive plotting, you'll also need more refined control of the artists.

