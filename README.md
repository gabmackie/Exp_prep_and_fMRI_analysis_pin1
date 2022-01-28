# pin_assessment1
Fist assessment from my programming in neuroimaging module. It contains the data, zip file of my original submission, and code that's been improved based on their feedback.

### *Below are the instructions I was given for the assessment.*

&nbsp;

---------------------------------------------------------------------


# Programming in NeuroImaging – 2020/21: Assessment 1

For the first assignment in the PiN module, you will be required to produce a
portfolio in two parts.  The first part of the portfolio requires you to write
a script which will select word stimuli for an experiment.  The second part of
the portfolio requires you to write code to extract and plot percentage signal
change data from some real fMRI data files.  This assessment counts 30% towards
the overall module mark.

## General Guidelines

Some of the things we are looking for include:

 * Appropriate commenting of the scripts.  Remember, comments should not just
   say what something does – they should explain why it does it.
 * Making your scripts neat and adaptable to other situations – for example, if
   you are asked to input three numbers from a user, use a loop with a counter
   rather than copying and pasting the code three times.
 * Where appropriate, ensuring that you handle bad user input in a robust way –
   for example, making sure that your script doesn't crash if you ask for a
   number and the user types a word
 * Where appropriate, ensuring that any output shown to the user is formatted
   neatly.

### Testing your scripts

*Remember: Test your scripts!*  They must at least run through even if they
don't implement all of the functionality required.  Also, make sure that you
submit the correct version of your scripts - we can only mark what you submit!

### Use of Python Modules

Important note regarding the use of Python modules:  Whilst you have almost
complete freedom to use any Python modules installed at YNiC (including those
which we have not used in the course), you may explicitly not use the “pandas”
module.  The aim of the assessment is to assess your ability to handle data
using the low level numpy and scipy routines and our experience is that
students who use the “pandas” module fail to demonstrate this ability.  Use of
the “pandas” module will result in a mark of 0 for the relevant section of the
assessment.

### Data files for the assessment

Data files for the assessment:  The data files for the assessment are available
either from the VLE, or via a Git repository at
<https://vcs.ynic.york.ac.uk/cn/pin-assessment1>

You can clone the above git repository using:

```
git clone https://vcs.ynic.york.ac.uk/cn/pin-assessment1
```

You will require your YNiC username and password to do this.  If you do not
wish to use git, the same files can be found on the PiN VLE page.

Note that if you download the files from the VLE, the data for section B will
be a zip file (due to VLE limitations).  You should unzip this by hand – you do
not need to use Python to do this.  If you get the data from the git
repository, the files will be ready to use.

## Section A – Preparing word stimuli for an experiment

*40% of the available marks for this assessment*

The scenario for this exercise is the following:  Your supervisor requires word
stimuli for an experiment.  They want words containing exactly four characters.
They also want these words to all have a different  pair of final two
characters (i.e. coal and goal should not both be used as stimuli).  The final
two characters are called the “word ending”.  So coal and goal both have a word
ending of al.

In addition, your supervisor only wants stimuli taken from common word endings
(word endings with at least 30 words available in the dictionary).  They also
want to know how many words were available in total and for each of the word
endings.  They have provided you with a long list of words to start from.

To perform this task, you have been provided with a file containing a large
list of words (`words.txt`).  This file is available on the VLE and in the git
repository linked above.

