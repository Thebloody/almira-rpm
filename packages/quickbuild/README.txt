===============================================================================
almira.rpm.quickbuild
===============================================================================

Overview
--------
PMEase Quickbuild RPM.


Customization
-------------

Run 'bin/server.sh install' this creates link:

creates a link:

    /etc/init.d/quickbuild -> /home/quickbuild/quickbuild/bin/./server.sh

customize server.sh:

 sed -i 's|PIDDIR="."|PIDDIR="/var/run/quickbuild"|g' server.sh
 sed -i 's|#RUN_AS_USER=|RUN_AS_USER=quickbuild|g' server.sh


run migrate.sh --> cannot have symlinks in quickbuild/conf, so we invert the
link: /etc/quickbuild -> quickbuild/conf. This means the configuration is not
saved when uninstalling RPM.



TODO with Puppet:

Added the following line ine wrapper.conf

    wrapper.java.additional.4=-XX:MaxPermSize=256m


Edited hibernate.properties to use MySQL instead of embedded database.

    hibernate.dialect=org.hibernate.dialect.MySQLDialect
    hibernate.connection.driver_class=com.mysql.jdbc.Driver
    hibernate.connection.url=jdbc:mysql://localhost:3306/quickbuild
    hibernate.connection.username=root
    hibernate.connection.password=mysql


Configuration
-------------
http://server:8810/setup

1. Setup Administrator
    Login name: admin
    Login password: admin

2. System Settings
    URL to Access QuickBuild: http://server:8810/
    Global Storage Directory: /home/quickbuild/storage

3. Email Setting
    STMP Host: localhost

Click on root, Settings, Advanced Setting, Edit
    Workspace Directory Setting
        -> Select 'Use Specified workspace directory'
            Path: /home/quickbuild/workspace/${configuration.pathName}
    Save


References
----------
http://wiki.pmease.com/display/QB50/Server+Installation+Guide
http://forum.pmease.com/viewtopic.php?f=1&t=1435