# Maytee Kneitz
# Sequential  Processing
# April 29, 2014
# Due  April 29, 2014

# Obtains input from user to determine the desired first and last names.
print "Enter the student's first name: "
desired_first_name=STDIN.gets.chomp
print "Enter the student's last name: "
desired_last_name=STDIN.gets.chomp

# Sets the variables for total_grade_points and total__credit_hours 
total_credit_hours = 0.0
total_grade_points = 0.0

# create file object fin
# Pseudocode  used file open, but the directions asked for redirection - Not sure which one applied. 
# I could have also used the code in the below comment to use redirection
#   > ruby kneitz_assign_5.rb < student-records.txt

fin=File.open("student-records.txt", "r") 


# Read and throws away the header line with column names
fin.gets

while line = fin.gets
	fields=line.chomp.split(',')
	last_name = fields[1]
	first_name = fields[2]
	credit_hours= fields[6]
	grade= fields[7]

	# Sets variables to integer and float instead of strings 
	credit_hours = credit_hours.to_i
    grade_points = grade_points.to_f

    # Checks if the entered first name and last name match a record in student-records.txt
    if first_name == desired_first_name && last_name == desired_last_name
        
        if grade == "A"
            grade_points = credit_hours * 4
        elsif grade == "B"
            grade_points = credit_hours * 3
        elsif grade == "C"
            grade_points = credit_hours * 2
        elsif grade == "D"
            grade_points = credit_hours * 1
        elsif grade == "F"
            grade_points = credit_hours * 0
        end        
         
    	total_credit_hours = total_credit_hours + credit_hours
    	total_grade_points = total_grade_points + grade_points
    end
end

# Closes the input file
fin.close

# Calculates and outputs the GPA of the student
gpa = total_grade_points / total_credit_hours
print "The GPA for ",  desired_first_name, " ", desired_last_name, " is ", gpa
