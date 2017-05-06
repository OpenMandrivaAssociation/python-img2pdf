%define module	img2pdf

Summary:	Convert images to PDF via direct JPEG inclusion
Name:		python-img2pdf
Version:	0.2.3
Release:	1
Source0:	http://pybrary.net/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pybrary.net/img2pdf/
Provides:	%{module}
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
%{_bindir}/%{module}
%{py_puresitedir}/%{module}-%{version}-py%{py_ver}.egg-info
%{py_puresitedir}/*.py

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --no-compile

