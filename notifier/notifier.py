import requests

__author__ = 'weiwu'


def notify(push_token, title=None, push_body=None, iden=None):
    if push_token is None:
        return
    if push_body is None:
        push_body = ''
    if title is None:
        title = 'Message from Push Notifier'

    if not push_token.starts_with('Bearer'):
        push_token = 'Bearer {t}'.format(t=push_token.strip())
    data = {
        'type': 'note',
        'title': title,
        'body': push_body
    }
    if iden is not None:
        data['target_device_iden'] = iden
    return requests.post('https://api.pushbullet.com/v2/pushes', data=data, headers={'Authorization': push_token})
