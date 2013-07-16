===============================================================================
almira-rpm
===============================================================================

Overview
--------
Maven PRM source packages.


Sources
-------
git clone git://github.com/tischda/almira-rpm.git


Dependencies
------------
Binaries are not checked into VCS.
To package the 'dist' directory, execute 'mvn assembly:single'


Installation
------------
Copy binary files to 'dist' directory:

+---apache-activemq
|       apache-activemq-5.8.0-bin.tar.gz
|
+---apache-ant
|       apache-ant-1.9.2-bin.tar.gz
|       apache-ivy-2.3.0-bin-with-deps.tar.gz
|
+---apache-httpd
|       apr-1.4.8.tar.bz2
|       apr-util-1.5.2.tar.bz2
|       apr.url
|       distcache-1.4.5-23.src.rpm
|       distcache.url
|       httpd-2.4.4.tar.bz2
|       httpd.url
|
+---apache-maven
|       apache-maven-3.1.0-bin.tar.gz
|
+---apache-tomcat
|   |   apache-tomcat-7.0.42.tar.gz
|   |
|   \---extra
|           catalina-jmx-remote.jar
|           catalina-ws.jar
|           tomcat-juli-adapters.jar
|           tomcat-juli.jar
|
+---atlassian-jira
|       atlassian-jira-6.0.4.tar.gz
|       mysql-connector-java-5.1.25.tar.gz
|
+---atlassian-jira-plugins
|       jira-dvcs-connector-plugin-1.4.0.1.jar
|
+---cmake
|       cmake-2.8.11.2.tar.gz
|
+---git
|       git-1.8.3.2.tar.gz
|       git-manpages-1.8.3.2.tar.gz
|       perl-YAML-0.81-20.2.noarch.rpm
|
+---nexus
|       nexus-2.5.1-01.war
|
+---oracle-mysql
|       MySQL-client-5.6.12-1.el6.x86_64.rpm
|       MySQL-devel-5.6.12-1.el6.x86_64.rpm
|       MySQL-server-5.6.12-1.el6.x86_64.rpm
|       MySQL-shared-5.6.12-1.el6.x86_64.rpm
|       MySQL-shared-compat-5.6.12-1.el6.x86_64.rpm
|
+---quickbuild
|       mysql-connector-java-5.1.25.tar.gz
|       quickbuild-5.0.29.tar.gz
|
+---sonar
|       mysql-connector-java-5.1.25.tar.gz
|       sonar-3.6.1.zip
|       sonar-plugins-3.6-2.zip
|
\---tomcat-native
        tomcat-native-1.1.27-src.tar.gz


References
----------
http://blog.quilitz.de/2010/03/checkout-sub-directories-in-git-sparse-checkouts/comment-page-1/#comment-3146
http://stackoverflow.com/questions/4114887/is-it-possible-to-do-a-sparse-checkout-without-checking-out-the-whole-repository


Knows Issues
------------
You need to specify <filemode> when specifying username and groupname, the
RPM plugin misses the defaults:

    <mapping>
        <directory>/var/run/${appServiceName}</directory>
        <username>${appUserName}</username>
        <groupname>${appGroupName}</groupname>
        <filemode>755</filemode>
    </mapping>

   will become:

    %files
    %defattr(644,root,root,755)
    %attr(755,quickbuild,quickbuild) "/home/quickbuild/quickbuild"
    %dir %attr(755,quickbuild,quickbuild) "/var/run/quickbuild"
               ^--- if not specified, it will be 644 and override the default

Another perhaps related problem is that intermediate directories in the path are
not created with default username:

    <mapping>
        <directory>${destBase}/bin</directory>
    </mapping>                 ^----- if you don't specify, 'bin' belongs to root
    <mapping>
        <directory>${destBase}/bin/jsw</directory>
                                   ^----- should belong to default username

Finally, because of the previous issue, when you do excludes, all files are
listed but not the containing directory, which now also gets owned by root.

See also:
    http://jira.codehaus.org/browse/MRPM-89
    http://jira.codehaus.org/browse/MRPM-8
    http://jira.codehaus.org/browse/MRPM-68

