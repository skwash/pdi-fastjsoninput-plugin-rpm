SPECFILE=pdi-fastjsoninput-plugin.spec
TOPDIR=`pwd`/rpmbuild
SOURCEDIR=$TOPDIR/SOURCES

sudo yum-builddep $SPECFILE

echo "Create rpmbuild dir"
mkdir -p $TOPDIR/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

echo "Download sources for $SPECFILE"
spectool -C $SOURCEDIR -g $SPECFILE

echo "Build the RPM for $SPECFILE"
rpmbuild --define "_topdir $TOPDIR" \
         --define "_sourcedir $SOURCEDIR" \
         -ba $SPECFILE
