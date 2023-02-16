# Format Matplotlib Graph

## General Formatting

* [Python date format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

  | Directive | Meaning | Example | 
  | ----------- | ----------- | ----------- | 
  | %Y | Year with century as a decimal number. | 2019, 2020, 2021, etc. | 
  | %m | Month as a zero-padded decimal number. | 01, 02, ..., 12 |
  | %d | Day of the month as a zero-padded decimal number. | 01, 02, ..., 31 |
  | %H | Hour (24-hour clock) as a zero-padded decimal number. | 00, 01, ..., 23 |
  | %M | Minute as a zero-padded decimal number. | 00, 01, ..., 59 |
  | %S | Second as a zero-padded decimal number. | 00, 01, ..., 59 |
  | %a | Weekday as locale’s abbreviated name. | Sun, Mon, ..., Sat |
  | %b | Month as locale’s abbreviated name. | Jan, Feb, ..., Dec |

* Numpy date format in X-axis

  ```python
  import matplotlib.dates as mdates
  ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
  ```

* Spines & Grid

  ```python
  ax.spines[['top', 'right']].set_visible(False)
  ax.grid(lw=1, ls='--')
  ```

* [Legend position](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend)
 
  | Location String | Location Code |
  | ----------- | ----------- |
  | 'best' | 0 |
  | 'upper right' | 1 |
  | 'upper left' | 2 |
  | 'lower left' | 3 |
  | 'lower right' | 4 |
  | 'right' | 5 |
  | 'center left' | 6 |
  | 'center right' | 7 |
  | 'lower center' | 8 |
  | 'upper center' | 9 |
  | 'center' | 10 |

  ```python
  ax.legend(loc = 'upper right', bbox_to_anchor=(1, -0.1)) # refer to docs about bbox_to_anchor
  ```
