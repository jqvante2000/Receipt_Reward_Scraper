
def get_panda_express_information(site, split_text):    
    reward_number = split_text[102]
    revised_reward_number = ''
    for letter in reward_number:
        if letter.isnumeric():
            revised_reward_number += letter
    reward_code = panda_express_survey_completer(site, revised_reward_number)
    return reward_code

def insert_reward_panda(site,reward_number):
    i = 0
    site.find_element_by_id('CN1').send_keys(reward_number[i:i + 4])
    i += 4
    site.find_element_by_id('CN2').send_keys(reward_number[i:i + 4]) 
    i += 4
    site.find_element_by_id('CN3').send_keys(reward_number[i:i + 4])
    i += 4
    site.find_element_by_id('CN4').send_keys(reward_number[i:i + 4])
    i += 4
    site.find_element_by_id('CN5').send_keys(reward_number[i:i + 4])
    i += 4
    site.find_element_by_id('CN6').send_keys(reward_number[i:i + 4])
    i += 2

def panda_express_survey_completer(site, reward_number):
    site.get("https://pandaguestexperience.com")
    insert_reward_panda(site, reward_number)
    site.find_element_by_id('NextButton').click()
    site.find_element_by_id('NextButton').click() # not sure why it requires you to click the button twice

    # Please rate your overall satisfaction with your Panda Express experience:
    site.find_element_by_class_name("radioSimpleInput").click()
    site.implicitly_wait(3)
    site.find_element_by_id('NextButton').click()

    # Please rate your satisfaction with ...
    panda_express_highly_satisfied(site)
    panda_express_highly_satisfied(site)
    panda_express_highly_satisfied(site)
    panda_express_highly_satisfied(site)

    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[5]/span/span').click()
    site.find_element_by_id('NextButton').click() 

    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[5]/span').click()
    site.find_element_by_id('NextButton').click() 

    panda_express_highly_satisfied(site)
    set_text_field(site)

    # Rate satisfaction with panda express location related to health crisis
    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[1]/span').click()
    site.find_element_by_id('NextButton').click() 


    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').click()
    site.find_element_by_id('NextButton').click() 

    # How many times you visited Panda Express
    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/fieldset/div/div/div[4]/span/span').click()
    site.find_element_by_id('NextButton').click() 

    # How likely is it that you will enter the "Embrace Your Inner Panda" Sweepstakes?
    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[1]/span').click()
    site.find_element_by_id('NextButton').click() 

    # Final questions... Gender:
    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[3]/div[2]/div/select/option[3]').click()
    #Age:
    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[4]/div[2]/div/select/option[3]').click()

    #Annual household:
    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[5]/div[2]/div/select/option[8]').click()

    site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[6]/div[2]/div/select/option[9]').click()
    
    site.find_element_by_id('NextButton').click() 

    redemption_code = site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[1]/span')
    
    print('\n\n',redemption_code)

def set_text_field(site):
    text = 'I am satisfied because the food tasted well. I enjoyed the staff members hospitality and ability to quickly serve my food. The staff served warm food and gave good portions.'

    text_area = site.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[2]/div[2]/div/div/div[2]/textarea')
    text_area.click()
    text_area.send_keys(text)
    site.find_element_by_id('NextButton').click() 

def panda_express_highly_satisfied(site):

    flag = 0
    tbody = site.find_element_by_css_selector('tbody')
    rows = tbody.find_elements_by_css_selector('tr')
    num_rows = len(rows) - 1
    end_program = False
    for row in rows:
        if end_program:
            break
        columns = row.find_elements_by_css_selector('td')
        for cell in columns:
            if flag == 0:
                flag += 1
                break 
            elif num_rows == 6:
                # reduce code below later by creating a temp string and counter for xpath
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[1]/span').click()
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[1]/span').click()
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[4]/td[1]/span').click()
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[5]/td[1]/span').click()
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[6]/td[1]/span').click()
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[7]/td[1]/span').click()
                end_program = True
                break
            elif num_rows == 1:
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[1]/span').click()
                end_program = True
                break 
            elif num_rows == 2:
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[1]/span').click()
                cell.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[1]/span').click()
                end_program = True
                break 
    site.find_element_by_id('NextButton').click()  
