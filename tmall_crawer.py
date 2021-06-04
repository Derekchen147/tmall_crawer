import requests
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import time
import json

all = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
           "cookie": 'hng=CN%7Czh-CN%7CCNY%7C156; lid=t_1501259612036_0833; enc=jdMsCn4vEQ2QSmHe%2B0guz%2FvSPrhVublI5%2FAzvcclJddTCVKEoKIFIzqre0mfe7wgXLXb0J3mKyboJsvSzjG6dg%3D%3D; cna=ZZEfGQB6Yy4CATohq0p3woxm; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; t=04d4f884888c66d88fa9e62e19ef344d; tracknick=t_1501259612036_0833; lgc=t_1501259612036_0833; _tb_token_=ebb1734177a3f; cookie2=19f19b059d92cb80d38e60ab1ebad8a6; xlly_s=1; res=scroll%3A1349*5510-client%3A1349*657-offset%3A1349*5510-screen%3A1366*768; pnm_cku822=098%23E1hvvQvUvbpvjQCkvvvvvjiWPFqwgjnHn2SU1j3mPmPZ0jrmRLMvsj3UR2qwtjIRvpvhvv2MMq9Cvm9vvvvvphvvvvvv9krvpv3Vvvmm86Cv2vvvvUUdphvUOQvv9krvpv3FkvhvC99vvOCgL49Cvv9vvUmGDo%2BxSp9CvhQUanWvCsdhzb2XrqpyCW2%2BFO7t%2BeCBtRFEDLuTWDAvD7zhe8tYcWmQiNp4V5Db%2BneYiLUpwhKn3w0xhCDQo%2Bex6aZtn0vHfwLvaXTAvvhvC9vhvvCvp29Cvvpvvvvvi9hvCvvv9UU%3D; dnk=t_1501259612036_0833; uc1=pas=0&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie14=Uoe2z%2BTD1e3q6A%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dCuw77pEN9jNcyK0k%3D&nk2=F6k3HSxsRhd3Ek9fukdyDJkStpw%3D&id2=UUGjNTrI%2FW8Rgw%3D%3D; _l_g_=Ug%3D%3D; uc4=id4=0%40U2OU%2BtEnsmv3otYne2nKL05qBc8l&nk4=0%40FbMocxnLmepXoquRUsQEFeFcZOKS67TdA8lmVykRzQ%3D%3D; unb=2917284038; cookie1=BxNZ2nQJwYfpY8F6DmtSCx%2FFXFxliOuLP2wO4iWKtg8%3D; login=true; cookie17=UUGjNTrI%2FW8Rgw%3D%3D; _nk_=t_1501259612036_0833; sgcookie=E100zTVHhRvL2omggP00Sv8fkJfGri9FrlvtObww2HZUIsq%2BnjaluMtAP4MdQ6vsYtVIuZsAjd%2F0qTMYcKWIMBIOGg%3D%3D; sg=381; csg=36c97a8b; cq=ccp%3D0; _uab_collina=162279298655742712329799; csa=9907140493_0_30.832626.120.916215_0_0_0; _m_h5_tk=c0436bc5731e0b66165fb9730d0b65be_1622805712470; _m_h5_tk_enc=3b69f838a1a1344b0b53ed188886d370; sm4=330421; x5sec=7b22746d616c6c7365617263683b32223a223665316635346431643037383865643261613765313562323235346562643964434a7a6d35345547454b36347776794f3334433138414561444449354d5463794f4451774d7a67374d6a446a316f536d2b662f2f2f2f3842227d; tfstk=c255BvxZv0m7Ay2EaaaqUFjVvnAlZkhXojxVPOpNNeJsyGb5itcwfQ4wPmGvBE1..; l=eBaT90FRjkqfTbMEBOfCnurza7797IRYSuPzaNbMiOCPOH5yca0VW6___xL2CnGVh6oWR3RSn5QMBeYBqCmdv7aStBALuPkmn; isg=BFpa_zu07uxz4mJW5mB7sED4qwB8i95l6Nl1kWTTEu2E1_oRTBiAdecto6PLAlb9'
           }


def get_html(url):
    try:
        response = requests.get(url, allow_redirects=True, headers=headers)
        if response.status_code == 200:
            return response.text
            print('200')
        if response.status_code == 302:
            print('302')
        if response.status_code == 404:
            print('404')

    except ConnectionError:
        return get_html(url)


def get_index(base_url):
    url = base_url
    html = get_html(url)
    doc = pq(html)
    title = doc('.product-title a').items()
    wd_sum = doc('.item-sum strong').items()
    price = doc('.item-price strong').items()
    href = doc('.product-title a').items()
    flag = True

    for o, i, e, j in zip(title, wd_sum, price, href):
        dic1 = {}
        dic1['title'] = o.text(),
        dic1['wd_sum'] = i.text(),
        dic1['price'] = e.text(),
        dic1['href'] = j.attr('href')
        all.append(dic1)
        flag = False

    return flag


def main():
    # url = f'https://list.tmall.com/search_product.htm?spm=a3204.23072412.1996500281.55.e2d75885UvCxKf&s=0&user_id=725677994&cat=51294012&area_code=330100&active=1&style=g&acm=lb-zebra-26901-350672.1003.4.467893&sort=s&search_condition=23&scm=1003.4.lb-zebra-26901-350672.OTHER_14440830747347_467893&n=0'
    #         'https://list.tmall.com/search_product.htm?spm=a3204.23072412.1996500281.56.e2d75885UvCxKf&s=0&user_id=725677994&area_code=330100&cat=50514010&active=1&style=g&acm=lb-zebra-26901-329720.1003.4.467882&search_condition=1&sort=s&scm=1003.4.lb-zebra-26901-329720.OTHER_14440833867602_467882&n=40'
    # print('正在爬虫第0页请稍后…………')
    # get_index(url)
    # time.sleep(20)
    for i in range(1,37):
        url = f'https://list.tmall.com/search_product.htm?totalPage=36&q=&sort=s&user_id=725677994%2C2136152958&style=g&brand=&prop=&start_price=&end_price=&chaoshi_imported=&cat=51278010&jumpto={i}'
        print('正在爬虫第{}页请稍后…………'.format(i))
        flag = get_index(url)
        k = 0
        while flag and k<10:
            k += 1
            print('被拦截')
            new_cookie = input('输入新cookie： ')
            headers["cookie"] = str(new_cookie)
            flag = get_index(url)
        if k > 9:
            with open('./天猫数据/饼干_曲奇.json', 'w', encoding='utf8') as f:
                json.dump(all, f, ensure_ascii=False)
            exit()
        time.sleep(40)
    for i in range(1,12):
        url = f'https://list.tmall.com/search_product.htm?totalPage=11&q=&sort=s&user_id=725677994%2C2136152958&style=g&brand=&prop=&start_price=&end_price=&chaoshi_imported=&cat=51286011&jumpto={i}'
        print('正在爬虫第{}页请稍后…………'.format(i))
        flag = get_index(url)
        k = 0
        while flag and k<10:
            k += 1
            print('被拦截')
            new_cookie = input('输入新cookie： ')
            headers["cookie"] = str(new_cookie)
            flag = get_index(url)
        if k > 9:
            with open('./天猫数据/饼干_曲奇.json', 'w', encoding='utf8') as f:
                json.dump(all, f, ensure_ascii=False)
            exit()
        time.sleep(40)


if __name__ == '__main__':
    main()

    with open('./天猫数据/饼干_曲奇.json', 'w', encoding='utf8') as f:
        json.dump(all,f, ensure_ascii=False)