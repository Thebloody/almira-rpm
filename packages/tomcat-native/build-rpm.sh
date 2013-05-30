#!/bin/sh

version=`grep Version tomcat-native.spec | sed -e 's/Version: \(.*\)/\1/'`

# clean
rm -rf rpmbuild
rm -rf tomcat-native-*

# unpack (provided by CI)
#tar xzvf tomcat-native-$version-src.tar.gz
#rm -f tomcat-native-$version-src.tar.gz

# clean up
cd tomcat-native-$version-src
cp CHANGELOG.txt jni/native/CHANGES
cp LICENSE jni/native/LICENSE
cp NOTICE jni/native/NOTICE
rm -f jni/native/tcnative.spec
cd ..

# create the actual package
mv tomcat-native-$version-src/jni/native tomcat-native-$version

# inject a working spec file
cp tomcat-native.spec tomcat-native-$version
tar czvf tomcat-native-$version.tar.gz tomcat-native-$version

# build
rpmbuild -D '%_topdir %(echo $PWD)/rpmbuild' -tb tomcat-native-$version.tar.gz