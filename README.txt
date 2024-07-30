TP-Link RE315 API Client.

The RE315 is trash, even if in close range, the 5GHz channel will eventually lost connection with the root AP (I have 2 RE315 and they face the same problem).
TP-Link support is ok, but didn't solve my problem.
I suppose it was configured to lock the BSSID or maybe it have something to do with MU-MIMO.
Every time, I have to login to web's quick setup section, retype password to be able to use the 5GHz channel (which is a pain in the ass for me).

I'm not going to implement the full API client, so the code in this repo is simply the implementation of the RE315's E2E encryption.

Tested on:
    Firmware Version: 1.0.30 Build 230919 Rel.52342n (6985)
    Hardware Version: RE315 1.0