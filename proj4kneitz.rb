#  Maytee Kneitz
# Draw Two Letters ( A and X)
# Due 5/8/14
# Submission Date 5/7/14


# Letter X drawing

# Draw first diagonal
for y in 1..15
  for x in 1..(1+y)
    print " "
  end
  for x in 5..9
    print "*"
  end
  for x in 10..(38-y-y+1)
  	print " "
  end
  for x in 1..5
  	print "*"
  end
 print "\n"
end


#Draw next diagonal 
for x in 1..15
  for y in 1..(17 - x)
    print " "
  end
  for y in 1..5
    print "*"
  end
  for y in 4..(1+ x +x)
    print " "
  end
  for y in 1..5
    print "*"
  end
  print "\n"
end

print "\n"

# Draw letter A
# Prints the upper portion of the A
for y in 1..5
  for x in 1..(17 - y)
    print " "
  end
  for x in 1..5
    print "*"
  end
  for x in 4..(1+ y +y)
    print " "
  end
  for x in 1..5
    print "*"
  end
  print "\n"
end

# Print horizontal line
for x in 4..5
  for y in 11..15
    print " "
    end
  end
  for x in 3..5
    for y in 1..7
      print "*"
    end
end
print "\n"

# Print bottom diagonals
for x in 1..5
  for y in 1..(10 - x)
    print " "
  end
  for y in 1..5
    print "z"
  end
  for y in -9..(1+ x +x)
    print " "
  end
  for y in 1..5
    print "p"
  end
  print "\n"
end





