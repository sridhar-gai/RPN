@successful_evaluation
Feature: RPN Calculator
As a customer I would like to enter an RPN expression
So that I can see the result of the expression
Scenario: Binary expression - success case
Given I have entered "2,3,*"
When click on "Evaluate"
Then System display message "6"
