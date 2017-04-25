from behave import step, use_step_matcher


import environment


class Calculator(object):
    @step('the Calculator app is loaded')
    def app_is_loaded(context):
        context.browser.get(
            'http://seleniumsimplified.com/testpages/calculate.php'
        )

    @step('there is no current value in the calculator')
    def check_current_value(context):
        first_number_input = context.browser.find_element_by_xpath(
            '//input[@id=\'number1\']'
        )
        second_number_input = context.browser.find_element_by_xpath(
            '//input[@id=\'number2\']'
        )

        if first_number_input.get_attribute('value') != '':
            first_number_input.clear()
            if second_number_input.get_attribute('value') != '':
                second_number_input.clear()
        assert (
            first_number_input.get_attribute('value') == '' and
            second_number_input.get_attribute('value') == ''
            )

    use_step_matcher('re')

    @step(
        'you enter \'(?P<number>.*)\' as the (?P<field>first|second) '
        'number in the calculator'
        )
    def enter_number(context, number, field):
        if field == 'first':
            first_number_input = context.browser.find_element_by_xpath(
                '//input[@id=\'number1\']'
            )
            first_number_input.send_keys(number)
            context.browser.first_number = int(number)
        else:
            second_number_input = context.browser.find_element_by_xpath(
                '//input[@id=\'number2\']'
            )
            second_number_input.send_keys(number)
            context.browser.second_number = int(number)
    use_step_matcher('parse')

    @step('you click the \'{operation}\' button')
    def click_option(context, operation):
        option = context.browser.find_element_by_xpath(
            '//option[contains(., \'{operation}\')]'.format(
                operation=operation
                )
        )
        option.click()
        context.browser.option = operation

    @step('you click the equals button')
    def click_equals(context):
        equals = context.browser.find_element_by_xpath(
            '//input[@id=\'calculate\']'
        )
        equals.click()

    @step(
        'the value displayed is the correct result for the two numbers entered'
        )
    def correct_answer(context):
        answer = context.browser.find_element_by_xpath(
            '//span[@id=\'answer\']'
            )
        answer_text = answer.text
        if context.browser.option == 'plus':
            assert answer_text == str(
                context.browser.first_number + context.browser.second_number
            )
        elif context.browser.option == 'minus':
            assert answer_text == str(
                context.browser.first_number - context.browser.second_number
            )
        elif context.browser.option == 'times':
            assert answer_text == str(
                context.browser.first_number * context.browser.second_number
            )
        elif context.browser.option == 'divide':
            if (context.browser.second_number != 0):
                assert answer_text in str(
                    context.browser.first_number /
                    context.browser.second_number
                )
            else:
                assert answer_text == '0'
