from selenium import webdriver
import pyautogui
import time
import math
from selenium.webdriver.common.by import By

def switch2frame(par):
    par.switch_to.frame('secondIframe')
    par.switch_to.frame('thirdIframe')
    par.switch_to.frame('dataMainIframe')


def run_main(video_unstudy_num,text, browser):
    if int(video_unstudy_num) > 0:
        print("nonlocal--{}目录下还有{}个视频未学习……".format(text,video_unstudy_num))
        js_click = 'document.getElementsByClassName("courseware-reed")[0].click()'
        browser.execute_script(js_click)
        time.sleep(3)
        # 拿到所有的窗口
        all_handles = browser.window_handles
        pre_window_handle = browser.current_window_handle
        for handle in all_handles:
            if handle != pre_window_handle:
                browser.switch_to.window(handle)
                browser.implicitly_wait(10)
                # time.sleep(10)
                # elem = browser.find_element_by_class_name("introjs-button")
                elem = browser.find_element(By.ID,"btnConfirm")
                elem.click()
                time.sleep(2)
                browser.switch_to.alert.accept()
                browser.switch_to.frame('course_frame')
                time.sleep(10)
                # 点击播放
                js_paused = 'return document.getElementById("my-video_html5_api").paused;'
                view_paused_status = browser.execute_script(js_paused)
                print('viewPaused：' + str(view_paused_status))
                # false 点击了播放  true 点击了暂停
                if view_paused_status:
                    elem = browser.find_element_by_class_name("vjs-play-control")
                    elem.click()
                time.sleep(5)
                # 获取视频播放时长?
                js_duration_str = 'return document.getElementById("my-video_html5_api").duration;'
                view_time = browser.execute_script(js_duration_str)
                print('viewTime:' + str(view_time))
                time.sleep(5)
                js_current_time_str = 'return document.getElementById("my-video_html5_api").currentTime;'
                view_current_time = browser.execute_script(js_current_time_str);
                print('viewCurrentTime:' + str(view_current_time))

                if math.ceil(view_current_time) >= math.ceil(view_time):
                    print('{}'.format(text))
                    browser.switch_to.default_content()
                    browser.switch_to.alert.accept()
                    elem = browser.find_element(By.ID,'btnexit')
                    elem.click()
                    # 关闭视频网站页面 进入pre_window_handle页面
                    browser.switch_to.window(pre_window_handle)
                    browser.refresh()
                    browser.implicitly_wait(10)
                    switch2frame(browser)
                    js_list = 'return document.getElementsByClassName("courseware-reed").length;'
                    video_unstudy_num = browser.execute_script(js_list)
                    time.sleep(3)
                    # print("local--该目录下还有{}个视频未学习……".format(video_unstudy_num))
                    run_main(video_unstudy_num, text,browser)
                else:
                    print('{}播放开始'.format(text))
                    time.sleep(math.ceil(view_time) - math.ceil(view_current_time))
                    browser.switch_to.default_content()
                    #elem = browser.find_element_by_xpath('//*[@id="len1"]/li[2]/img')
                    #elem.click()
                    #time.sleep(1)
                    elem = browser.find_element(By.ID,'btnexit')
                    elem.click()
                    #browser.switch_to.alert.accept()
                    # elem = browser.find_element_by_id('btnexit')
                    # elem.click()
                    # 关闭视频网站页面 进入pre_window_handle页面
                    browser.switch_to.window(pre_window_handle)
                    browser.refresh()
                    browser.implicitly_wait(10)
                    switch2frame(browser)
                    js_list = 'return document.getElementsByClassName("courseware-reed").length;'
                    video_unstudy_num = browser.execute_script(js_list)
                    time.sleep(3)
                    # print("local--该目录下还有{}个视频未学习……".format(video_unstudy_num))
                    run_main(video_unstudy_num,text, browser)
    else:
        print("该目录下还有视频已学习完毕……")

