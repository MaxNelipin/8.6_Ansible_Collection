# Ansible Collection - maxnelipin.yandex_cloud_elk

Коллекция с ролью для тетсирования модуля создания файла в директории.

Role Variables
--------------
| Variable name | Default | Description |
|-----------------------|----------|-------------------------|
| path | "/home/maxn/4.txt"| путь к фалу |
| content | "role content default" | строка, записываемая в файл |

Example Playbook
----------------
```yaml
- hosts: localhost
  tasks:
  - name: run mkfile_module
    import_role:
      name: maxnelipin.yandex_cloud_elk.ynd_cloud_elk
    vars:
      path: "/home/maxn/test.txt"
      content: "From playbook and collection"
```

License
-------

BSD

Author Information
------------------

MaxNelipin