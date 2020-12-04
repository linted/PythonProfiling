# Python Profiling
This repo seeks to find answers to common speed questions in python.

## Question 1: `if/else` or dictionaries
In this test we compare the performance impact of using `if/else` statements or using a dictionary as a switch statement.
 -  Is a dictionary faster then an if statement for decision trees?
 -  Is there a point where one should be used over the other?
 -  Does the type of data being compaired against change the performance characteristics?
 -  Do `elif` statements impact the performance of a program?
 -  What hidden overheads are assiciated with both styles (ie. Memory usage, hidden multi-threaded overheads...)?

### Notes of issues found while building
- elif statments appear to have a hard limit at 2996 conditions