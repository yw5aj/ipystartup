import matplotlib as mpl


# Figure formatting
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['figure.figsize'] = (3.5, 3.5)

# Font setting
mpl.rcParams['mathtext.default'] = 'regular'
mpl.rcParams['font.family'] = ['sans-serif']
mpl.rcParams['font.sans-serif'] = ['Arial']
mpl.rcParams['font.size'] = 8
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['svg.fonttype'] = 'none'

# Line properties
mpl.rcParams['lines.linewidth'] = 1.
mpl.rcParams['lines.markersize'] = 4

# Legends
mpl.rcParams['legend.frameon'] = False
mpl.rcParams['legend.fontsize'] = 8
mpl.rcParams['legend.handlelength'] = 3

# Subplot frame line
mpl.rcParams['axes.linewidth'] = .5

# Color of ticks, axes, and labels
color = '.5'
mpl.rcParams['axes.edgecolor'] = color
mpl.rcParams['xtick.color'] = color
mpl.rcParams['ytick.color'] = color
