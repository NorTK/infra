Name:           nortk-erp-release
Version:        {{ repo_version }}
Release:        1
Summary:        Nortk ERP Repository Configuration
BuildArch:      noarch
License:        GPL

%description
This package contains the repository configuration for Nortk ERP.

%install
mkdir -p %{buildroot}/etc/yum.repos.d
cat <<EOR > %{buildroot}/etc/yum.repos.d/nortk_erp.repo
[nortk_erp]
name=Nortk ERP Repository
baseurl=http://{{ repo_fqdn }}/erp/
enabled=1
gpgcheck=0
EOR

%files
/etc/yum.repos.d/nortk_erp.repo

%changelog
* Tue Apr 09 2024 Iván Chavero <imcsk8@nortk.com> - 1.0-1
- Initial repository package creation
