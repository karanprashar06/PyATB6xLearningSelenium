## **Project 1 - Automating by using the Selenium Python.**
# 1. Navigate to the URL - [katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
# 2. Find the **Make appointment** Button
# 3. Click on the **Make appointment** Button
# 4. Next Page will be loaded
# 5. **Find and Enter** the details **Username and Password** and **Click** on the Login Button
# 6. Verify current URL - [katalon-demo-cura.herokuapp.com/#appointment](https://katalon-demo-cura.herokuapp.com/#appointment)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_project_1_katalon_positive():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://instagram.com/")

    #<input class="x1i10hfl xggy1nq xtpw4lu x1tutvks x1s3xk63 x1s07b3s x1a2a7pz xjbqb8w x1v8p93f x1o3jo1z x16stqrj xv5lvn5 x1ejq31n x18oe1m7 x1sy0etr xstzfhl x972fbf x10w94by x1qhh985 x14e42zd x9f619 xzsf02u x1lliihq x15h3p50 x10emqs4 x1vr9vpq x1iyjqo2 x10d0gm4 x1fhayk4 x16wdlz0 x3cjxhe xe9ewy2 x11lt19s xeuugli xlyipyv x1hcrkkg xfvqz1d x12vv892 x1hu168l xttzon8 x1sfh74k x3fqe8q x185fvkj x1p97g3g xmtqnhx x11ig0mb xgmu6d7 x1quw8ve xx0ingd xp5op4 x1y44fgy xdzva22 xs8nzd4 x1fzehxr xha3pab"
    # dir="ltr"
    # autocomplete="username webauthn"
    # aria-invalid="false"
    # id="_R_32d9lplcldcpbn6b5ipamH1_"
    # type="text"
    # name="email"
    # value="">


    user_name_input_box = driver.find_element(By.NAME, "email")
    user_name_input_box.send_keys("karanprashar06@gmail.com")
    time.sleep(5)

    #<input class="x1i10hfl xggy1nq xtpw4lu x1tutvks x1s3xk63 x1s07b3s x1a2a7pz xjbqb8w x1v8p93f x1o3jo1z x16stqrj xv5lvn5 x1ejq31n x18oe1m7 x1sy0etr xstzfhl x972fbf x10w94by x1qhh985 x14e42zd x9f619 xzsf02u x1lliihq x15h3p50 x10emqs4 x1vr9vpq x1iyjqo2 x10d0gm4 x1fhayk4 x16wdlz0 x3cjxhe xe9ewy2 x11lt19s xeuugli xlyipyv x1hcrkkg xfvqz1d x12vv892 x1hu168l xttzon8 x1sfh74k x3fqe8q x185fvkj x1p97g3g xmtqnhx x11ig0mb xgmu6d7 x1quw8ve xx0ingd xp5op4 x1y44fgy xdzva22 xs8nzd4 x1fzehxr xha3pab"
    # dir="ltr"
    # aria-invalid="false"
    # id="_R_33d9lplcldcpbn6b5ipamH1_"
    # type="password"
    # name="pass"
    # value="">

    password_input_box = driver.find_element(By.NAME, "pass")
    password_input_box.send_keys("csfdv")
    time.sleep(5)

    #<span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">
    # Log in
    # </span>


    #<div role="none" class="x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x972fbf x10w94by x1qhh985 x14e42zd x9f619 xtvsq51 xqbgfmv xbe3n85 x7a1id4 x1d9i5bo x1xila8y x1bumbmr xc8cyl1 xti2d7y">
    # <div class="html-div xdj266r xat24cr xexx8yu xyri2b x18d9i69 x1c1uobl x6s0dn4 x78zum5 xl56j7k x1e0frkt xf0ucvx xx2axb6">
    # <div role="none" class="x9f619 x1n2onr6 x1ja2u2z x193iq5w xeuugli x6s0dn4 x78zum5 x2lah0s x10ksdce x16k4gxc">
    # <span class="x1lliihq x1plvlek xryxfnj x1n2onr6 xyejjpt x15dsfln x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1sfkdl8 xurcqga x3vd66c xhqx0jl xtk6v10 x1yc453h xudqn12 x3x7a5m"
    # style="--x---base-line-clamp-line-height: calc(var(--primary-label-line-height) * 1em); --x-lineHeight: calc(var(--primary-label-line-height) * 1em);">
    # <span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">
    # Log in</span></span></div></div><div class="x1ey2m1c xtijo5x x1o0tod xg01cxk x47corl x10l6tqk x13vifvy x1ebt8du x19991ni x1dhq9h x1fmog5m xu25z0z x140muxe xo1y3bh"
    # role="none" data-visualcompletion="ignore"></div></div>


    logged_in_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
    logged_in_button.click()

    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(20)

    #not_now = driver.find_element(By.XPATH, "//span[text()='Not Now']")
    save_info = driver.find_element(By.XPATH, "//button[normalize-space()='Save info']")
    save_info.click()

    time.sleep(10)
    #driver.quit()



    send_message =driver.find_element(By.XPATH, "//span[text()='Messages']")
    send_message.click()
    time.sleep(10)

    ak_message = driver.find_element(By.XPATH, "//span[text()='Akshay Parashar']")
    ak_message.click()
    time.sleep(10)

    input_message = driver.find_element(By.XPATH, "//div[@aria-label='Message']")
    input_message.send_keys("Hello Akshay")
    time.sleep(5)

    click = message_box = driver.find_element(
    By.XPATH, "//div[@aria-label='Message' and @role='textbox']"
)
    click.click()
    time.sleep(10)



