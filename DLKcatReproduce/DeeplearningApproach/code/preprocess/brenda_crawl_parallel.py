from tools.decorator import timetry
from tools.tool import response_to_txt
import requests
@timetry
def crawl(ecNumber):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
    # 'cookie': 'AWSUSER_ID=awsuser_id1722646144802r8854; _pk_id.23.153d=268dc7d3fb1c3c1d.1722646151.; brenda-cookie-allowed=1; PHPSESSID=iolvbrtd1g00co2qjvgj4rbg4r; SERVERID=brenda-1; _pk_ref.23.153d=%5B%22%22%2C%22%22%2C1727919051%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DS8yIj0qNYtvSpfZwAQQ2jYYCiheauvgCcCpLYzygRpuPr1xihjOjm6JOgGathy2O%26wd%3D%26eqid%3Db222fb1a034053590000000566fd202f%22%5D; _pk_ses.23.153d=1',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}
    params= {'ecno': ecNumber,}
    print(params)
    response=requests.get('https://www.brenda-enzymes.org/enzyme.php', params=params, headers=headers)
    output_path='./Data/database/brenda_raw/KCAT/'
    file_name = output_path+'EC' + ecNumber+ '_KCAT' +'.txt'
    response_to_txt(file_name,response)

    return response

if __name__=='__main__':
    response=crawl('1.1.1.1')
    print(response.status_code)