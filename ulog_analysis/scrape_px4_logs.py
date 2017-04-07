"""Downloads px4 log files from website."""

import datetime
import json
import os
import re
import time
import urllib.request

from bs4 import BeautifulSoup


def get_log_data(log_dir):
    """Download log data from px4 webpage."""

    # create directory
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    # get log data
    page = urllib.request.urlopen("http://review.px4.io/browse")
    soup = BeautifulSoup(page.read(), 'html.parser')
    log_data = {}
    for row in soup.find_all('tr'):
        entries = []
        for column in row.find_all('td'):
            entries += [column]

        try:
            uuid = re.match('.*log=(.*)', entries[1].find(
                'a', href=True)['href']).group(1)
        except IndexError:
            continue

        try:
            ts = time.strptime(entries[7].getText(), '%H:%M:%S')
            sec = datetime.timedelta(
                hours=ts.tm_hour,
                minutes=ts.tm_min,
                seconds=ts.tm_sec).total_seconds()
        except Exception as exc:
            print(uuid, exc)
            continue

        log_data[uuid] = {
            'date': entries[1].getText(),
            'num': entries[0].getText(),
            'uuid': uuid,
            'description': entries[2].getText(),
            'type': entries[3].getText(),
            'airframe': entries[4].getText(),
            'hardware': entries[5].getText(),
            'software': entries[6].getText(),
            'duration': sec,
            'rating': entries[8].getText(),
            'errors': int(entries[9].getText()),
        }

    log_data_file = os.path.join(log_dir, 'log_data.json')
    with open(log_data_file, 'w') as fid:
        fid.write(json.dumps(log_data, indent=2, sort_keys=True))
    print('found ', len(log_data.keys()), ' logs')

    # download log files and save to disk
    for log in sorted(log_data.keys()):
        log_path = os.path.join('logs', '{:s}.ulg'.format(log))
        if os.path.exists(log_path):
            pass
            # print('already have log', log)
        else:
            print('downloading log', log)
            urllib.request.urlretrieve(
                'http://review.px4.io/download?log={:s}'.format(log),
                log_path)


if __name__ == "__main__":
    get_log_data('logs')
