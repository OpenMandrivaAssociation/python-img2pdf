Summary:	Convert images to PDF via direct JPEG inclusion
Name:		python-img2pdf
Version:	0.5.0
Release:	1
Source0:	https://pypi.io/packages/source/i/img2pdf/img2pdf-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://gitlab.mister-muffin.de/josch/img2pdf
Provides:	img2pdf
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Losslessly convert raster images to PDF. The file size will not 
unnecessarily increase. One major application would be a number of scans
made in JPEG format which should now become part of a single PDF
document. Existing solutions would either re-encode the input JPEG files
(leading to quality loss) or store them in the zip/flate format which
results into the PDF becoming unnecessarily large in terms of its file
size.

%files
%doc README.md
%{_bindir}/img2pdf
%{_bindir}/img2pdf-gui
%{py_puresitedir}/*.py
%{py_puresitedir}/img2pdf-%{version}-py%{py_ver}.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n img2pdf-%{version}

%build
sed -i '1{/^#!\//d}' src/*.py
%py3_build

%install
%py3_install
