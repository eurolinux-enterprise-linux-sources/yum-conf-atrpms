Name:           yum-conf-atrpms       
Version:        6
Release:        1.1
Summary:        ATrpms configuration files for package managers.
Group:          System Environment/Base 
License:        GPL 
URL:            http://ATrpms.net/
Requires:       atrpms-repo
Requires:	yum-plugin-fastestmirror

%description
This package pulls in atrpms-repo which contains the
atrpms configuration files for yum, smart and apt.


%files


%changelog
* Tue Dec 6 2011 Pat Riehecky <riehecky@fnal.gov> - 6-1.1
- Added requires yum-plugin-fastest mirror (adding to all non SL yum-conf packages)

* Thu Jan 13 2011 Troy Dawson <dawson@fnal.gov> - 6-1
- The rpm only pulls in the appropriate release package

