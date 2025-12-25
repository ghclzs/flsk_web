import requests



admin_token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ1c2VyX25hbWUiOiJjYW95b25neW9uZ0Bncm91cHl1c2h1bi5jb20iLCJyZWFsX25hbWUiOiLmm7nli4fli4ciLCJhdmF0YXIiOiIiLCJhdXRob3JpdGllcyI6WyJQVF9URVNUX0xFQURFUiJdLCJjbGllbnRfaWQiOiJjX3VuaWFwcCIsInJvbGVfbmFtZSI6IlBUX1RFU1RfTEVBREVSIiwibGljZW5zZSI6InBvd2VyZWQgYnkgYmxhZGV4IiwicG9zdF9pZCI6IiIsInVzZXJfaWQiOiIxNzczNTQ2Mjg4MTA3MTYzNjQ5Iiwicm9sZV9pZCI6IjE3NTI4ODQyNTUyODY4MzMxNTQiLCJzY29wZSI6WyJhbGwiXSwibmlja19uYW1lIjoiIiwib2F1dGhfaWQiOiIiLCJkZXRhaWwiOnsidHlwZSI6IndlYiIsInBob25lIjoiMTg3NzA4MTMyOTIiLCJjdXN0b21lcklkIjpudWxsLCJyb2xlSWQiOm51bGwsInVzZXJUeXBlIjoxLCJmaXJzdFJlZ2lzdGVyIjpmYWxzZX0sImV4cCI6MjMzNzQ3MTc5MiwiZGVwdF9pZCI6Ii0xIiwianRpIjoiZjdkYmFhZjYtZmM1ZC00YjI5LWE4YzYtMzUwNzFmZTdhNmJkIiwiYWNjb3VudCI6ImNhb3lvbmd5b25nQGdyb3VweXVzaHVuLmNvbSJ9.3fICcymFed0in_TbfAlrBJO0ksuXm46BRlUr26RRVR0"
class CodeServices():
    def __init__(self):
        self.url = "https://huijob.groupyushun.com"
        self.header =  {
            "isSkipSign": "true",
            "client-id": "saber",
            "content-type": "application/json",
            "Authorization": "Basic Y191bmlhcHA6Y191bmlhcHBfc2VjcmV0",
            "Blade-Auth":"bearer "+admin_token
        }
    #获取线上c小程序验证码
    def get_c_captcha(self,phone):
        url = self.url+"/api/biz-fnd/cache/get?key=c-applet:login:phone_captcha:"+str(phone)
        result = requests.get(url=url,headers=self.header).json()
        return result

    #查询b小程序验证码
    def get_b_captcha(self,phone):
        url = self.url+"/api/biz-fnd/cache/get?key=login:phone_captcha:"+str(phone)
        result = requests.get(url=url,headers=self.header).json()
        return result

    #查询m站验证码
    def get_m_captcha(self,phone):
        url = self.url+"/api/biz-fnd/cache/get?key=m-website:phone_captcha:"+str(phone)
        result = requests.get(url=url,headers=self.header).json()
        return result

    #查询bweb验证码
    def get_B_captcha(self,phone):
        url = self.url + "/api/biz-fnd/cache/get?key=m-website:phone_captcha:" + str(phone)
        result = requests.get(url=url, headers=self.header).json()
        return result

    def get_edu_b_captcha(self,phone):
        url = self.url + "/api/biz-fnd/cache/get?key=edu:login:phone_captcha:" + str(phone)
        result = requests.get(url=url, headers=self.header).json()
        return result
    def get_edu_app_captcha(self, phone):
        url = self.url + "/api/biz-fnd/cache/get?key=edu-app-applet:login:phone_captcha:" + str(phone)
        result = requests.get(url=url, headers=self.header).json()
        return result
    def get_edu_c_captcha(self, phone):
        url = self.url + "/api/biz-fnd/cache/get?key=edu-c-applet:login:phone_captcha:" + str(phone)
        result = requests.get(url=url, headers=self.header).json()
        return result

    def get_pwd(self,phone):
        # 000000: web_crm:changePwdSendCaptcha: 19521275178:1823291976877154305
        url = self.url + "/api/biz-fnd/cache/get?key=edu_crm:login:find_phone_captcha:" + str(phone)
        # url = self.url + "/api/biz-fnd/cache/get?key=edu-crm:update:phone:captcha"+ str(phone)
        result = requests.get(url=url, headers=self.header).json()
        return result

    def get_edu_p_captcha(self,phone):
        url = self.url + "/api/biz-fnd/cache/get?key=edu-crm:update:password:captcha:" + str(phone)
        result = requests.get(url=url, headers=self.header).json()
        return result

    def get_bind_captcha(self,phone):
        url = self.url + "/api/biz-fnd/cache/get?key=edu-app-applet:login:bind_phone_captcha:" + str(phone)
        result = requests.get(url=url, headers=self.header).json()
        return result

    # redis登录验证key
    # c端小程序
    # c - applet: login:phone_captcha: 这里拼接手机验号
    # b端小程序
    # login: phone_captcha:这里拼接手机验号
    # m站
    # m - website: phone_captcha:这里拼接手机验号

    def all_main(self,type,phone):
        if type == "c":
            result = self.get_c_captcha(phone)
        elif type == "b":
            result = self.get_b_captcha(phone)
        elif type == "m":
            result = self.get_m_captcha(phone)
        #教培b端验证码
        elif type == 'edu':
            result = self.get_edu_b_captcha(phone)
        #教培c端验证码
        elif type == 'edu_c':
            result = self.get_edu_c_captcha(phone)
        #教培修改密码验证码
        elif type == 'edu_p':
            result = self.get_edu_p_captcha(phone)
        return result



if __name__ == '__main__':
    # res = select_online_captcha().all_main("edu_c",10000000070)

    # res = select_online_captcha().all_main("edu", 11000000060)
    # res = select_online_captcha().all_main("b", 18770813292)
    res = CodeServices().get_edu_app_captcha(10000000105)
    # res = select_online_captcha().get_edu_c_captcha(10000000095)



    print(res)