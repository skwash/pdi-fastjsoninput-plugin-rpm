%global __pdi_home /opt/pentaho/data-integration
%global __pdi_plugins %{__pdi_home}/plugins/steps

Summary:    Pentaho Data Integration FastJSONInput Plugin
Name:       pdi-fastjsoninput-plugin
Version:    1.0.5
Release:    1%{?dist}
License:    Apache 2.0
Url:        https://github.com/graphiq-data/pdi-fastjsoninput-plugin
Source0:    https://github.com/graphiq-data/pdi-fastjsoninput-plugin/archive/v%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
BuildArch:  x86_64
Vendor:     Etienne Dube <etdube@gmail.com>, Jesse Adametz <jesse@graphiq.com>, James Ebentier <jebentier@graphiq.com>

BuildRequires: apache-maven
Requires: jre
Requires: pdi-ce

%description
Pentaho Data Integration FastJSONInput Plugin

%prep
%setup -n %{name}-%{version} -q

%build
mvn package

%install
mkdir -p %{buildroot}%{__pdi_home}
mvn install -Dpdi.home=%{buildroot}%{__pdi_home}

%clean
rm -rf %{buildroot}

%files
/opt/pentaho/data-integration/plugins/steps/FastJsonInput/

%defattr(-,root,root)
%attr(-,root,root) %{__pdi_plugins}/FastJsonInput
