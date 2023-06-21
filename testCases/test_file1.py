# from selenium import webdriver
# from selenium.webdriver.common.service import Service
# headless_option = webdriver.ChromeOptions()
# headless_option.add_argument("headless")
#
# class Test_Pytest:
#
#     def test_sum_001(self):
#         a = 3
#         b = 4
#         sum = a + b
#         print(sum)
#         if sum == 7:
#             assert True
#         else:
#             assert False
#
#     def test_sum_002(self):
#         a = 5
#         b = 4
#         sum = a + b
#         print(sum)
#         if sum == 9:
#             assert True
#         else:
#             assert False

# def test_mul_003(self):
#     a = 5
#     b = 4
#     mul = a * b
#     print(mul)
#     if mul == 20:
#         assert True
#     else:
#         assert False
#
# def test_Credence_Url_004(self):
#
#     driver = webdriver.Chrome(options= headless_option)
#     driver.get("https://credence.in/")
#     if driver.title == "Credence":
#         print("You are at Right place")
#     else:
#         print("You are at Wrong place")
#
#
# def test_Credence_Url_009(self):
#     driver = webdriver.Chrome(options= headless_option)
#     driver.get("https://credence.in/")
#     if driver.title == "Credence1":
#         print("You are at Right place")
#     else:
#         print("You are at Wrong place")

from selenium import webdriver
from selenium.webdriver.common.service import Service


# class Test_Pytest:
#
#      def  test_cred_001(self):
#           driver=webdriver.Chrome()
#           driver.title=='Credence'
#           if driver.title in 'Credence':
#                print('u r right bro')
#           else:
#                print('u are wrog bro')


def test_cred_001(self):
    driver = webdriver.Chrome()
    driver.title == 'Credence'
    if driver.title in 'Credence':
        print('you are in right path')
    else:
        print('you are not in right path')
