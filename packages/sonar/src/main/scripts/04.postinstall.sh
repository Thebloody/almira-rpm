# Initial installation
if [ "$1" = "1" ]; then
  mkdir -p -m775 @{destBase}/{conf,logs,temp,work,webapps}
  chown :@{appGroupName} @{destBase}/{logs,temp,work,webapps}
  mkdir -p -m775 @{appWorkFolder}/conf

  cd /etc/rc.d/init.d
  ln -sf tomcat @{appServiceName}

  chkconfig --add @{appServiceName}
fi

# Link back from /etc
ln -sf @{destConf}/server.xml @{destBase}/conf/server.xml
ln -sf @{destConf}/context.xml @{destBase}/conf/context.xml
ln -sf @{destConf}/web.xml @{destBase}/conf/web.xml
ln -sf @{destConf}/catalina.policy @{destBase}/conf/catalina.policy
ln -sf @{destConf}/catalina.properties @{destBase}/conf/catalina.properties

ln -sf @{destConf}/logback.xml @{appWorkFolder}/conf/logback.xml
ln -sf @{destConf}/sonar.properties @{appWorkFolder}/conf/sonar.properties

# Recompile WAR
echo Building...
cd @{appWorkFolder}/war
chmod +x build-war.sh
chmod +x apache-ant-*/bin/ant
./build-war.sh > /dev/null 2>&1
mv build/sonar-server @{destBase}/webapps/@{appServiceName}
rm -f sonar.war