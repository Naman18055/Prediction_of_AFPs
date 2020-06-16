import csv
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

rows=[]   # Storing Every informative row in this array

with open('train.csv', 'r') as file:
	reader = csv.reader(file)   #initiating file reader
	flag=0
	for row in reader:
		if flag==0:        		# Skipping the first row as it contains coloumn titles 
			flag=1
			continue
		rows.append(row)   		#Adding each row to the array

serialno=[]		#
sequences=[]	# Splitting the information of each row into different arrays.
label=[]		#

for i in rows:
	sequences.append(i[2])  # storing the sequences in the sequences array
	label.append(i[1])		# storing the Labels in the label array

X=[]    # Initiating arrays for training data
Y=[]

for i in range(len(sequences)): 
	Tripeptides=[[[0 for i in range(26)] for j in range(26)] for k in range(26)] #Initiating a 26X26X26 matrix for storing Tripeptides 
	new = []
	residues=[0]*26 #
	for j in range(len(sequences[i])-2):  																# going over every triplet of letters in the seuence
		Tripeptides[ord(sequences[i][j])-65][ord(sequences[i][j+1])-65][ord(sequences[i][j+2])-65]+=1 	# and updating the matrix
		residues[ord(sequences[i][j])-65]+=1															# and also updating the residue arrya appropriatly
	for j in range(26):
		for k in range(26):
			for l in range(26):
				Tripeptides[j][k][l]=(Tripeptides[j][k][l]*100/400)   #dividing every element with 4 from the matrix of Tripeptides 
		residues[j]=(residues[j]*100/len(sequences[i]))               # and doing the same for the residues
	
	for j in Tripeptides:
		for k in j:
			for l in k:
				new.append(l) # adding information about tripeptides into the new array 
	
	X.append(new)
	Y.append(int(label[i]))

X=np.array(X)   			 # converting into numpy array 
Y=np.array(Y)				 # converting into numpy array

clf = svm.SVC(kernel='rbf')  # initiating classifier
clf.fit(X,Y)				 # training data

rows=[]   					 #initiating row matrix for test data

with open('test.csv', 'r') as file:
	reader = csv.reader(file)
	flag=0
	for row in reader:
		if flag==0:
			flag=1
			continue
		rows.append(row)   	# reading the rows from the test file

sequences=[] 				# Splitting the information of each row into different arrays.
ans=[]

for i in rows:
	serialno.append(i[0])
	sequences.append(i[1])	#adding sequences to the array


# this is the same as above , for finding tripeptides 
for i in range(len(sequences)):
	Tripeptides=[[[0 for i in range(26)] for j in range(26)] for k in range(26)]
	residues=[0]*26
	new=[]
	for j in range(len(sequences[i])-2):
		Tripeptides[ord(sequences[i][j])-65][ord(sequences[i][j+1])-65][ord(sequences[i][j+2])-65]+=1
		residues[ord(sequences[i][j])-65]+=1
	for j in range(26):
		for k in range(26):
			for l in range(26):
				Tripeptides[j][k][l]=(Tripeptides[j][k][l]*100/400)
		residues[j]=(residues[j]*100/len(sequences[i]))
	for j in Tripeptides:
		for k in j:
			for l in k:
				new.append(l)

	ans.append(clf.predict([new])) #pedicting the answer using the clf. and storing the answer in the answer array


# writing the answers in the ans2.csv file
with open('ans2.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["ID","Label"])
	for i in range(len(ans)):
		writer.writerow([serialno[i],ans[i][0]])

# print (len(ans))
