#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : h2
Version  : 4.0.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/05/b8/cc1692aab910c0319b7c35e03c043bdda1cfeff67fa25b555eb2864a36e3/h2-4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/b8/cc1692aab910c0319b7c35e03c043bdda1cfeff67fa25b555eb2864a36e3/h2-4.0.0.tar.gz
Summary  : HTTP/2 State-Machine based protocol implementation
Group    : Development/Tools
License  : MIT
Requires: h2-license = %{version}-%{release}
Requires: h2-python = %{version}-%{release}
Requires: h2-python3 = %{version}-%{release}
Requires: hpack
Requires: hyperframe
BuildRequires : buildreq-distutils3
BuildRequires : hpack
BuildRequires : hyperframe
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
hyper-h2: HTTP/2 Protocol Stack
===============================

%package license
Summary: license components for the h2 package.
Group: Default

%description license
license components for the h2 package.


%package python
Summary: python components for the h2 package.
Group: Default
Requires: h2-python3 = %{version}-%{release}

%description python
python components for the h2 package.


%package python3
Summary: python3 components for the h2 package.
Group: Default
Requires: python3-core
Provides: pypi(h2)
Requires: pypi(hpack)
Requires: pypi(hyperframe)

%description python3
python3 components for the h2 package.


%prep
%setup -q -n h2-4.0.0
cd %{_builddir}/h2-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603925660
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/h2
cp %{_builddir}/h2-4.0.0/LICENSE %{buildroot}/usr/share/package-licenses/h2/80129bce9030cf215fc93006dce98b0ba8c778f8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/h2/80129bce9030cf215fc93006dce98b0ba8c778f8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
