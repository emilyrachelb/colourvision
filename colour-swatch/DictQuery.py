#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Filename:       DictQuery.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 14, 2018
#   Description:    JSON Dictionary Navigation

class Query(dict):
    def get(self, path, default=None):
        keys = path.split('/')
        val = None

        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [v.get(key, default) if v else None for v in val]
                else:
                    val = val.get(key, default)
            else:
                val = dict.get(self, key, default)

            if not val:
                break

        return val