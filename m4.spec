Name:           m4
Version:        1.4.18
Release:        16
Summary:        A GNU implementation of macro processor
License:        GPLv3+
URL:            https://www.gnu.org/software/m4/
Source0:        https://ftp.gnu.org/gnu/m4/%{name}-%{version}.tar.xz
Patch0:         m4-1.4.18-glibc-change-work-around.patch

BuildRequires:  gcc autoconf automake
Provides:       bundled(gnulib)

%description
GNU M4 is an implementation of the traditional Unix macro processor.
It is mostly SVR4 compatible although it has some extensions (for
example, handling more than 9 positional parameters to macros). GNU M4
also has built-in functions for including files, running shell commands,
doing arithmetic, etc.

%package help
Summary:        Help Document
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description help
This package provides help document for m4.

%prep
%autosetup -p1

%build
%ifarch aarch64
CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%endif
autoreconf -ivf
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir

%check
make check

%files
%doc README ChangeLog
%license COPYING AUTHORS
%{_bindir}/m4

%files help
%defattr(-,root,root)
%doc NEWS INSTALL THANKS TODO
%{_mandir}/man1/m4*
%{_infodir}/m4*

%changelog
* Wed Dec 29 2021 shixuantong <shixuantong@huawei.com> - 1.4.18-16
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:move -fsigned-char to %build

* Tue Dec 21 2021 shixuantong <shixuantong@huawei.com> - 1.4.18-15
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add -fsigned-char to %check

* Sat Dec 18 2021 shixuantong <shixuantong@huawei.com> - 1.4.18-14
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix test_localeconv fail in aarch64 machine

* Mon Dec 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.4.18-13
- Type:NA
- ID:NA
- SUG:NA
- DESC:delete unneeded source

* Mon Oct 21 2019 shenyangyang <shenyangyang4@huawei.com> - 1.4.18-12
- Type:NA
- ID:NA
- SUG:NA
- DESC:move AUTHORS to license directory

* Sun Sep 29 2019 shenyangyang <shenyangyang4@huawei.com> - 1.4.18-11
- Type:NA
- ID:NA
- SUG:NA
- DESC:move the directory of README

* Thu Aug 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.4.18-10
- Package Init
