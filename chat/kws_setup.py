import os
import shutil
import sys
import secrets


def setup():
    home = os.path.expanduser("~")
    target_dir = os.path.join(home, "KWS")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Move all .py files to the target directory
    for fname in os.listdir(current_dir):
        if fname.endswith('.py'):
            src = os.path.join(current_dir, fname)
            dst = os.path.join(target_dir, fname)
            if src != dst:
                shutil.copy2(src, dst)

    # Create data files
    auth_file = os.path.join(target_dir, 'auth.key')
    config_file = os.path.join(target_dir, 'config.cfk')
    contacts_file = os.path.join(target_dir, 'contacts.cdf')
    data_file = os.path.join(target_dir, 'datatrans.ksys')

    if not os.path.exists(auth_file):
        with open(auth_file, 'w') as f:
            f.write(secrets.token_hex(16))

    for fpath in (config_file, contacts_file, data_file):
        if not os.path.exists(fpath):
            open(fpath, 'w').close()

    print('Installation Done, Need to restart the Script.')

if __name__ == '__main__':
    setup()
