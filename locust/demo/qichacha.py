from locust import HttpLocust,task,TaskSet
import random

class Qichacha(TaskSet):

    @task
    def search(self):
        payload = ['探迹','小米','华为','洗衣粉','中通','众泰','保险','电影','连云港市前进洗衣粉有限公司','广东省徐闻洗衣粉厂']

        url = '/search'
        data={'key':random.choice(payload)}
        header={
            'referer':'https://www.qichacha.com',
        }
        req=self.client.get(url=url,params=data,headers=header)
        if req.status_code == 200:
            print('success')
        else:
            print('failure')

class WebsitUser(HttpLocust):
    task_set = Qichacha
    max_wait = 5000
    min_wait = 3000

if __name__ == '__main__':
    import os
    os.system('locust -f qichacha.py --host=https://www.qichacha.com --no-web -c 20 -r 5 -t 3m')