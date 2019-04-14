import pytest
from all_api.topics import Topics


@pytest.mark.parametrize("limit,tab", [("1", "ask"), ("10", "share"), ("5", "job")])
def test_index_page(limit,tab):
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
