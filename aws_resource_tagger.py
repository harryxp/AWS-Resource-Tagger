import boto3

def main():
    client = boto3.client('resourcegroupstaggingapi')

    response = client.get_resources(
        PaginationToken='',
        TagFilters=[
            {
                'Key': 'app',   # TODO change me
                'Values': [
                    'old_app',  # TODO change me
                ]
            },
        ],
        ResourcesPerPage=100,
        ResourceTypeFilters=[
            'ec2:instance',     # TODO MAYBE change me
        ],
        IncludeComplianceDetails=False,
    )

    resource_list = response['ResourceTagMappingList']

    for rc in resource_list:
        resource_arn = rc['ResourceARN']
        print(f'Tagging resource {resource_arn}')

        client.tag_resources(
            ResourceARNList=[
                resource_arn
            ],
            Tags={
                'ec2_arn': resource_arn     # TODO MAYBE change me
            }
        )

if __name__ == '__main__':
    main()
