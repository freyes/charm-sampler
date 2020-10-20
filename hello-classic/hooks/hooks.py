#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.join(os.environ['CHARM_DIR'], 'lib'))

from charmhelpers.core import (
    hookenv,
    host,
)

from start import start

hooks = hookenv.Hooks()
log = hookenv.log

SERVICE = 'hello-classic'

@hooks.hook('install')
def install():
    log('Installing hello-classic')


@hooks.hook('start')
def start():
    host.service_restart(SERVICE) or host.service_start(SERVICE)


@hooks.hook('stop')
def stop():
    host.service_stop(SERVICE)


@hooks.hook('upgrade-charm')
def upgrade_charm():
    log('Upgrading hello-classic')


@hooks.hook('cluster-relation-changed')
def cluster_relation_changed():
    log('Running cluster-relation-changed')


@hooks.hook('config-changed')
def config_changed():
    config = hookenv.config()

    for key in config:
        if config.changed(key):
            log("config['{}'] changed from {} to {}".format(
                key, config.previous(key), config[key]))

    config.save()
    start()


if __name__ == "__main__":
    # execute a hook based on the name the program is called by
    hooks.execute(sys.argv)
