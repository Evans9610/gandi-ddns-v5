#coding=utf8

import json
import requests


class Gandi():
    def __init__(self, api_key, domain):
        self.api_key = api_key
        self.domain = domain
        self.headers = {'X-Api-Key': self.api_key,
                        'Content-Type': 'application/json'}
        self.api_url = 'https://dns.api.gandi.net/api/v5'

    def update_A(self, ip):
        url = '{}/domains/{}/records/%40/A'.format(self.api_url, self.domain)
        data = {'rrset_ttl': 10800,
                'rrset_values': ip}
        res = requests.put(url, headers=self.headers, data=json.dumps(data),
                           verify=False)
        return json.loads(res.content)['message']

    def get_uuid(self):
        url = '{}/domains/{}'.format(self.api_url, self.domain)
        response = requests.get(url, headers=self.headers, verify=False)
        uuid = json.loads(response.content)
        return uuid['zone_uuid']

    def get_all_records(self):
        url = '{}/domains/{}/records'.format(self.api_url, self.domain)
        response = requests.get(url, headers=self.headers)
        return json.loads(response.content)


def get_ip():
    url = 'http://outian.org/'
    response = requests.get(url)
    ip = response.content.split('\n')[0].replace('<br />', '')
    return ip

def main():
    api_key = ''
    domain = ''
    g = Gandi(api_key, domain)
    print g.update_A(['{}'.format(get_ip())])

if __name__ == "__main__":
    main()
