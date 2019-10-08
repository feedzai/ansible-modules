#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# ------------------------------------------------------------------------------------------------------
#
#  Complements
#  https://github.com/ansible/ansible/blob/devel/lib/ansible/modules/cloud/google/gcp_storage_object.py
#
#  The mentioned file has trouble regarding reading non-text (binary for example) files
#  Besides that, it creates an unnecessary file as we want to simply store contents in memory / parameter

# In https://docs.ansible.com/ansible/devel/dev_guide/testing/sanity/metaclass-boilerplate.html
from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1' }

DOCUMENTATION = '''
---
module: gcp_storage_value
description:
- Get contents from a file in a GCS bucket
short_description: Reads contents from GCS file
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  path:
    description:
    - file path inside GCS bucket.
    required: true
    type: path
  bucket:
    description:
    - The name of the bucket.
    required: true
    type: str
'''

EXAMPLES = '''
- name: get message
  gcp_storage_value:
    bucket: ansible-bucket
    path: hello-world.txt
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
  register: hello_world
'''

RETURN = '''
value:
  description:
  - File contents
  returned: success
  type: str
'''

from ansible.module_utils.gcp_utils import GcpSession, GcpModule
import json

def main():
    module = GcpModule(
        argument_spec=dict(
            path=dict(type='path'),
            bucket=dict(type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/devstorage.full_control']

    session = GcpSession(module, 'storage')

    remote_object = session.get("https://www.googleapis.com/storage/v1/b/{bucket}/o/{path}".format(**module.params))
    if remote_object.status_code == 404 or remote_object.status_code == 204:
        module.fail_json(msg="File not found")

    data = session.get(remote_object.json()['mediaLink'])
    module.exit_json(changed=False, value=data.content)

if __name__ == '__main__':
    main()
