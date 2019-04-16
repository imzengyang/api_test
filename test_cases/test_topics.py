import pytest
from all_api.topics import Topics
import tools


default_token = "3333a0fb-6dd8-439e-813b-2c3a5213a154"
create_data = tools.get_data()


@pytest.mark.parametrize("limit,tab", [("1", "ask"), ("10", "share"), ("5", "job")])
def test_index_page(limit,tab):
    """
    获取主题首页帖子api 测试
    测试不同参数返回不同服务器数据
    """
    url = "/topics"
    topics = Topics(url)
    # assert_limit=1
    # tab = 'ask'
    res = topics.get_index_topics(limit,tab)
    r = res.json()
    assert len(r['data']) == int(limit)
    # r['data'][0]['tab'] == 'ask'
    assert res.status_code == 200
    all_data = r['data']
    for data in all_data:
        assert data['tab'] == tab
    
@pytest.mark.parametrize("tab,title,content", create_data)
def test_post_create_topic(tab,title,content,token=default_token):
    url = '/topics'
    topic = Topics(url)
    res = topic.post_create_topic(token,title,tab,content)
    assert res.status_code == 200
    r = res.json()
    assert r['success'] == True


# def test_update_topic():
#     t1 = Topics('/topics')
#     t1.post_create_topic('')