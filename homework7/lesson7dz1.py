
import os

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}  # we can save .json
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            if os.path.exists(cur_dir):
                print(cur_dir, 'существует')
            else:
                os.makedirs(cur_dir)