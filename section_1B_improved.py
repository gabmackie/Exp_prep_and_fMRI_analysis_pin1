from glob import glob
from os.path import join
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Create a function so any file can be read when needed
def read_file(filename):

    # Create a blank numpy array to store the data in
    # It has 5 rows because there are 5 stimulus categories
    data = np.zeros(5)

    # Reading the file is done inside a try statement
    # This is in case one of the relevant files is missing, to prevent the code from crashing
    try:
        # Open the file
        f = open(filename, 'r')

        # Run through each line in the file
        for dataline in f:
            # Convert each line into a stripped list
            dataline = dataline.strip().split()

            # Extract the name of the line, to match it to a stimulus class
            name = dataline[1]

            # Check the name against our stimulus class names
            # Save the mean variable, found in column 6, to the numpy array
            # Adding them to the array converts them to floats automatically
            for i in range(5):
                category = "cope" + str(i+1)
                if name.endswith(category):
                    data[i] = dataline[5]

        # Close the file
        f.close()

    # If there is a problem reading a file, this code runs
    except FileNotFoundError as e:
        # It prints a warning to the user
        print('WARNING: one of the ROI data files is missing')
        print('Analysis will be incorrect, please supply the necessary ROI data file')
        # It prints the exact error so they know which file is missing
        print(e)

    # Return the final numpy array with
    return data


# A function to analyse each ROI/stimulus class combination
# It returns the information necessary to plot the graph
# It also prints descriptive statistics for each ROI x stimulus class combination
def analyse_data(roi_data, roi, classes):

    # Create a list for the means, and one for the confidence intervals
    roi_means = []
    roi_cis = []

    # We run through this loop once for each stimulus class
    for i in range(len(classes)):

        # The current stimulus class is taken from the classes list
        this_class = classes[i]

        # This calculates the number of participants,
        # based on the number of entries in that column
        sub_n = len(roi_data[:, i])

        # This extracts the mean and SD from the specific column of data in,
        # the ROI file that corresponds to the current stimulus class
        stimulus_mean = np.mean(roi_data[:, i])
        stimulus_sd = np.std(roi_data[:, i])

        # Print all that information, neatly and in .csv style
        print(f'{roi},{this_class},{stimulus_mean:.3f},{stimulus_sd:.3f},{sub_n}')

        # Add the mean for this stimulus class to our list for use in the graph later
        roi_means.append(stimulus_mean)

        # We also calculate 95% confidence intervals
        # Done using the t-distribution because our sample size is small (N<30)
        interval = stats.t.interval(alpha=0.95, df=len(roi_data[:, i])-1, scale=stats.sem(roi_data[:, i]))

        # Add the positive confidence interval value to our CI list
        roi_cis.append(interval[1])

    # Return the list of means and CIs so they can be used in the graph
    return roi_means, roi_cis


# Create a list of all the participant folders in our chosen folder
# TODO REPLACE THIS WITH YOUR FOLDER (But please leave the *)
subject_folders = sorted(glob('roi_data\\*'))

# Define the classes of stimuli you have
classes = ['Bottle', 'Chair', 'Face', 'House', 'Shoe']
# Save the number of classes to a variable for future use
num_class = len(classes)

# Work out how many participants there are by counting the number of folders
num_sub = len(subject_folders)

# Print the number of participants
print(f'There are {num_sub} participants in this analysis\n')



# Create a dictionary containing the rois as keys and an array as the values
# Each array has one row per perticipant, and one column per stimulus class
roi_data = {'ffa': np.zeros([num_sub, num_class]), 
            'lingual_gyrus': np.zeros([num_sub, num_class]),
            'ppa': np.zeros([num_sub, num_class])}

# Run through every participant
for n in range(num_sub):
    # Do this analysis for each ROI in our dictionary
    for roi, data in roi_data.items():
        # Create the filename fir the ROI files within that subject's folder
        roi_file = join(subject_folders[n], roi, 'report.txt')

        # Call the reading function and save it to a variable
        new_roi_data = read_file(roi_file)

        # Replace the row corresponding with the subject number in our overall data file,
        # with the data we just extracted from the file
        # So each row contains a different participant's data
        roi_data[roi][n, :] = new_roi_data


# We need to print out the data for each ROI/stimulus class combination
# Print the headers for the data
print('ROI,Cope,Mean,Stdev,Nsamples')

# Run the function to print the data for each of the three ROIs
ffa_means, ffa_cis = analyse_data(roi_data['ffa'], 'FFA', classes)
lg_means, lg_cis = analyse_data(roi_data['lingual_gyrus'], 'Lingual Gyrus', classes)
ppa_means, ppa_cis = analyse_data(roi_data['ppa'], 'PPA', classes)



# Now we create a graph with that information
# Our graph will have a width equal to the number of classes
x = np.arange(num_class)
# The width of each bar can be adjusted
width = 0.28

# Set up our graph
plt.style.use('classic')
f = plt.figure()
ax = plt.gca()

# Plot each of the three ROIs,
# adjusting their locations on the x-axis so they don't overlap
# Add their respective confidence intervals as error bars
plt.bar(x - width, ffa_means, width, yerr=ffa_cis)
plt.bar(x, ppa_means, width, yerr=ppa_cis)
plt.bar(x + width, lg_means, width, yerr=lg_cis)

# Edit the labels and title of the graph, and add a figure legend
plt.title('ROI Analysis of Mean fMRI Single Change for Different Stimuli Categories')
plt.xlabel('Stimulus Categories')
plt.ylabel('fMRI Units (arbitrary)')
plt.legend(['FFA', 'PPA', 'Lingual Gyrus'], loc=4)

# Label the x axis correctly
ax.set_xticks(x)
ax.set_xticklabels(classes)

# Show the graph
plt.show()
