#!/usr/bin/env python

from fabric.api import *

hostlist = [ line.strip('\n') for line in open('hostlist.txt') ]

env.roledefs = {
     'loadbalancer': hostlist
     }

@roles('loadbalancer')
@parallel
def install_keepalived():
    with settings(warn_only=True):
	test = run('rpm -qa wget')
        if test == '':
            run('yum install wget -y')
    with cd('/opt/'):
    	run('wget http://www.keepalived.org/software/keepalived-1.2.15.tar.gz')
	run('tar xzvf ./keepalived-1.2.15.tar.gz')
	with cd('./keepalived-1.2.15'):
	    run('yum -y install kernel-headers kernel-devel gcc popt-devel.x86_64 openssl-devel.x86_64 make ipvsadm')
	    run('./configure --with-kernel-dir=/lib/modules/$(uname -r)/build')
	    run('make && make install')

@roles('loadbalancer')
#@parallel
def setup_links():
    with cd('/etc/sysconfig'):
	run('ln -s /usr/local/etc/sysconfig/keepalived .')
    with cd('/etc/init.d/'):
	run('ln -s /usr/local/etc/rc.d/init.d/keepalived .')
    run('ln -s /usr/local/etc/keepalived/ /etc/keepalived')
    run('sed -i \'s:daemon keepalived:daemon /usr/local/sbin/keepalived:\' /usr/local/etc/rc.d/init.d/keepalived')
    run('chkconfig keepalived on')

