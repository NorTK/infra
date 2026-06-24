%global distro          TacOS
%define release_name    Arrachera
%define release_type    stable
%global major           {{ spec_major_version }}
%global minor           {{ spec_minor_version }}

Name:           tacos-repo
Version:        %{major}.%{minor}
Release:        {{ spec_release_version }}%{?dist}
Summary:        TacOS Linux Repository Configuration
BuildArch:      noarch
License:        GPL

%description
This package contains repositories configurations for TacOS Linux

%install
mkdir -p %{buildroot}/etc/yum.repos.d
cat <<EOR > %{buildroot}/etc/yum.repos.d/tacos.repo
[tacos]
name=TacOS Linux Repository
baseurl=http://{{ repo_fqdn }}/{{ spec_major_version }}/BaseOS/$basearch/os
enabled=1
gpgcheck=0

[tacos-source]
name=TacOS Linux Repository
baseurl=http://{{ repo_fqdn }}/{{ spec_major_version }}/BaseOS/source/tree
enabled=1
gpgcheck=0

EOR

%files
/etc/yum.repos.d/tacos.repo

%changelog
* Tue Jun 01 2026 Iván Chavero <imcsk8@nortk.com> - 0.1-1
- Initial repository package creation
