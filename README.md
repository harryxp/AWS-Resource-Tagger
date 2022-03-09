# AWS-Resource-Tagger

A simple Python script that grabs AWS resources filtered by tags and resource types, then attach tags to these resources.

```
git clone https://github.com/harryxp/AWSResourceTagger.git
cd AWSResourceTagger/
python3 -m venv .venv
source .venv/bin/activate
pip install boto3
python3 aws_resource_tagger.py
```
