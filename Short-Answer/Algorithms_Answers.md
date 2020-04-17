#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
o(n) linear since its also being calculated on line 11. a increments by n and n is incremented by itself n times

b)
o(n log n) linearithmic due to the nested loop being traversed will result at an exponential rate

c)
o(n\*\*2) polynomial as bunnies grow the time to execute doubles due to line 29

## Exercise II

store the lowest floor that an egg breaks
if an egg is dropped from the first floor and breaks, get the middle floor
return the lowest floor var if an egg is dropped from the middle floor and breaks
return the lowest floor var if an egg is dropped from the middle or last floor and doesn't break
call function for the top and bottom floors and store the results in the lowest floor var
return the lowest floor var

o(n log n)
