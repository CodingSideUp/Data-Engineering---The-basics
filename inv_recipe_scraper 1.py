from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


csv_file = 'C:/Users/vandi/Desktop/SRH/BLOCK 3/Data Engineering 1 - Bin Vuh/data_eng_proj_directory/stpatricks_recipes.csv'
df = pd.read_csv(csv_file)

recipe_title_list = []
recipe_rating_list = []
recipe_ingredients_list = []
recipe_cook_time = []
recipe_calories_list = []
recipe_fat_list = []
recipe_carbs_list = []
recipe_protein_list = []

# recipe_ingredients_list = ""

def inv_pg_scrape(link):
    options = webdriver.ChromeOptions()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(
    options=options)
    time.sleep(5)  
    driver.get(link)

    recipe_title = driver.find_element(By.ID,"article-heading_1-0").text
    recipe_title_list.append(recipe_title)
    try:
        recipe_rating = driver.find_element(By.ID,"mntl-recipe-review-bar__rating_1-0").text
        print(recipe_rating)
        recipe_rating_list.append(recipe_rating)
    except NoSuchElementException:
        r = print("0.0")
        recipe_rating_list.append(r)
    
    print(recipe_title)

    recipe_ingredients = driver.find_elements(By.CLASS_NAME,"mntl-structured-ingredients__list-item")
    # recipe_ingredients_list = ""
    ing = ""
    for ingredient in recipe_ingredients: 
        ing = ing + "," + ingredient.text  
        # recipe_ingredients_list.append(ingredient.text)
        # recipe_ingredients_list = recipe_ingredients_list + "," + ingredient.text
        # print(ingredient.text)
    recipe_ingredients_list.append(ing)
    # try:
    #     cooking_time = driver.find_elements(By.CLASS_NAME,"mntl-recipe-details__value")
    #     for ctime in cooking_time[2:3]:
    #         ct = ctime.text
    #         print(ct)
    #         recipe_cook_time.append(ct)
    # except NoSuchElementException:
    #     print("30 mins")
    #     recipe_cook_time.append("30 mins")
    # cooking_time = driver.find_elements(By.CLASS_NAME,"mntl-recipe-details__value")
    # for ctime in cooking_time[:1]:
    #         ct = ctime.text
    #         print(ct)
    #         recipe_cook_time.append(ct)
    cooking_time = driver.find_elements(By.CLASS_NAME, "mntl-recipe-details__value")

    try:
        # Try to get the first cooking time element
        ct = cooking_time[0].text
    except (IndexError, NoSuchElementException):
        # Handle the exception if the element is not found or list index is out of range
        print("Default cooking time: 30 mins")
        ct = "30 mins"

    print(ct)
    recipe_cook_time.append(ct)


    # try:
    #     recipe_facts = driver.find_elements(By.CLASS_NAME,"mntl-nutrition-facts-summary__table-row")
    #     for rcals in recipe_facts[:1]:
    #         rc = rcals.text
    #         print(rc)
    #         recipe_calories_list.append(rc)
    # except NoSuchElementException:
    #     print("0 Calories")
    #     recipe_calories_list.append("0 Calories")

    # try:
    #     for rfat in recipe_facts[1:2]:
    #         rf = rfat.text
    #         print(rf)
    #         recipe_fat_list.append(rf)
    # except NoSuchElementException:
    #     print("0g Fat")
    #     recipe_fat_list.append("0g Fat")

    # try:     
    #     for rcarbs in recipe_facts[2:3]:
    #         rcb = rcarbs.text
    #         print(rcb)
    #         recipe_carbs_list.append(rcb)
    # except NoSuchElementException:
    #     print("0g Carbs")
    #     recipe_carbs_list.append("0g Carbs")

    # try:    
    #     for rprot in recipe_facts[3:4]:
    #         rpt = rprot.text
    #         print(rpt)
    #         recipe_protein_list.append(rpt)
    # except NoSuchElementException:
    #     print("0g Protein")
    #     recipe_protein_list.append("0g Protein")
    
    recipe_facts = driver.find_elements(By.CLASS_NAME, "mntl-nutrition-facts-summary__table-row")

    nutritional_categories = ["Calories", "Fat", "Carbs", "Protein"]
    nutritional_lists = [recipe_calories_list, recipe_fat_list, recipe_carbs_list, recipe_protein_list]

    for i, category in enumerate(nutritional_categories):
        try:
            if i < len(recipe_facts):
                nutritional_value = recipe_facts[i].text
                print(f"{category}: {nutritional_value}")
                nutritional_lists[i].append(nutritional_value)
            else:
                raise NoSuchElementException("Index out of range")
        except NoSuchElementException:
            zero_value = f"0g {category}"
            print(zero_value)
            nutritional_lists[i].append(zero_value)
            continue  # Continue to the next iteration after handling the exception


    
    # print(recipe_rating)
    # for recipe in recipe_ingredients:
    #     print(recipe.text)

    # driver.quit()


# for link in df.iloc[:,1]:
#     inv_pg_scrape(link)
for link in df.iloc[:,1]:
    try:
        inv_pg_scrape(link)
    except Exception as e:
        # Handle the exception, print or log the error
        print(f"Error processing link {link}: {e}")


print(len(recipe_title_list))
print(len(recipe_rating_list))
print(len(recipe_ingredients_list))
print(len(recipe_cook_time))
print(recipe_cook_time)
print(len(recipe_calories_list))
print(len(recipe_protein_list))
print(len(recipe_fat_list))
print(len(recipe_carbs_list))

breakfast_recipes_ingredients = {"Recipes":recipe_title_list,"Rating":recipe_rating_list,"Ingredients":recipe_ingredients_list,"Cook_Time":recipe_cook_time,"Calories":
                                 recipe_calories_list,"Protein":recipe_protein_list,"Fat":recipe_fat_list,"Carbs":recipe_carbs_list}
df = pd.DataFrame(breakfast_recipes_ingredients)
# print(df)
df.to_csv('stpatricks_new_inv.csv', index=False)