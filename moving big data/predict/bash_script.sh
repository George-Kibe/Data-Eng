#!/bin/bash 
sudo s3fs de-mbd-predict-george-wambui-s3-source -o use_cache=/tmp -o allow_other -o nonempty -o uid=$UID -o mp_umask=002 -o multireq_max=5 -o umask=0007 /home/ec2-user/my-s3-bucket
python3 /home/ec2-user/my-s3-bucket/Scripts/python_data_processing.py