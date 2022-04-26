Jonathan Chavarria
CS 491
Documentation

app.py is my Recursive Postive Integer Equation solver, it has support for addition, subtraction, multiplication and integer division. 
test_app.py has 89% test coverage and 5 integration tests. 

In order for my code to support proper PEMDAS I made two seperate functions for MD (multiplication/division) and AS (addition/subtraction). So, my code first calls the MD fucntion which from left to right solves the part of the problem having to do with MD one at a time and passes the new equation into the MD function again until there are no more multiplication or division symbols in the equation, then it passes the eq with no MD signs into the AS function where similiar steps are taken.

This made my integration testing simple as it tests the integration between those two functions. This is key because some situations are "impossible" to occur in actual run time. For example there had to be a if case for when an MD operator was not the first operator found, but this did not need to be in the AS function because in runtime AD is called second so either '+' or '-' would be the first operator in the equation.

For automation I used Github Actions and Azure together. My .yml file Tests and Deploys to an Azure app service server whenever a change is made to the repo.

