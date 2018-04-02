#Importing important modules
import math

#Null Hypothesis Mean
null_mean = float(raw_input('Mean for the Null Hypothesis: '))

#If mean and deviation is provided?
feedback = raw_input("Do you have the mean and standard deviation calculated?(yes/no) - ")

alternate_mean = 0
deviation = 0

#If yes
if feedback.lower() == 'yes':
	alternate_mean = float(raw_input('Mean for the Alternate Hypothesis: '))
	deviation = float(raw_input('Standard Deviation: '))

#If not
else:

	#Asking for data points
	x_input = raw_input('Enter all the x values: ').split(' ')

	#From string to float
	index_x= 0
	while index_x < len(x_input):
		x_input[index_x] = float(x_input[index_x])
		index_x = index_x + 1

	#Calculating mean
	alternate_mean = 0
	for x in x_input:
		alternate_mean = alternate_mean + x

	alternate_mean = alternate_mean / len(x_input)

	print 'Mean for the Alternate Hypothesis: ', alternate_mean

	#Calculating deviation
	deviation = 0
	for x in x_input:
		deviation = deviation + ((x - alternate_mean) ** 2)
	deviation = deviation / (len(x_input) - 1)
	deviation = math.sqrt(deviation)

	print 'Standard Deviation: ', deviation
	
#Asking for sample size
sample_size = int(raw_input('Sample Size (n): '))

#Taking square root to use in the formula
sample_size_sqrt = math.sqrt(sample_size)

