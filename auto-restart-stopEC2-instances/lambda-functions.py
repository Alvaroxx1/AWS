import boto3


def lambda_handler(event, context):\
    
    # Create EC2 Client
    ec2 = boto3.resource('ec2')

    for instance in ec2.instances.all():
        # print(instance.id, instance.state)

        state = instance.state['Name']
        if state == 'stopped':

            try:
                instance.start()
            except:
                print('Something went wrong starting instance ' + instance.id)