def run_main1(video_studying_num,browser):
    if int(video_studying_num) > 0:
        progress=browser.find_element(By.XPATH, '//*[@id="gvList"]/tbody/tr[{}]/td[5]'.format(i+2)).text
        if progress!='100%':
            print("nonlocal--学习信息目录下还有{}个视频未学习……".format(video_studying_num))
            js_click = 'document.getElementsByClassName("courseware-list-reed")[0].click()'
            browser.execute_script(js_click)
            time.sleep(3)
            # 拿到所有的窗口
            all_handles = browser.window_handles
            browser.switch_to.window(all_handles[0])
            pre_window_handle = browser.current_window_handle
            for handle in all_handles:
                if handle != pre_window_handle:
                    browser.switch_to.window(handle)
                    browser.implicitly_wait(10)
                    # time.sleep(10)
                    # elem = browser.find_element_by_class_name("introjs-button")
                    browser.switch_to.frame('course_frame')
                    time.sleep(10)
                    # 点击播放
                    js_paused = 'return document.getElementById("my-video_html5_api").paused;'
                    view_paused_status = browser.execute_script(js_paused)
                    print('viewPaused：' + str(view_paused_status))
                    # false 点击了播放  true 点击了暂停
                    if view_paused_status:
                        elem = browser.find_element(By.CLASS_NAME,"vjs-play-control")
                        elem.click()
                    time.sleep(5)
                    # 获取视频播放时长?
                    js_duration_str = 'return document.getElementById("my-video_html5_api").duration;'
                    view_time = browser.execute_script(js_duration_str)
                    print('viewTime:' + str(view_time))
                    time.sleep(5)
                    js_current_time_str = 'return document.getElementById("my-video_html5_api").currentTime;'
                    view_current_time = browser.execute_script(js_current_time_str);
                    print('viewCurrentTime:' + str(view_current_time))

                    if math.ceil(view_current_time) >= math.ceil(view_time):
                        print('播放结束')
                        browser.switch_to.default_content()
                        elem = browser.find_element(By.ID,'btnexit')
                        elem.click()
                        # 关闭视频网站页面 进入pre_window_handle页面
                        browser.switch_to.window(pre_window_handle)
                        browser.refresh()
                        browser.implicitly_wait(10)
                        switch2frame(browser)
                        js_list = 'return document.getElementsByClassName("courseware-list-reed").length;'
                        video_studying_num= browser.execute_script(js_list)
                        time.sleep(3)
                        # print("local--该目录下还有{}个视频未学习……".format(video_unstudy_num))
                        run_main1(video_studying_num, browser)
                    else:
                        print('播放开始')
                        time.sleep(math.ceil(view_time) - math.ceil(view_current_time))
                        browser.switch_to.default_content()
                        elem = browser.find_element(By.ID,'btnexit')
                        elem.click()
                        # 关闭视频网站页面 进入pre_window_handle页面
                        browser.switch_to.window(pre_window_handle)
                        browser.refresh()
                        browser.implicitly_wait(10)
                        switch2frame(browser)
                        js_list = 'return document.getElementsByClassName("courseware-list-reed").length;'
                        video_studying_num = browser.execute_script(js_list)
                        time.sleep(3)
                        # print("local--该目录下还有{}个视频未学习……".format(video_unstudy_num))
                        run_main1(video_studying_num, browser)
    else:
        print("该目录下视频已学习完毕……")


#点击评价
def assess(video_studying_num,browser):
    js_click = 'document.getElementsByClassName("courseware-reed")[{}].click()'.format(video_studying_num-1)
    browser.execute_script(js_click)
    time.sleep(3)
    # 拿到所有的窗口
    all_handles = browser.window_handles
    pre_window_handle = browser.current_window_handle
    for handle in all_handles:
        if handle != pre_window_handle:
            browser.switch_to.window(handle)
            browser.implicitly_wait(10)
            elem = browser.find_element(By.XPATH, '//*[@id="len1"]/li[2]/img')
            elem.click()
            time.sleep(1)
            elem = browser.find_element(By.XPATH, '//*[@id="cmdSubmit"]')
            elem.click()
            time.sleep(1)
            browser.switch_to.alert.accept()


def main():
    # 输入账号
    username=""
    # 输入密码
    passwd=""
    login_url = 'https://gbpx.gd.gov.cn/gdceportal/index.aspx'
    option = webdriver.ChromeOptions()
    #option.add_argument("headless")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--mute-audio')
    browser = webdriver.Chrome(options=option)
    browser.get(login_url)
    browser.implicitly_wait(10)
    # 窗口最大化
    #browser.maximize_window()
    # elem=browser.find_element_by_xpath('//*[@id="pnlLogin"]/div[1]/div[1]')
    # elem.click()
    # time.sleep(1)
    elem = browser.find_element(By.ID,"txtLoginName")
    elem.clear()
    elem.send_keys(username)
    time.sleep(1)
    elem = browser.find_element(By.ID,"txtPassword")
    elem.clear()
    elem.send_keys(passwd)
    time.sleep(1)
    elem = browser.find_element(By.ID, 'cbAgree')
    elem.click()
    time.sleep(1)
    # 验证码
    code_num = pyautogui.prompt("请输入验证码:")
    elem = browser.find_element(By.ID,"txtValid")
    elem.clear()
    elem.send_keys(code_num)
    elem = browser.find_element(By.XPATH,'//*[@id="user-login-form"]/div[2]/input[1]')
    elem.click()
    time.sleep(1)
    elem = browser.find_element(By.ID,'btnStudy')
    elem.click()
    time.sleep(1)
    # browser.switch_to_frame('secondIframe')
    # browser.switch_to.frame('secondIframe')
    # browser.switch_to.frame('thirdIframe')
    # browser.switch_to.frame('dataMainIframe')
    elems = browser.find_elements(By.CLASS_NAME,'leftHrefChild')
    for i in range(0,len(elems)):
        #返回主文档
        browser.switch_to.default_content()
        elems = browser.find_elements(By.CLASS_NAME,'leftHrefChild')
        print(elems[i].text)
        if  "学习信息" in elems[i].text:
            switch2frame(browser)
            #返回当前页面中 class 为 courseware-list-reed 的元素个数
            js_list1 = 'return document.getElementsByClassName("courseware-list-reed").length;'
            video_studying_num = browser.execute_script(js_list1)
            for i in range(0, int(video_studying_num)):
                print(i)
                assess(video_studying_num,browser)
                all_handles = browser.window_handles
                browser.switch_to.window(all_handles[0])
                run_main1(video_studying_num,browser)

            continue
        text=elems[i].text
        elems[i].click()
        time.sleep(1)
        switch2frame(browser)
        js_list = 'return document.getElementsByClassName("courseware-reed").length;'
        video_unstudy_num = browser.execute_script(js_list)
        time.sleep(3)
        print(video_unstudy_num)
        run_main(video_unstudy_num, text,browser)
    browser.close()
    print("end......")


if __name__ == '__main__':
    main()