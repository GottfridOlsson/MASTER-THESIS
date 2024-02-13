##======================================================================##
##     Project: TIFX05 MASTER THESIS
##        File: SEM-01_bdat-viewer.py
##      Author: GOTTFRID OLSSON 
##     Created: 2024-02-13
##     Updated: 2024-02-13
##       About: Read a .bdat file from the battery cycling program.
##              1. Read file
##              2. Do calculations (change this dependent on your case).
##              3. Plot x_data and y_data, change any settings you want.
##              4. Save a copy of the code in another place (ARCHIVE).
##======================================================================##



# LIBRARIES #
import CSV_handler as CSV
import plot_functions as f
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as plticker



# READ .bdat #
# Change these:
filename_bdat = '2024-02-06_SEM-01_SEI-formation_sample-B.bdat' 
filename_pdf = 'testdata1.pdf'

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CSV_path = "\\MASTER-THESIS\\EXPERIMENTAL\\Data\\Battery-cycling\\SEM-01_SEI-formation\\" + filename_bdat
PDF_path = CURRENT_PATH + "\\PDF\\" + filename_pdf

CSV_data   = CSV.read(CSV_path, skiprows=10, delimiter='\t')
CSV_header = CSV.get_header(CSV_data)


# pick out columms
elapsed_time = CSV_data[CSV_header[5]] # s
current = CSV_data[CSV_header[7]] # A
cell_voltage = CSV_data[CSV_header[8]] # V
capacity = CSV_data[CSV_header[10]] # Ah

x_data_column_number = 5
y_data_column_number = 8

x_data = CSV_data[CSV_header[x_data_column_number]]
y_data = CSV_data[CSV_header[y_data_column_number]]



# PLOT SETTINGS #
fig_width_cm = 16
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9

x_label = f"{CSV_header[x_data_column_number]}"
y_label = f"{CSV_header[y_data_column_number]}"
title = f"{filename_bdat}"

x_lim = [np.min(x_data), np.max(x_data)]
y_lim = [np.min(y_data), np.max(y_data)]

grid_major = True
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting




# PLOT # 
# Create figure on which axis lives, one axis per subplot
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

# Plot your data (axs.plot, .errorbar, .hist, ...)
axs.plot(x_data, y_data, linewidth=1, linestyle='-', color='k', marker='.', markersize='3', label='Measured data')
#axs.plot(x_data, y_data_2, linewidth=1, linestyle='-', color='k', marker='.', markersize='3', label='Measured data')


# Settings for each axis (axs)
f.set_font_size(axis=font_size_axis, tick=font_size_tick, legend=font_size_legend)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label=x_label, y_label=y_label)
f.set_axis_invert(  axs, x_invert=False, y_invert=False)
f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
f.set_grid(         axs, grid_major_on=grid_major, grid_major_linewidth=0.7, grid_minor_on=grid_minor, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
f.set_legend(       axs, legend_on=legend_on, alpha=1.0, location='best')
axs.set_title(title)
#loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals determined by base
#axs.xaxis.set_major_locator(loc)

f.align_labels(fig)
f.set_layout_tight(fig)
#f.export_figure_as_pdf(PDF_path)
plt.show()


