  Feature: As a calculator user I want to add, multiply and divide numbers So I can do simple maths quickly

    Scenario: simple maths
      Given the Calculator app is loaded
      And there is no current value in the calculator
      When you enter '0' as the first number in the calculator
      And you enter '6' as the second number in the calculator
      And you click the 'plus' button
      And you click the equals button
      Then the value displayed is the correct result for the two numbers entered
      When you click the 'minus' button
      And you click the equals button
      Then the value displayed is the correct result for the two numbers entered
      When you click the 'times' button
      And you click the equals button
      Then the value displayed is the correct result for the two numbers entered
      When you click the 'divide' button
      And you click the equals button
      Then the value displayed is the correct result for the two numbers entered

    Scenario: simple maths part 2
      Given there is no current value in the calculator
      When you enter '7' as the first number in the calculator
      And you enter '1' as the second number in the calculator
      And you click the 'plus' button
      And you click the equals button
      Then the value displayed is the correct result for the two numbers entered
      When there is no current value in the calculator
      And you enter '1' as the first number in the calculator
      And you enter '8' as the second number in the calculator
      And you click the 'minus' button
      And you click the equals button
      Then the value displayed is the correct result for the two numbers entered
      When you click the 'times' button
      And you click the equals button
      Then the value displayed is the correct result for the two numbers entered
