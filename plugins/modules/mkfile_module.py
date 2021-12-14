#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: mkfile_module

short_description: module for create file with content

version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: This is path to file.
        required: true
        type: str
    content:
        description: content for write to file
        required: false
        type: str
        default: Default content

author:
    - Max Nelipin (@MaxNelipin)
'''

EXAMPLES = r'''
# pass in a message and have changed true
- name: Test create
  my_namespace.my_collection.mkfile_module:
    path: "\path\to\file.txt"
    content: "some content"

'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.

message:
    description: status oparation.
    type: str
    returned: always
    sample: 'file created'
'''

from ansible.module_utils.basic import AnsibleModule
from pathlib import Path


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default="Default content")
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    my_file = Path(module.params['path'])

    if my_file.is_dir():
        result['changed'] = False
        result['failed'] = True
        result['message'] = "Path must be a file"
    elif my_file.exists():
        some_file_read = open(module.params['path'], 'r')
        if some_file_read.read() == module.params['content']:
            result['changed'] = False
            result['message'] = "Content equal"
        else:
            some_file_read.close()
            some_file_write = open(module.params['path'], 'w')
            some_file_write.write(module.params['content'])
            result['changed'] = True
            result['message'] = "file rewrite"
            some_file_write.close()
    else:
        with open(module.params['path'], 'w') as some_file:
            some_file.write(module.params['content'])
            some_file.close()
        result['changed'] = True
        result['message'] = "new file created"

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
