from time import sleep
from selenium import webdriver
tuong = webdriver.Chrome(executable_path=r"C:\Users\DELL\Documents\selenium\chromedriver.exe")
tuong.set_window_size(1000,1000)
tuong.get("https://tuong-tran.glitch.me/?fbclid=IwAR2pkuHM3dK9d3AkitjSo3vPEEF9n9HVXEIbY6tIAw9WWxAdDPi5jOrmEMA")