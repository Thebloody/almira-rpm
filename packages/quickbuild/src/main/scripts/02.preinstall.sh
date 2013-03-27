# Create user and group
getent group @{appGroupName} > /dev/null || groupadd -r @{appGroupName}
getent passwd @{appUserName} > /dev/null || useradd -r -m -g @{appGroupName} @{appUserName}

# Uninstall or Update => stop service
if [ "$1" = "0" -o "$1" = "2" ]; then
  service @{appServiceName} stop
fi

# Update => Save old folder for migration, and get rid of symlinks
if [ "$1" = "2" ]; then
  echo backing up old version
  rm -f @{destBase}/conf
  cp -r @{destConf} @{destBase}/conf
  mv @{destBase} @{destBase}.old
fi
