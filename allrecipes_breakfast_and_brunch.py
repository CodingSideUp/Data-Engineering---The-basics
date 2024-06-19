from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = "https://www.allrecipes.com/recipes/197/holidays-and-events/st-patricks-day/"

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(
    options=options)

driver.get(url)
cookies_acceptor = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
cookies_acceptor.click
recipe_category = driver.find_element(By.ID,"three-post__title_1-0").text
all_recipes_in_category = driver.find_elements(By.CLASS_NAME,"card__title-text")
print(len(all_recipes_in_category))

print(recipe_category)

recipe_names_list = []
# for recipe in all_recipes_in_category[8:]:
for recipe in all_recipes_in_category[13:]:
    ls = recipe.text
    recipe_names_list.append(ls)
    # print(recipe.text)

recipes_links_list = []
# for n in range(4,64):
for n in range(6,66):
    inv_recipe_page = driver.find_element(By.ID,f"mntl-card-list-items_2-0-{n}")
    inv_pg_link = inv_recipe_page.get_attribute("href")
    recipes_links_list.append(inv_pg_link)
    # recipe_title = driver.find_element(By.ID,"article-heading_1-0").text
    # recipe_rating = driver.find_element(By.ID,"mntl-recipe-review-bar__rating_1-0").text
    # recipe_ingredients = driver.find_elements(By.CLASS_NAME,"mntl-structured-ingredients__list-item")
    # print(recipe_ingredients)
# inv_recipe_page = driver.find_elements(By.CLASS_NAME,"comp mntl-card-list-items mntl-document-card mntl-card card card--no-image")
# print(len(inv_recipe_page))

print(len(recipe_names_list))
print(len(recipes_links_list))
lunch_recipes = {"Recipes":recipe_names_list,"Links":recipes_links_list}
df = pd.DataFrame(lunch_recipes)
print(df)
df.to_csv('stpatricks_recipes.csv', index=False)

