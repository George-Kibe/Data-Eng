## SSH to linux

ssh -i "ec2-de-mbd-predict-key.pem" ec2-user@ec2-54-217-133-30.eu-west-1.compute.amazonaws.com

# install s3fuse

sudo yum install automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel

git clone https://github.com/s3fs-fuse/s3fs-fuse.git

sudo yum update all

cd s3fs-fuse
./autogen.sh
./configure --prefix=/usr --with-openssl
make
sudo make install

which s3fs

# for configuring your aws credentials access key and secret key

# create a folder and file to write

sudo touch /etc/passwd-s3fs

# write

nano /etc/passwd-s3fs
sudo chmod 640 /etc/passwd-s3fs
sudo chmod 777 /etc/passwd-s3fs
type accesskey:Access_secret_key
ctrl+x

# mounting

sudo s3fs de-mbd-predict-george-wambui-s3-source -o use_cache=/tmp -o allow_other -o uid=1001 -o mp_umask=002 -o multireq_max=5 /home/ec2-user/my-s3-bucket

export PATH="/home/username/miniconda/bin:$PATH"

#!/bin/bash sudo s3fs de-mbd-predict-george-wambui-s3-source -o use_cache=/tmp -o allow_other -o nonempty -o id=$UID -o mp_umask=002 -o multireq_max=5 -o umask=0007 /home/ec2-user/my-s3-bucket python /home/ec2-user/my-s3-bucket/Scripts/python_data_processing_walkthrough.py

# installing anaconda

wget https://repo.continuum.io/archive/Anaconda3-5.3.1-Linux-x86_64.sh
bash Anaconda3-5.3.1-Linux-x86_64.sh

sudo amazon-linux-extras install python3.8
aws configure

### Bash command

#!/bin/bash sudo s3fs de-mbd-predict-george-wambui-s3-source -o use_cache=/tmp -o allow_other -o nonempty -o uid=$UID -o mp_umask=002 -o multireq_max=5 -o umask=0007 /home/ec2-user/my-s3-bucket/Scripts/python_data_processing_walkthrough.py

#!/bin/bash
sudo s3fs de-mbd-predict-george-wambui-s3-source -o use_cache=/tmp -o allow_other -o nonempty -o uid=$UID -o mp_umask=002 -o multireq_max=5 -o umask=0007 /home/ec2-user/my-s3-bucket
python3 /home/ec2-user/my-s3-bucket/Scripts/python_data_processing.py

### SNS Topic ARN

arn:aws:sns:eu-west-1:179792149144:de-mbd-predict-george-wambui-SNS

CREATE TABLE historical_stocks_data (
stock_date VARCHAR ( 56 ),
open_value VARCHAR ( 56 ),
high_value VARCHAR ( 56 ),
low_value VARCHAR ( 56 ),
close_value VARCHAR ( 56 ),
volume_traded VARCHAR ( 56 ),
daily_percent_change VARCHAR ( 56 ),
value_change VARCHAR ( 56 ),
company_name VARCHAR ( 56 ))
