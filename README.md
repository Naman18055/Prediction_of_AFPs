# INTRODUCTION
Our Model is used for predicting Antifungal Peptides. It classifies the antifungal peptides into positive and negative peptides by first training over the given data and then testing it. 

# FILES
1. Train.csv - It contains the training data of 2550 lines consisting of three columns namely ID, Label and Sequence. Label "1" denotes the positive peptide and "-1" denotes the negative peptide. Sequence consists of the protein sequence. 

2. Test.csv - This file contains the testing data of 368 lines. It includes two columns namely ID and Sequence.

3. Script.py - Python file for creating the model using training data and testing it on the testing data. It uses the Machine Learning model SVM (Support Vector Machine) to create the model. Details of the code is given in the file as comments.

4. ans2.csv - It contains the classification of the testing data after running the file script.py.

# FEATURE USED FOR TRAINING DATA
For training of our ML model we will be using a single feature which will be ​Tripeptides​. \
We find these tripeptides using a loop over all the sequences and storing the value in a 3D matrix which store the count value for every possible value Tripeptide in the sequence, Which we then further divide by 4.
Then for every sequence we add this tripeptide data and their respective label into the training data.
After Training we read the value from the test data and respectively predict its label and store the predicted info into a new ans2.csv.
# Past Attempts
1) Using various properties such as isoelectric , molecular weight using functions from the Bio library in python.
2) Using basic dipeptide.\
2-Fold Cross Validation Results : 0.844\
Details about the code is present in the script itself as comments

# RUNNING THE FILE
To run the file, run "python3 script.py" on the command line. Make sure that training data and testing data are already present in your current directory and saved as "train.csv" and "test.csv". The code will automatically generate "ans2.csv" file.
