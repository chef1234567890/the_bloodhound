#!/usr/bin/env python
import csv

class Diff:
    def diff():
        previous_cache = './tmp/previous.cache'
        recent_cache = './tmp/recent.cache'
        increment_cache = './tmp/increment.cache'
        decrement_cache = './tmp/decrement.cache'

        previous = list(csv.reader(open(previous_cache)))
        recent = list(csv.reader(open(recent_cache)))

        incremental = list(set(recent[0]) - set(previous[0]))
        decremental = list(set(previous[0]) - set(recent[0]))

        increment = csv.writer(open(increment_cache, 'w'))
        increment.writerow(incremental)
        decrement = csv.writer(open(decrement_cache, 'w'))
        decrement.writerow(decremental)
