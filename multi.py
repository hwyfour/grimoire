#!/usr/bin/env python

'''

A script to scrape the internet in parallel

'''

import sys
import time
import signal

from Queue import Queue
from threading import Thread, Lock

concurrent = 10

class Worker(Thread):
    screen_mutex = Lock()

    def __init__(self, queue, thread_id):
        super(Worker, self).__init__()
        self.queue = queue
        self.id = thread_id

    def console(self, msg):
        Worker.screen_mutex.acquire()
        print msg
        Worker.screen_mutex.release()

    def run(self):
        while True:
            number, url = self.queue.get()
            self.console('%s - Processing %s' % (self.id, url))
            time.sleep(4)
            self.queue.task_done()


def killed(message='', agent=''):
    print 'killed'

def main(list):
    queue = Queue()

    for _ in range(concurrent):
        worker = Worker(queue, _)
        worker.daemon = True
        worker.start()

    # request each url in the list
    with open(list, 'r') as infile:

        count = 0

        for line in infile:
            stripped = line.strip()

            if stripped == '':
                return

            count += 1

            queue.put([count, stripped])

        queue.join()


if __name__ == "__main__":

    signal.signal(signal.SIGTERM, killed)

    args = sys.argv

    if len(args) == 2:
        main(args[1])
    else:
        print 'Usage: %s <plaintext file w/ URL on each line>' % args[0]
