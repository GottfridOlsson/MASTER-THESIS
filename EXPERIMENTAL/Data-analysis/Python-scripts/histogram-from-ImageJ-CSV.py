##=============================================##
##     Project: TIFX05 MASTER THESIS
##        File: histogram-from-ImageJ-CSV.py
##      Author: GOTTFRID OLSSON 
##     Created: 2024-03-05
##     Updated: 2024-03-05
##       About: Plots a histogram of particle
##              sizes from a CSV-file created
##              by ImageJ. 
##=============================================##

## LIBRARIES ##

import CSV_handler as CSV
import matplotlib.pyplot as plt
import plot_functions as f
import matplotlib as mpl
import numpy as np



## FUNCTIONS ##

def micrometer_per_pixel(SEM_magnification):
    return 195 / (SEM_magnification + 6.6) #micrometer per pixel as function of magnification (times, e.g. 1000 or 5000) in the SEM (PHI 700 Scanning auger nanoprobe, in IMS at Chalmers)

def area_to_diameter_circular_particle(area):
    # A = pi*r*r   ==> r = (A/pi)^(0.5)    and   d = 2*r
    return 2*(area/3.1415926)**(0.5)

def get_statistical_measures(data):
    mean = np.mean(data)
    variance = np.var(data)
    sigma = np.sqrt(variance)
    return (mean, sigma)




## READ ##
CSV_filename = '2024-02-21_Cu-Li_SEM-03_125_threshold-MaxEntropy_analyzed.csv'
CSV_path = 'C:\\MASTER-THESIS\\EXPERIMENTAL\\Data-analysis\\Test-ImageJ\\2024-02-21_SEM-03_tif\\' + CSV_filename

CSV_data   = CSV.read(CSV_path)
CSV_header = CSV.get_header(CSV_data) # header =  [' ', 'Area', 'Mean', 'Min', 'Max'] (pixels)
CSV_header[0] = 'Particle-number'
CSV_header[1] = 'Area (px^2)'


particle_area_px = CSV_data[CSV_header[1]]
particle_diameter_px = area_to_diameter_circular_particle(particle_area_px)
#particle_diameter_micrometer = micrometer_per_pixel(magnification) * particle_diameter_px

x_data = particle_diameter_px
mean, sigma = get_statistical_measures(x_data)
number_of_particles = len(x_data)



# PLOT SETTINGS #

fig_width_cm = 16
fig_height_cm = 9

font_size_axis = 13
font_size_tick = 11
font_size_legend = 9


x_bins = [0,1,2,3,4,5,6,7,8,9,10]
patch_color = 'r' #'#606060'
patch_linewidth = 0.5
hatch_string = '\\\\\\' #'xxx' # '///'; / , \\ , | , - , + , x, o, O, ., *

x_label = "X-axis, particle diameter (px)"
y_label = "Particle count"

#x_lim = [np.min(x_data), np.max(x_data)]
#y_lim = [np.min(y_data), np.max(y_data)]

grid_major = True
grid_minor = False
legend_on = True

f.set_LaTeX_and_CMU(True) #must run before plotting
mpl.rcParams['hatch.linewidth'] = patch_linewidth  # hatch linewidth, not accessable elsehow



# add text (and box):   https://matplotlib.org/stable/gallery/text_labels_and_annotations/placing_text_boxes.html#sphx-glr-gallery-text-labels-and-annotations-placing-text-boxes-py


## PLOT ##

# Create figure on which axis lives, one axis per subplot
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(fig_width_cm/2.54, fig_height_cm/2.54), sharex=False, sharey=False)

# Plot your data (axs.plot, .errorbar, .hist, ...)
axs.hist(x_data, fill=False, hatch=hatch_string)#, linewidth=0.1)#, color=color)#, bins=x_bins)
for patch in axs.patches:
    patch.set_edgecolor(patch_color)
    #patch.set_linewidth(patch_linewidth)

# Settings for each axis (axs)
f.set_font_size(axis=font_size_axis, tick=font_size_tick, legend=font_size_legend)
f.set_axis_scale(   axs, xScale_string='linear', yScale_string='linear')
f.set_axis_labels(  axs, x_label=x_label, y_label=y_label)
#f.set_axis_invert(  axs, x_invert=False, y_invert=False)
#f.set_axis_limits(  axs, x_lim[0], x_lim[1], y_lim[0], y_lim[1])
#f.set_grid(         axs, grid_major_on=grid_major, grid_major_linewidth=0.7, grid_minor_on=grid_minor, grid_minor_linewidth=0.3) # set_grid must be after set_axis_scale for some reason (at least with 'log')
#f.set_legend(       axs, legend_on=legend_on, alpha=1.0, location='best')

#loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals determined by base
#axs.xaxis.set_major_locator(loc)

f.align_labels(fig)
f.set_layout_tight(fig)
#f.export_figure_as_pdf(PDF_path)

print(f"\nData from filepath: {CSV_path}")
print(f"Number of particles analyzed: {number_of_particles}")
print(f"Mean: {mean:.2f}")
print(f"1sigma: {sigma:.2f}")

plt.show()