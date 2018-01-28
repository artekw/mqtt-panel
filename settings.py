import os
import sys
import yaml


with open("settings.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def read(section, *argv):
    if section:
        if section == 'settings':
            for idx, value in enumerate(cfg[section][argv[0]]):
                if argv[1] in value:
                    return cfg[section][argv[0]][idx][argv[1]]
        if section == 'feeds':
            return cfg[section]
