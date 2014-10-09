#!/usr/bin/env python

maxsize=10 #maximale erlaubte anzahl an servern

#f=open('template.yaml','r')

#input anzahl server
while True:
    try:
        size=int(input('Wieviele Webserver sollen erstellen werden? '))
        if size <1:
            print("ernsthaft? ein positiver Wert ist erforderlich")
        elif size >maxsize:
            print("aus Gründen maximal %d" %(maxsize))
        else:
            print(size)
            break
    except ValueError:
        if not size:
            raise ValueError('empty string')
        else:
            raise ValueError('not int')

#input servername
name=input('Wie sollen die Server benannt werden? ')
if not name:
    name='WebServer'
    print('Kein Input, wähle default')

print('Erstelle %d Server mit dem Name %s' %(size,name))

with open('template1.yaml', 'r') as file1:
    part1=file1.read()
    file1.close()

with open('template2.yaml', 'r') as file2:
    part2=file2.read()
    file2.close()

with open('template3.yaml', 'r') as file3:
    part3=file3.read()
    file3.close()

with open('test.yaml', 'r+') as f:
    f.write(part1)
    #generate port entries
    for i in range(1,size+1):
        if i<10:
            j='0%s'%(i)
        else:
            j=str(i)
        ports=' my_port%s:\n  type: OS::Neutron::Port\n  properties:\n   admin_state_up: true\n   name: Port%s\n   network_id: { get_resource: my_first_network }\n   fixed_ips: [{ "subnet_id": { get_resource: my_first_subnet }, "ip_address": { get_param: gateway_address } }]\n   security_groups: [ { get_resource: my_router_security_group } ]\n\n'%(j, j)
        f.write(ports)
    f.write(part2)
    #generate server entries
    for i in range(1,size+1):
        if i<10:
            j='0%s'%(i)
        else:
            j=str(i)
        server=' my_server%s:\n  type: OS::Nova::Server\n  properties:\n   name: %s%s\n   key_name: { get_param: keypair_name }\n   flavor: { get_param: machine_flavor }\n   image: { get_param: image_id }\n   networks: [{ "port": { get_resource: my_port%s }, "network": { get_resource: my_first_network }}]\n   user_data: |\n    #!/bin/bash\n    ping -c 4 141.20.9.17\n\n'%(j, name, j,j)
        f.write(server)
    f.write(part3)
    #generate output
    for i in range(1,size+1):
        if i<10:
            j='0%s'%(i)
        output=' Server%s:\n  value: { get_attr: [ my_server%s, show ] }\n'%(j,j)
        f.write(output)
    f.write(' Port4:\n  value: { get_attr: [ my_port4, show ] }\n')
    f.close()


