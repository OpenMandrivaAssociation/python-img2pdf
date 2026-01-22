%define module img2pdf

Name:		python-img2pdf
Summary:	Convert images to PDF via direct JPEG inclusion
Version:	0.6.3
Release:	1
Source0:	https://pypi.io/packages/source/i/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
URL:		https://gitlab.mister-muffin.de/josch/img2pdf
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Provides:	img2pdf = %{version}-%{release}

%description
Losslessly convert raster images to PDF. The file size will not 
unnecessarily increase. One major application would be a number of scans
made in JPEG format which should now become part of a single PDF
document. Existing solutions would either re-encode the input JPEG files
(leading to quality loss) or store them in the zip/flate format which
results into the PDF becoming unnecessarily large in terms of its file
size.

%prep -a
sed -Ei "1{s@/usr/bin/env python3\$@%{__python3}@}" src/*.py

%files
%doc README.md
%{_bindir}/%{module}
%{_bindir}/%{module}-gui
%{py_puresitedir}/%{module}.py
%{py_puresitedir}/__pycache__/
%{py_puresitedir}/%{module}-%{version}.dist-info
