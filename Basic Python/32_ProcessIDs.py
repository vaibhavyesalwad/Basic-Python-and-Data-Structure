"""Program to get the effective group id, effective user id, real group id, a list of supplemental group ids
associated with the current process"""
import os                               # using os module
print('For current process')
print(f'Effective Group id:{os.getegid()}')     # gets effective group id & it can be set by os.setegid(new_id)
print(f'Effective User id:{os.geteuid()}')      # gets effective user id & it can be set by os.seteuid(new_id)
print(f'Real Group id:P{os.getgid()}')         # gets real group id & can be set by os.setgid(new_id)
print(f'Supplemental group ids: {os.getgroups()}')  # supplementary group ids for current process

