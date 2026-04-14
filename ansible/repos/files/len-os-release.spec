Name:           len-os-release
Version:        {{ repo_version }}
Release:        1
Summary:        Linux Enterprise OS Repository by NorTK Configuration
BuildArch:      noarch
License:        GPL

%description
This package contains the repository configuration for Linux Enterprise OS by NorTK.

%install
mkdir -p %{buildroot}/etc/yum.repos.d
cat <<EOR > %{buildroot}/etc/yum.repos.d/len_os.repo
[len_os]
name=Linux Enterprise OS Repository by NorTK
baseurl=http://{{ repo_fqdn }}/os/
enabled=1
gpgcheck=0
EOR

%files
/etc/yum.repos.d/len_os.repo

%changelog
* Tue Apr 09 2024 Iván Chavero <imcsk8@nortk.com> - 1.0-1
- Initial repository package creation
