Name:           tacos-os-release
Version:        {{ repo_version }}
Release:        1
Summary:        TacOS Linux Repository Configuration
BuildArch:      noarch
License:        GPL

%description
This package contains the repository configuration for TacOS Linux

%install
mkdir -p %{buildroot}/etc/yum.repos.d
cat <<EOR > %{buildroot}/etc/yum.repos.d/tacos_os.repo
[len_os]
name=TacOS Linux Repository
baseurl=http://{{ repo_fqdn }}/os/
enabled=1
gpgcheck=0
EOR

%files
/etc/yum.repos.d/tacos_os.repo

%changelog
* Tue Jun 01 2026 Iván Chavero <imcsk8@nortk.com> - 0.1-1
- Initial repository package creation
