
def insert_reward_chipotle(site, reward_number):
    i = 0 
    site.find_element_by_id('CN1').send_keys(reward_number[i:i + 3])
    i += 3
    site.find_element_by_id('CN2').send_keys(reward_number[i:i + 3])
    i += 3
    site.find_element_by_id('CN3').send_keys(reward_number[i:i + 3])
    i += 3
    site.find_element_by_id('CN4').send_keys(reward_number[i:i + 3])
    i += 3
    site.find_element_by_id('CN5').send_keys(reward_number[i:i + 3])
    i += 3
    site.find_element_by_id('CN6').send_keys(reward_number[i:i + 3])
    i += 3
    site.find_element_by_id('CN7').send_keys(reward_number[i:i + 2])


def get_chipotle_information(site, split_text):
    curr = 50
    is_a_number = True
    reward_number = ''
    while is_a_number:
        reward_number += split_text[curr]
        if split_text[curr + 1].isnumeric():
            curr += 1
        else:
            is_a_number = False
    reward_code = chipotle_website_survey_completer(site, reward_number)
    return reward_code


def chipotle_website_survey_completer(site, reward_number):
    site.get("https://ChipotleFeedback.com")

    result = site.find_element_by_class_name('radioSimpleInput').is_selected()
    if result:
        print("Checkbox already selected")
    else:
        site.find_element_by_class_name('radioSimpleInput').click()
        print("Checkbox selected")

    site.find_element_by_id('NextButton').click()
    insert_reward_chipotle(site, reward_number)
    
    # navigate to next page
    site.find_element_by_id('NextButton').click()

    # Survey

    #Question: How was your Overall Experience?  /  Answer: 5 stars rating
    site.find_element_by_id("ANS003000.5").click()

    #Question: What type of experience did you have?  /  Answer: It randomizes dine-in/carry-out, but it doesn't matter
    dine_in_or_carry_out = site.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[1]/form/div/fieldset/div/div/div[2]').click()
    # Which of the following did you order? (Select all that apply)

    site.find_element_by_css_selector('#FNSR000131 > label').click()

    site.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/div[1]/form/div/div[3]/input').click()
    site.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/div[4]/input').click()
    site.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/fieldset/div/div/div[6]/div[5]').click()
    site.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/form/div/fieldset/div/div/div[6]/div[5]').click()


    #link = driver.find_element_by_link_text("")
    # driver.quit()