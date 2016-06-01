# This file is to define connection to device via Expect como funcion:
#
# ConectaEquipo(<ip>,<script>)
#
#


def ConectaEquipo(ip_address,scripts)
    # Verificamos si es alcanzable

    import ping, socket
    try:
        ping.verbose_ping(ip_address, count=3)
        except socket.error, e:
            error = "No se pudo alcanzar la dirección IP: ", e

    # Conectamos a la DB y obtenemos usuario y contraseña correspondiente a la ip_address
    import MySQLdb

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="john",  # your username
                     passwd="megajonhy",  # your password
                     db="jonhydb")  # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM YOUR_TABLE_NAME")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print
        row[0]

    db.close()

    # Conectamos via expect y ejecutamos el script
    import pexpect

    ssh_newkey = 'Are you sure you want to continue connecting'
    # my ssh command line
    p=pexpect.spawn('ssh mysurface@192.168.1.105 uname -a')

    i=p.expect([ssh_newkey,'password:',pexpect.EOF])
    if i==0:
        print "I say yes"
        p.sendline('yes')
        i=p.expect([ssh_newkey,'password:',pexpect.EOF])
    if i==1:
        print "I give password",
        p.sendline("mypassword")
        p.expect(pexpect.EOF)
    elif i==2:
        print "I either got key or connection timeout"
        pass
    print p.before # print out the result

    # Manejo de errores

    # Return


