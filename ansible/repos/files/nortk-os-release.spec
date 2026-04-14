Name:           nortk-os-release
Version:        {{ repo_version }}
Release:        1
Summary:        Nortk OS Repository Configuration
BuildArch:      noarch
License:        GPL

%description
This package contains the repository configuration for Nortk OS.

%install
mkdir -p %{buildroot}/etc/yum.repos.d
cat <<EOR > %{buildroot}/etc/yum.repos.d/nortk_os.repo
[nortk_os]
name=Nortk OS Repository
osurl=http://{{ repo_fqdn }}/os/
enabled=1
gpgcheck=0
EOR

%files
/etc/yum.repos.d/nortk_os.repo

%changelog
* Tue Apr 09 2024 Iván Chavero <imcsk8@nortk.com> - 1.0-1
- Initial repository package creation