#Checking if z-test
if sample_size >= 30:

	#Asking for threshold
	alpha = float(raw_input('Threshold: '))

	#Dictionary for the z table values

	z_table = {	
		'0.00'	:	50.00,
		'0.01'	:	50.40,
		'0.02'	:	50.80,
		'0.03'	:	51.20,
		'0.04'	:	51.60,
		'0.05'	:	51.99,
		'0.06'	:	52.39,
		'0.07'	:	52.79,
		'0.08'	:	53.19,
		'0.09'	:	53.59,
		'0.10'	:	53.98,
		'0.11'	:	54.38,
		'0.12'	:	54.78,
		'0.13'	:	55.17,
		'0.14'	:	55.57,
		'0.15'	:	55.96,
		'0.16'	:	55.36,
		'0.17'	:	56.75,
		'0.18'	:	57.14,
		'0.19'	:	57.53,
		'0.20'	:	57.93,
		'0.21'	:	58.32,
		'0.22'	:	58.71,
		'0.23'	:	59.10,
		'0.24'	:	59.48,
		'0.25'	:	59.87,
		'0.26'	:	60.26,
		'0.27'	:	60.64,
		'0.28'	:	61.03,
		'0.29'	:	61.41,
		'0.30'	:	61.79,
		'0.31'	:	62.17,
		'0.32'	:	62.55,
		'0.33'	:	62.93,
		'0.34'	:	63.31,
		'0.35'	:	63.68,
		'0.36'	:	64.06,
		'0.37'	:	64.43,
		'0.38'	:	64.80,
		'0.39'	:	65.17,
		'0.40'	:	65.54,
		'0.41'	:	65.91,
		'0.42'	:	66.28,
		'0.43'	:	66.64,
		'0.44'	:	67.00,
		'0.45'	:	67.36,
		'0.46'	:	67.72,
		'0.47'	:	68.08,
		'0.48'	:	68.44,
		'0.49'	:	68.79,
		'0.50'	:	69.15,
		'0.51'	:	69.50,
		'0.52'	:	69.85,
		'0.53'	:	70.19,
		'0.54'	:	70.54,
		'0.55'	:	70.88,
		'0.56'	:	71.23,
		'0.57'	:	71.57,
		'0.58'	:	71.90,
		'0.59'	:	72.24,
		'0.60'	:	72.57,
		'0.61'	:	72.91,
		'0.62'	:	73.24,
		'0.63'	:	73.57,
		'0.64'	:	73.89,
		'0.65'	:	74.22,
		'0.66'	:	74.54,
		'0.67'	:	74.86,
		'0.68'	:	75.17,
		'0.69'	:	75.49,
		'0.70'	:	75.80,
		'0.71'	:	76.11,
		'0.72'	:	76.42,
		'0.73'	:	76.73,
		'0.74'	:	77.04,
		'0.75'	:	77.34,
		'0.76'	:	77.64,
		'0.77'	:	77.94,
		'0.78'	:	78.23,
		'0.79'	:	78.52,
		'0.80'	:	78.81,
		'0.81'	:	79.10,
		'0.82'	:	79.39,
		'0.83'	:	79.67,
		'0.84'	:	79.95,
		'0.85'	:	80.23,
		'0.86'	:	80.51,
		'0.87'	:	80.78,
		'0.88'	:	81.06,
		'0.89'	:	81.33,
		'0.90'	:	81.59,
		'0.91'	:	81.86,
		'0.92'	:	82.12,
		'0.93'	:	82.38,
		'0.94'	:	82.64,
		'0.95'	:	82.89,
		'0.96'	:	83.15,
		'0.97'	:	83.40,
		'0.98'	:	83.65,
		'0.99'	:	83.89,
		'1.00'	:	84.13,
		'1.01'	: 	84.38,
		'1.02'	: 	84.61,
		'1.03'	: 	84.85,
		'1.04'	: 	85.08,
		'1.05'	: 	85.31,
		'1.06'	: 	85.54,
		'1.07'	: 	85.77,
		'1.08'	: 	85.99,
		'1.09'	: 	86.21,
		'1.10'	: 	86.43,
		'1.11'	: 	86.65,
		'1.12'	: 	86.86,
		'1.13'	: 	87.08,
		'1.14'	: 	87.29,
		'1.15'	: 	87.49,
		'1.16'	: 	87.70,
		'1.17'	: 	87.90,
		'1.18'	: 	88.10,
		'1.19'	: 	88.30,
		'1.20'	: 	88.49,
		'1.21'	: 	88.69,
		'1.22'	: 	88.88,
		'1.23'	: 	89.07,
		'1.24'	: 	89.25,
		'1.25'	: 	89.44,
		'1.26'	: 	89.62,
		'1.27'	: 	89.80,
		'1.28'	: 	89.97,
		'1.29'	: 	90.15,
		'1.30'	: 	90.32,
		'1.31'	: 	90.49,
		'1.32'	: 	90.66,
		'1.33'	: 	90.82,
		'1.34'	: 	90.99,
		'1.35'	: 	91.15,
		'1.36'	: 	91.31,
		'1.37'	: 	91.47,
		'1.38'	: 	91.62,
		'1.39'	: 	91.77,
		'1.40'	: 	91.92,
		'1.41'	: 	92.07,
		'1.42'	: 	92.22,
		'1.43'	: 	92.36,
		'1.44'	: 	92.51,
		'1.45'	: 	92.65,
		'1.46'	: 	92.79,
		'1.47'	: 	92.92,
		'1.48'	: 	93.06,
		'1.49'	: 	93.19,
		'1.50'	: 	93.32,
		'1.51'	: 	93.45,
		'1.52'	: 	93.57,
		'1.53'	: 	93.70,
		'1.54'	: 	93.82,
		'1.55'	: 	93.94,
		'1.56'	: 	94.06,
		'1.57'	: 	94.18,
		'1.58'	: 	94.29,
		'1.59'	: 	94.41,
		'1.60'	: 	94.52,
		'1.61'	: 	94.63,
		'1.62'	: 	94.74,
		'1.63'	: 	94.84,
		'1.64'	: 	94.95,
		'1.65'	: 	95.05,
		'1.66'	: 	95.15,
		'1.67'	: 	95.25,
		'1.68'	: 	95.35,
		'1.69'	: 	95.45,
		'1.70'	: 	95.54,
		'1.71'	: 	95.64,
		'1.72'	: 	95.73,
		'1.73'	: 	95.82,
		'1.74'	: 	95.91,
		'1.75'	: 	95.99,
		'1.76'	: 	96.08,
		'1.77'	: 	96.16,
		'1.78'	: 	96.25,
		'1.79'	: 	96.33,
		'1.80'	: 	96.41,
		'1.81'	: 	96.49,
		'1.82'	: 	96.56,
		'1.83'	: 	96.64,
		'1.84'	: 	96.71,
		'1.85'	: 	96.78,
		'1.86'	: 	96.86,
		'1.87'	: 	96.93,
		'1.88'	: 	96.99,
		'1.89'	: 	97.06,
		'1.90'	: 	97.13,
		'1.91'	: 	97.19,
		'1.92'	: 	97.26,
		'1.93'	: 	97.32,
		'1.94'	: 	97.38,
		'1.95'	: 	97.44,
		'1.96'	: 	97.50,
		'1.97'	: 	97.56,
		'1.98'	: 	97.61,
		'1.99'	: 	97.67,
		'2.00'	: 	97.72,
		'2.01'	: 	97.78,
		'2.02'	: 	97.83,
		'2.03'	: 	97.88,
		'2.04'	: 	97.93,
		'2.05'	: 	97.98,
		'2.06'	: 	98.03,
		'2.07'	: 	98.08,
		'2.08'	: 	98.12,
		'2.09'	: 	98.17,
		'2.10'	: 	98.21,
		'2.11'	: 	98.26,
		'2.12'	: 	98.30,
		'2.13'	: 	98.34,
		'2.14'	: 	98.38,
		'2.15'	: 	98.42,
		'2.16'	: 	98.46,
		'2.17'	: 	98.50,
		'2.18'	: 	98.54,
		'2.19'	: 	98.57,
		'2.20'	: 	98.61,
		'2.21'	: 	98.64,
		'2.22'	: 	98.68,
		'2.23'	: 	98.71,
		'2.24'	: 	98.75,
		'2.25'	: 	98.78,
		'2.26'	: 	98.81,
		'2.27'	: 	98.84,
		'2.28'	: 	98.87,
		'2.29'	: 	98.90,
		'2.30'	: 	98.93,
		'2.31'	: 	98.96,
		'2.32'	: 	98.98,
		'2.33'	: 	99.01,
		'2.34'	: 	99.04,
		'2.35'	: 	99.06,
		'2.36'	: 	99.09,
		'2.37'	: 	99.11,
		'2.38'	: 	99.13,
		'2.39'	: 	99.16,
		'2.40'	: 	99.18,
		'2.41'	: 	99.20,
		'2.42'	: 	99.22,
		'2.43'	: 	99.25,
		'2.44'	: 	99.27,
		'2.45'	: 	99.29,
		'2.46'	: 	99.31,
		'2.47'	: 	99.32,
		'2.48'	: 	99.34,
		'2.49'	: 	99.36,
		'2.50'	: 	99.38,
		'2.51'	: 	99.40,
		'2.52'	: 	99.41,
		'2.53'	: 	99.43,
		'2.54'	: 	99.45,
		'2.55'	: 	99.46,
		'2.56'	: 	99.48,
		'2.57'	: 	99.49,
		'2.58'	: 	99.51,
		'2.59'	: 	99.52,
		'2.60'	: 	99.53,
		'2.61'	: 	99.55,
		'2.62'	: 	99.56,
		'2.63'	: 	99.57,
		'2.64'	: 	99.59,
		'2.65'	: 	99.60,
		'2.66'	: 	99.61,
		'2.67'	: 	99.62,
		'2.68'	: 	99.63,
		'2.69'	: 	99.64,
		'2.70'	: 	99.65,
		'2.71'	: 	99.66,
		'2.72'	: 	99.67,
		'2.73'	: 	99.68,
		'2.74'	: 	99.69,
		'2.75'	: 	99.70,
		'2.76'	: 	99.71,
		'2.77'	: 	99.72,
		'2.78'	: 	99.73,
		'2.79'	: 	99.74,
		'2.80'	: 	99.74,
		'2.81'	: 	99.75,
		'2.82'	: 	99.76,
		'2.83'	: 	99.77,
		'2.84'	: 	99.77,
		'2.85'	: 	99.78,
		'2.86'	: 	99.79,
		'2.87'	: 	99.79,
		'2.88'	: 	99.80,
		'2.89'	: 	99.81,
		'2.90'	: 	99.81,
		'2.91'	: 	99.82,
		'2.92'	: 	99.82,
		'2.93'	: 	99.83,
		'2.94'	: 	99.84,
		'2.95'	: 	99.84,
		'2.96'	: 	99.85,
		'2.97'	: 	99.85,
		'2.98'	: 	99.86,
		'2.99'	: 	99.86,
		'3.00'	: 	99.87,
		'3.01'	: 	99.87,
		'3.02'	: 	99.87,
		'3.03'	: 	99.88,
		'3.04'	: 	99.88,
		'3.05'	: 	99.89,
		'3.06'	: 	99.89,
		'3.07'	: 	99.89,
		'3.08'	: 	99.90,
		'3.09'	:	99.90
				}


	#List of keys of the dictionary
	keys = z_table.keys()

	#Asking for the type of test
	print ('1. One Tailed Test \n2. Two Tailed Test')

	choice = raw_input('Your Choice- ')

	#If one tailed
	if choice == '1':

		#Calculating z value
		z_value = (abs(null_mean - alternate_mean)) / (deviation / sample_size_sqrt)
	
		#Area for critical point
		critical_point = 100.00 - alpha

		#Empty list to store the differences
		list_abs = []

		#iterating over the keys and values of the dictionary
		for key, value in z_table.iteritems():

			#Appending the magnitude of the difference
			list_abs.append(abs(value - critical_point))

		#Taking the index of the minimum difference
		index = list_abs.index(min(list_abs))
	
		#Taking its key from list of keys of dictionary
		critical_z = keys[index]
	
		print 'Critical Z Value: ', critical_z

		print 'Calculated Z Value after assuming our Null Hypothesis true: ', z_value

		#Checking extremity of z value wrt critical z value
		if float(z_value) > float(critical_z):

			print 'We REJECT the Null Hypothesis since our Z Value is more extreme than our Critical Z Vaue.'
			
		elif float(z_value) == float(critical_z):
		
			print 'We ACCEPT the Null Hypothesis since our Z Value is equally extreme as our Critical Z Value.'

		else:
			
			print 'We ACCEPT the Null Hypothesis since our Z Value is less extreme than our Critical Z Value.'

	#If two tailed
	elif choice == '2':

		#Calculating z value
		z_value = (abs(null_mean - alternate_mean)) / (deviation / sample_size_sqrt)

		#Area for critial point
		critical_point = 100.00 - (alpha/2.0)

		#Empty list to store the differences
		list_abs = []

		#Iterating over the keys and values of the dictionary
		for key,value in z_table.iteritems():

			#Appending the magnitude of the difference
			list_abs.append(abs(value - critical_point))

		#Taking index of the minimum difference
		index = list_abs.index(min(list_abs))
	
		#Taking its key from list of keys of dictionary
		critical_z = keys[index]
	
		print 'Critical Z Value: ', critical_z	

		print 'Calculated Z Value after assuming our Null Hypothesis true: ', z_value

		#Checking extremity of z value wrt critical z value
		if float(z_value) > float(critical_z):

			print 'We REJECT the Null Hypothesis since our Z Value is more extreme than our Critical Z Vaue.'

		elif float(z_value) == float(critical_z):
		
			print 'We ACCEPT the Null Hypothesis since our Z Value is equally extreme as our Critical Z Value.'

		else:
			
			print 'We ACCEPT the Null Hypothesis since our Z Value is less extreme than our Critical Z Value.'

#Else if t test
else:
	print ('Sorry for the inconvenience. I am not designed to tackle T-Statistics Test.')
