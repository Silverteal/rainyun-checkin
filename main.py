#ZYGLQexplorer/RainYun-Checkin

import requests
import json

"""请求IPIP并原样返回"""
def get_base_ip(*,log_func = print):
    log_func('获取网络状态...')
    return requests.request("GET", "https://myip.ipip.net/").text.strip()

"""请求用户信息"""
def get_user_info(api_key,*,entry_point="https://api.v2.rainyun.com/user/",log_func = print):
    headers = {
    'X-Api-Key': api_key
    }
    payload={}

    
    log_func('获取用户信息...')
    response = requests.request("GET", entry_point, headers=headers, data=payload).json()

    return response

"""签到"""
def checkin(api_key,*,entry_point='https://api.v2.rainyun.com/user/reward/tasks',log_func = print):
    headers = {
        'content-type':"application/json",
        'X-Api-Key':api_key
        }
    payload = {
        "task_name" : '每日签到'
        }

    log_func('发送每日签到...')
    response = requests.request("POST", entry_point, headers=headers, data = json.dumps(payload)).json()

    return response
    

#初始化全局变量
api_keys = [] #placeholder
api_key = '' #placeholder
succeed = 0
duplicate = 0
failed = 0

#获取机密
with open("arguments.txt") as f:
   api_keys = f.read().strip().split(',')

assert api_keys

print('==============================')
print(get_base_ip())

for i,api_key in enumerate(api_keys,start=1):
    # api_key = api_keys[0]
    print('==============================')
    print(f'任务第 {i} 项，共 {len(api_keys)} 项')
    print(f'APIKEY的长度是 {len(api_key)}')
    info_before = get_user_info(api_key)
    
    points_before = info_before['data']['Points']
    ID = info_before['data']['ID']
    name = info_before['data']['Name']

    print(f'ID长度: {len(str(ID))}')
    print(f'用户名: {name[0]}***{name[-1]}')
    print(f'签到前积分: {points_before}')

    checkin_response = checkin(api_key)

    info_after =get_user_info(api_key)
    points_after = info_after['data']['Points']
    print(f'签到后积分: {points_after}')
    if points_after > points_before :
        print(f'返回值: {checkin_response}')
        print('鉴定为签到成功')
        succeed += 1
    elif checkin_response['code'] == 30011:
        print(f'返回值: {checkin_response}')
        print('鉴定为签到重复')
        duplicate += 1
    else:
        print(f'返回值: {checkin_response}')
        print('鉴定为签到失败')
        failed += 1
    print('==============================')

print("全部任务已完成")
print(f"成功{succeed}个，重复签到{duplicate}个，失败{failed}个")
assert succeed or duplicate
