from task2_post import new_post, my_descr


def test_step1(get_token, description):
    new_post(get_token)
    assert description in my_descr(get_token)