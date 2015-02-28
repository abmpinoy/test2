#!/usr/bin/env python

import sys
  
import duo_client
  
argv_iter = iter(sys.argv[1:])
def get_next_arg(prompt):
    try:
        return argv_iter.next()
    except StopIteration:
        return raw_input(prompt)
  
# You can find this information in the integrations section
# where you signed up for Duo.
verify_api = duo_client.Verify(
    ikey='DILMTZEB12GJ4OND3I5W',
    skey='XefQ7cT8L9bQ4yk3VoBPwuprI96hnv0vtEe4NeHl',
    host='api-4a1b0eeb.duosecurity.com',
)
  
# Please use your valid telephone number with country code, area
# code, and 7 digit number. For example: PHONE = '+1-313-555-5555'
PHONE_NUMBER = get_next_arg('phone number ("+1-313-555-5555"): ')
  
(pin, txid) = verify_api.call(phone=PHONE_NUMBER)
print 'Sent PIN: %s' % pin
state = ''
while state != 'ended':
    status_res = verify_api.status(txid=txid)
    print status_res['event'], 'event:', status_res['info']
    state = status_res['state']
  
