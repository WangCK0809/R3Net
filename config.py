# coding: utf-8
import os

datasets_root = '/mnt/nfs/scratch1/dghose/Kaist/kaist_train/'
datasets_root = '/mnt/nfs/scratch1/dghose/Kaist_test_30X/kaist_30X_test/'

kaist_path = datasets_root

# For each dataset, I put images and masks together
msra10k_path = os.path.join(datasets_root, 'msra10k')
ecssd_path = os.path.join(datasets_root, 'ecssd')
hkuis_path = os.path.join(datasets_root, 'hkuis')
pascals_path = os.path.join(datasets_root, 'pascals')
dutomron_path = os.path.join(datasets_root, 'dutomron')
sod_path = os.path.join(datasets_root, 'sod')
