import requests

class Topics(object):
    base_url = "http://39.107.96.138:3000/api/v1"

    def __init__(self,url):
        self.url = self.base_url+url
    
    def get_index_topics(self,limit=20,tab=None):
        params = {"limit":limit,"tab":tab}
        r = requests.get(self.url,params=params)
        return  r
    
    def post_create_topic(self,token,title,tab,content):
        params = {
            "accesstoken":token,
            "title":title,
            "tab":tab,
            "content":content
        }
        r = requests.post(self.url,data=params)
        return r
    
    def post_update_topic(self,token,topic_id,title,tab,content):
        params = {
            "accesstoken":token,
            "topic_id":topic_id,
            "title":title,
            "tab":tab,
            "content":content
        }
        r = requests.post(self.url,data=params)
        return r

