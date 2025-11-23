Exercise 1
Q1. How many files are there? 
Answer - 6
______________________________
Q2. Did number of mapper change?
Answer - No
______________________________
Q3. Did number of reducer changed?
Answer - Yes, fron 3 to 6
______________________________
Q4. Did number of output files change? Why?
Answer - Yes because each reducer writes 1 output partition file so it will be equal to the number of reducers
______________________________
Q5. What does the value of 'Merged Map outputs' represents and how is it calculated?
Answer - It counts how many map-output segments were merged during th shuffle\sort phase, before being consumed by reducers
______________________________


Exercise 2
Q1. Is your change in the mapper or in the reducer?
Answer - In the mapper
______________________________


Exercise 3
Q1. Is your change in the mapper or in the reducer?
Answer - In the reducer
______________________________
