from datetime import date, timezone,datetime


def get_weekday_and_time():
    return datetime.today().strftime('Posted %a %d. %b at %H:%M')


def create_new_post(post, day=get_weekday_and_time()):
    copy_psot = post.copy()
    copy_psot['create_of_weekday'] = day
    return copy_psot


initial_post = {
    'id': 333,
    'User': 'Bazhen'
}

res = post_with_day = create_new_post(initial_post)

print(res)