The `words.txt` file contains words which contain the characters A-Z (upper and
lower case) and apostrophes (').  There are no other characters in the file to
worry about (all words with accents or umlauts have been removed for you).

You must write a script to perform the following tasks:

 1. Count all unique four letter words in the file.  Any word with an
    apostrophe in should be ignored.  You should ignore the case of the word
    (i.e. Tool and tool should only be counted as one word).  Print out (so that
    the user can see) the number of unique four letter words.
 2. Divide up the four letter words based upon the last two letters of the word
    (the word ending).  Count up how many words you have for each of these
    endings.  For the rest of the exercise, only work with word endings where there
    are at least 30 words.  As one example, there are 5 four-letter words which end
    with the characters af – you should therefore not use words ending with af for
    the rest of the exercise.  You will exclude many word endings based on this.
 3. Print out a list of word endings and the number of words you found for each
    ending, for example (this data is not from the real file – your answers
    will not agree with it):

```
as: 30
at: 35
...
```

   You may choose to format this output as a neat table.

 4. Randomly choose one word from those available for each of the word endings
    to use in your stimuli.  You should therefore end up with a stimulus list
    containing the same number of words as word endings.  Print out the number of
    stimuli you end up with.
 5. Print out your list of chosen word stimuli.

### Submission Requirements for Section A

 * Your script.  Call this `section_A.py`

## Section B – Analysing and Plotting fMRI ROI Data

*60% of the available marks for this assessment*

The scenario for this exercise is the following:  You have collected some fMRI
data on 10 participants and performed initial analysis on it.  Your experiment
involved presenting five classes of stimuli to people: Bottles, Chairs, Faces,
Houses and Shoes.  You have analysed the data for three regions of interest
(ROIs): the FFA, the PPA and the Lingual Gyrus.  Your supervisor has now asked
you to produce a summary of the mean values for each combination of ROI and
stimulus class and also to plot a presentable graph of this information,
ideally including errorbars.

The data you have been given is in a set of files, all of which are called
report.txt (these have been taken from real output from FEATQuery, a tool in
FSL which allows you to calculate percentage signal changes).  This data is
available in the zip file fmriroi.zip on the YNiC computers and the VLE.

You do not need to unzip the data using Python; just do this in your file
browser or other zip application.

The files are stored in subdirectories, so the data for subject 1, for the FFA
is stored in the file: `01/ffa/report.txt`

Inside this file, you have the following data:

```
1 stats/pe1 99 -1.142 -0.2346 0.2624 0.217 0.708 2.208 0.524 82 40 10 -41.4 -68.0 -26.3
1 stats/pe3 99 -0.8975 -0.3608 0.2384 0.172 0.8187 2.214 0.5717 82 40 10 -41.4 -68.0 -26.3
1 stats/pe5 99 -0.5678 -0.1925 0.6548 0.5609 1.689 3.413 0.7602 43 44 10 48.4 -61.3 -28.8
1 stats/pe7 99 -1.062 -0.5388 0.1613 0.1121 0.7017 2.181 0.5952 82 40 10 -41.4 -68.0 -26.3
1 stats/pe9 99 -0.4066 -0.0862 0.6283 0.4122 1.475 3.363 0.7636 43 44 10 48.4 -61.3 -28.8
1 stats/cope1 99 -1.121 -0.2304 0.2577 0.2131 0.6953 2.169 0.5146 82 40 10 -41.4 -68.0 -26.3
1 stats/cope2 99 -0.87 -0.3497 0.2311 0.1667 0.7936 2.146 0.5542 82 40 10 -41.4 -68.0 -26.3
1 stats/cope3 99 -0.5544 -0.188 0.6393 0.5476 1.649 3.332 0.7422 43 44 10 48.4 -61.3 -28.8
1 stats/cope4 99 -1.047 -0.5311 0.159 0.1105 0.6917 2.15 0.5867 82 40 10 -41.4 -68.0 -26.3
1 stats/cope5 99 -0.397 -0.08417 0.6135 0.4025 1.44 3.284 0.7456 43 44 10 48.4 -61.3 -28.8
```

The data which you require is on the lines which contain
`stats/cope1`..`stats/cope5`.  Your code needs to ignore all of the other
lines!  Each line has many values, but you need to ignore all of them except
for the mean percentage signal change.  This is the 6th column of the file
(shown in bold above).  You need to use only these values.

Each of the lines starting with stats/cope1..stats/cope5 give values for the
different stimulus classes.  As an example, in the file above, the values are
therefore:

 * `cope1`:	*Bottle*: `0.2577`
 * `cope2`: *Chair*: `0.2311`
 * `cope3`: *Face*: `0.6393`
 * `cope4`: *House*: `0.159`
 * `cope5`: *Shoe*: `0.6135`

These are therefore the percentage signal changes which were measured in the
FFA for each of the stimulus categories for participant 1.

You must write a script which can perform the following tasks:

 * Work out how many participants you have
 * Read in the relevant data from each of the files and store this in a
   sensible data structure
 * Calculate the mean and standard deviation across subjects for each ROI and
   stimulus class (you will therefore end up with fifteen means and standard
   deviation)
 * Print out the mean, standard deviation and number of samples which were used
   to calculate these to the screen as if it were a CSV file (with a header).
   As an example: (note that the values in this example are deliberately not
   correct!):

```
ROI,Cope,Mean,Stddev,Nsamples
FFA,Bottle,0.522,0.122,10
FFA,Chair,0.403,0.120,10
FFA,Face,0.666,0.055,10
FFA,House,0.211,0.122,10
FFA,Shoe,0.232,0.332,10
Lingual Gyrus,Bottle,0.888,0.221,5
… (continue with more lines for each combination)
```

 * Plot an appropriate graph to show the data - ideally showing confidence
   intervals.  Remember to call `plt.show()` at the end of your script so that
   the plot ends up on the screen.

### Tips for getting started:

 * First of all, figure out how to read the relevant information out of a
   single file (use the file for which you were given example data above to
   make sure you are doing it correctly)
 * Then work out how to do this for all of the files that you need to read from
 * Only start looking at how to output your summary information and plot once you have worked out how to load in and store all of your data

### Additional things to consider:

 * Think about how to make your script generally useful - can it be easily used
   with a different number of participants for instance?
 * Is your script robust - what would it do if one of the files for one of the
   participants is missing?

### Submission Requirements for Section B

 * Your script.  Call this `section_B.py`
