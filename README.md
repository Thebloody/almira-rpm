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
Binaries are not checked into VCS. This is what you need in your `dist` directory:

~~~
+---apache-activemq
|       apache-activemq-5.15.0-bin.tar.gz
|
+---apache-httpd
|       apr-1.6.2.tar.bz2
|       apr-util-1.6.0.tar.bz2
|       distcache-1.4.5-23.src.rpm
|       httpd-2.4.27.tar.bz2
|
+---apache-maven
|       apache-maven-3.5.0-bin.tar.gz
|
+---apache-tomcat
|   |   apache-tomcat-7.0.79.tar.gz
|   |
|   \---extras
|           catalina-jmx-remote.jar
|           catalina-ws.jar
|           tomcat-juli-adapters.jar
|           tomcat-juli.jar
|
+---atlassian-jira-software
|       atlassian-jira-software-7.4.1.tar.gz
|       mysql-connector-java-5.1.42.tar.gz
|
+---cmake
|       cmake-3.8.2.tar.gz
|
+---git
|       git-2.13.3.tar.gz
|       git-manpages-2.13.3.tar.gz
|       git.spec
|
+---gradle
|       gradle-4.0.1-bin.zip
|
+---java
|       jdk-8u131-linux-x64.rpm
|
+---nexus
|       nexus-2.14.4-03-bundle.tar.gz
|
+---oracle-mysql
|       MySQL-client-5.6.36-1.el6.x86_64.rpm
|       MySQL-devel-5.6.36-1.el6.x86_64.rpm
|       MySQL-server-5.6.36-1.el6.x86_64.rpm
|       MySQL-shared-5.6.36-1.el6.x86_64.rpm
|       MySQL-shared-compat-5.6.36-1.el6.x86_64.rpm
|
+---quickbuild
|       mysql-connector-java-5.1.42.tar.gz
|       quickbuild-7.0.19.tar.gz
|
+---rsync
|       rsync-3.1.2.tar.gz
|
+---sonar
|   |   sonarqube-6.4.zip
|   |
|   \---plugins (add to zip in extensions_plugins)
|           sonar-cxx-plugin-0.9.7.jar
|           sonar-golang-plugin-1.2.8.jar
|           sonar-java-plugin-4.11.0.10660.jar
|           sonar-javascript-plugin-3.1.1.5128.jar
|           sonar-php-plugin-2.10.0.2087.jar
|           sonar-scm-git-plugin-1.2.jar
|           sonar-scm-mercurial-plugin-1.1.1.jar
|           sonar-scm-svn-plugin-1.4.0.522.jar
|           sonar-timeline-plugin-1.5.jar
|
\---tomcat-native
        tomcat-native-1.2.12-src.tar.gz
~~~


References
----------
* http://blog.quilitz.de/2010/03/checkout-sub-directories-in-git-sparse-checkouts/comment-page-1/#comment-3146
* http://stackoverflow.com/questions/4114887/is-it-possible-to-do-a-sparse-checkout-without-checking-out-the-whole-repository


Known Issues
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

