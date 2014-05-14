
print "Enter f name"
desired_first_name=STDIN.gets.chomp
print "Enter l name: "
desired_last_name=STDIN.gets.chomp

total_credit_hours = 0.0
total_grade_points = 0.0

# create file object fin
fin=File.open("student-records.txt", "r")

# Read and get rid of header line with column names
fin.gets

while line = fin.gets
	fields=line.chomp.split(',')
	last_name = fields[1]
	first_name = fields[2]
	credit_hours= fields[6]
	grade_points= fields[7]
	
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
               
        total_credit_hours = credit_hours
        total_grade_points =grade_points
    end
end

#close input file
fin.close

gpa = total_grade_points / total_credit_hours
print gpa
